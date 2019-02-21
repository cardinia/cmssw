#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <iomanip>
#include <experimental/filesystem>
#include "TPad.h"
#include "TCanvas.h"
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TMultiGraph.h"
#include "TH1.h"
#include "THStack.h"
#include "TROOT.h"
#include "TFile.h"
#include "TColor.h"
#include "TLegend.h"
#include "TLegendEntry.h"
#include "TMath.h"
#include "TRegexp.h"
#include "TPaveLabel.h"
#include "TPaveText.h"
#include "TStyle.h"
#include "TLine.h"

using namespace std;
namespace fs = std::experimental::filesystem;

/*!
 * \def Dummy value in case a DMR would fail for instance
 */
#define DUMMY -999.
/*!
 * \def Scale factor value to have mean and sigmas expressed in micrometers. This incidentally is the same factor needed to express luminosity in fb^-1
 */
#define SFactor 1000.

/*! \struct Point
 *  \brief Structure Point
 *         Contains parameters of Gaussian fits to DMRs
 *  
 * @param run:             run number (IOV boundary)
 * @param mu:              mu/mean from Gaussian fit to DMR
 * @param sigma:           sigma/standard deviation from Gaussian fit to DMR
 * @param muplus:          mu/mean for the inward pointing modules
 * @param muminus:         mu/mean for outward pointing modules
 * @param sigmaplus:       sigma/standard for inward pointing modules 
 * @param sigmaminus: //!< sigma/standard for outward pointing modules
 */
struct Point {
    float run, mu, sigma, muplus, muminus, sigmaplus, sigmaminus; 

    /*! \fn Point
     *  \brief Constructor of structure Point, initialising all members one by one
     */
    Point (float Run = DUMMY, float y1 = DUMMY,float y2 = DUMMY, float y3 = DUMMY, float y4 = DUMMY, float y5 = DUMMY, float y6 = DUMMY) :
        run(Run), mu(y1), sigma(y2), muplus(y3), muminus(y5), sigmaplus(y4), sigmaminus(y6)
    {}

    /*! \fn Point
     *  \brief Constructor of structure Point, initialising all members from DMRs directly (with split)
     */
    Point (float Run, TH1 * histo, TH1 * histoplus, TH1 * histominus) :
        Point(Run, histo->GetMean(), histo->GetMeanError(),
                histoplus->GetMean(), histoplus->GetMeanError(),
                histominus->GetMean(), histominus->GetMeanError())
    {}

    /*! \fn Point
     *  \brief Constructor of structure Point, initialising all members from DMRs directly (without split)
     */
    Point (float Run, TH1 * histo) :
        Point(Run, histo->GetMean(), histo->GetMeanError())
    {}

    Point& operator=(const Point &p){ run = p.run; mu = p.mu;  muplus = p.muplus;  muminus = p.muminus; sigma = p.sigma;  sigmaplus = p.sigmaplus;  sigmaminus = p.sigmaminus; return *this;}

    float GetRun          () const { return run       ; } 
    float GetMu           () const { return SFactor*mu        ; } 
    float GetMuPlus       () const { return SFactor*muplus    ; } 
    float GetMuMinus      () const { return SFactor*muminus   ; } 
    float GetSigma        () const { return SFactor*sigma     ; } 
    float GetSigmaPlus    () const { return SFactor*sigmaplus ; } 
    float GetSigmaMinus   () const { return SFactor*sigmaminus; } 
    float GetDeltaMu      () const { if(muplus==DUMMY&&muminus==DUMMY) return DUMMY;
        else return SFactor*(muplus - muminus); }
        float GetSigmaDeltaMu () const { if(sigmaplus==DUMMY&&sigmaminus==DUMMY) return DUMMY;
            else return SFactor*hypot(sigmaplus,sigmaminus); };
};


///**************************
///*  Function declaration  *
///**************************

TString getName (TString structure, int layer, TString geometry);
TH1F* ConvertToHist(TGraphErrors *g); 
vector<int> runlistfromlumifile(string scalefile="/afs/cern.ch/work/h/hpeterse/public/lumiPerRun80.csv"); 
bool checkrunlist(vector<int> runs);
void scalebylumi(TGraphErrors *g, double min=0., string scalefile="/afs/cern.ch/work/h/hpeterse/public/lumiPerRun80.csv"); 
void scalebylumi(TGraph *g, double min=0., string scalefile="/afs/cern.ch/work/h/hpeterse/public/lumiPerRun80.csv"); 
//old /afs/cern.ch/work/h/hpeterse/public/lumiPerRun80.csv
//new /afs/cern.ch/work/h/hpeterse/public/lumiPerRun80.csv
double getintegratedlumiuptorun(int run, double min=0., string scalefile="/afs/cern.ch/work/h/hpeterse/public/lumiPerRun80.csv");
void PixelUpdateLines(TCanvas *c, bool showlumi=false, vector<int>pixelupdateruns={314881, 316758, 317527, 318228, 320377});
void PlotDMRTrends(string label="v11", string type="MB", string myValidation="/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/acardini/DMRs/", vector<string> geometries={"GT","SG", "MP pix LBL","PIX HLS+ML STR fix"}, vector<Color_t> colours={kBlue, kRed, kGreen, kCyan}, TString outputdir="/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/alignmentObjects/acardini/DMRsTrends/", bool pixelupdate=false, bool showlumi=false);
void compileDMRTrends(string label="v11", string myValidation="/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/acardini/DMRs/", vector<string> geometries={"GT","SG", "MP pix LBL","PIX HLS+ML STR fix"}, string type="MB", bool showlumi=false, bool hideproblems=false);
void DMRtrends(string label="v11", string myValidation="/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/acardini/DMRs/", vector<string> geometries={"GT","SG", "MP pix LBL","PIX HLS+ML STR fix"}, vector<Color_t> colours={kBlue, kRed, kGreen, kCyan}, TString outputdir="/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/alignmentObjects/acardini/DMRsTrends/", string type="MB", bool pixelupdate=false, bool showlumi=false, bool hideproblems=false);

/*! \class Geometry
 *  \brief Class Geometry
 *         Contains vector for fit parameters (mean, sigma, etc.) obtained from multiple IOVs
 *         See Structure Point for description of the parameters.
 */

class Geometry {
    public:
        vector<Point> points;
    private:
        //template<typename T> vector<T> GetQuantity (T (Point::*getter)() const) const {
        vector<float> GetQuantity (float (Point::*getter)() const) const {
            vector<float> v;
            for (Point point: points) {
                float value = (point.*getter)();
                v.push_back(value);
            }
            return v;
        }
    public:
        TString title;
        Geometry() : title ("") {}
        Geometry(TString Title) : title(Title) {}
        Geometry& operator=(const Geometry &geom){ title = geom.title; points = geom.points; return *this;}
        void SetTitle(TString Title){ title = Title;}
        TString GetTitle() { return title; }
        vector<float> Run             () const { return GetQuantity( &Point::GetRun         ); }
        vector<float> Mu              () const { return GetQuantity( &Point::GetMu          ); }
        vector<float> MuPlus          () const { return GetQuantity( &Point::GetMuPlus      ); }
        vector<float> MuMinus         () const { return GetQuantity( &Point::GetMuMinus     ); }
        vector<float> Sigma           () const { return GetQuantity( &Point::GetSigma       ); }
        vector<float> SigmaPlus       () const { return GetQuantity( &Point::GetSigmaPlus   ); }
        vector<float> SigmaMinus      () const { return GetQuantity( &Point::GetSigmaMinus  ); }
        vector<float> DeltaMu         () const { return GetQuantity( &Point::GetDeltaMu     ); }
        vector<float> SigmaDeltaMu    () const { return GetQuantity( &Point::GetSigmaDeltaMu); }
        //vector<float> Graph (string variable) const {
        // };
};

/// DEPRECATED
//struct Layer {
//    map<string,Geometry> geometries;
//};
//
//struct HLS {
//    vector<Layer> layers;
//    map<string,Geometry> geometries;
//};


/*! \fn getName
 *  \brief Function used to get a string containing information on the high level structure, the layer/disc and the geometry.
 */

TString getName (TString structure, int layer, TString geometry){
    geometry.ReplaceAll(" ","_");
    TString name=geometry+"_"+structure;
    if(layer!=0){
        if(structure=="TID"||structure=="TEC")name+="_disc";
        else name+="_layer";
        name+=layer;
    }

    return name;
};

/*! \fn runlistfromlumifile
 *  \brief Get a vector containing the list of runs for which the luminosity is known.
 */

vector<int> runlistfromlumifile(string scalefile){
    TGraph * scale = new TGraph(scalefile.c_str());
    double *xscale = scale->GetX();
    size_t N = scale->GetN();
    vector<int> runs;
    for(size_t i=0;i<N;i++)runs.push_back(xscale[i]);
    return runs;
} 

/*! \fn checkrunlist
 *  \brief Get a vector containing the list of runs for which the luminosity is known.
 */

bool checkrunlist(vector<int> runs){
    vector<int> runlist = runlistfromlumifile();
    vector<int> missingruns;
    bool problemfound=false;
    for(int run : runs){
      if(find(runlist.begin(),runlist.end(),run)==runlist.end()){
	problemfound=true;
	missingruns.push_back(run);
      }
    }
    std::sort(missingruns.begin(),missingruns.end());
    if(problemfound){
      cout << "WARNING: some runs are missing in the run/luminosity txt file" << endl << "List of missing runs:" << endl;
      for (int missingrun : missingruns) cout << to_string(missingrun) << " ";
      cout << endl;
    }
    return problemfound;

} 

/*! \fn DMRtrends
 *  \brief Create and plot the DMR trends.
 */

void DMRtrends(string label, string myValidation, vector<string> geometries, vector<Color_t> colours, TString outputdir, string type, bool pixelupdate, bool showlumi, bool hideproblems){

  compileDMRTrends(label, myValidation, geometries, type, showlumi, hideproblems);
  PlotDMRTrends(label, type, myValidation, geometries, colours, outputdir, pixelupdate, showlumi);

};

/*! \fn compileDMRTrends
 *  \brief  Create a file where the DMR trends are stored in the form of TGraph.
 */

void compileDMRTrends(string label, string myValidation, vector<string> geometries, string type, bool showlumi, bool hideproblems){
    gROOT->SetBatch();
    vector<int>RunNumbers;
    vector<TString> filenames;
    TRegexp regexp("[0-9][0-9][0-9][0-9][0-9][0-9]");
    for (const auto & entry : fs::recursive_directory_iterator(myValidation)){
      if ((entry.path().string().find("ExtendedOfflineValidation_Images/OfflineValidationSummary.root")!=std::string::npos)&&(entry.path().string().find(label)!=std::string::npos)){
	if(fs::is_empty(entry.path())) cout << "ERROR: Empty file " << entry.path() << endl;
	else{
	  TString filename(entry.path().string());
	  filenames.push_back(filename);
	  TString runstring(filename(regexp));
	  if(runstring.IsFloat()){
	    int runN=runstring.Atoi();
	    RunNumbers.push_back(runN);
	  }
	}
      }
    }
    if(checkrunlist(RunNumbers)&&showlumi&&!hideproblems){
      cout << "Please fix the run/luminosities file!" << endl;
      exit(EXIT_FAILURE);
    }
    vector<int> pixelupdateruns {314881, 316758, 317527, 318228, 320377};

    vector<TString> structures { "BPIX", "BPIX_y", "FPIX", "FPIX_y", "TIB", "TID", "TOB", "TEC"};

    const map<TString,int> nlayers{ {"BPIX", 4}, {"FPIX", 3}, {"TIB", 4}, {"TID", 3}, {"TOB", 6}, {"TEC", 9} };


    map<pair<pair<TString,int>,TString>,Geometry> mappoints; // pair = (structure, layer), geometry
    
    std::sort(filenames.begin(),filenames.end());//order the files in alphabetical order
    for (TString filename: filenames){
        int runN;
        TString runstring(filename(regexp));
        if(runstring.IsFloat()){
	  runN=runstring.Atoi();
	}
        else{
	  cout << "ERROR: run number not retrieved for file " << filename << endl;
	  continue;
	}

        TFile * f = new TFile(filename, "READ");

        for (TString& structure: structures) {
            TString structname = structure;
            structname.ReplaceAll("_y", "");
            size_t layersnumber=nlayers.at(structname);
            for (size_t layer=0; layer<=layersnumber;layer++){
                for (string geometry: geometries) {
                    TString name = getName(structure, layer, geometry);
                    TH1F *histo      = dynamic_cast<TH1F*>(f->Get( name));
                    //Geometry *geom =nullptr;
                    Point * point = nullptr;
                    if(!histo){
                        cout << "Run" << runN << " Histogram: " << name << " not found" << endl;
                        point= new Point(runN);
			if(hideproblems)continue;
                    }else if(structure!="TID"&&structure!="TEC"){
                        TH1F *histoplus  = dynamic_cast<TH1F*>(f->Get((name+"_plus")));
                        TH1F *histominus = dynamic_cast<TH1F*>(f->Get((name+"_minus")));						  
                        if(!histoplus||!histominus){
                            cout << "Run" << runN << " Histogram: " << name << " plus or minus not found" << endl;
                            point= new Point(runN, histo);
			    if(hideproblems)continue;
                        }else point= new Point(runN, histo, histoplus, histominus);

                    }else point= new Point(runN, histo);
                    mappoints[make_pair(make_pair(structure,layer),geometry)].points.push_back(*point);
                }
            }
        }
        f->Close();
    }
    TString outname=myValidation+"DMRtrends_";
    outname+=type.c_str(); outname+="_"; outname+=label; outname+=".root";	
    TFile * fout = TFile::Open(outname, "RECREATE");
    for (TString& structure: structures) {
        TString structname = structure;
        structname.ReplaceAll("_y", "");
        size_t layersnumber=nlayers.at(structname);
        for (size_t layer=0; layer<=layersnumber;layer++){
            for (string geometry : geometries) {
                TString name = getName(structure, layer, geometry);
                Geometry geom = mappoints[make_pair(make_pair(structure,layer),geometry)];
                using Trend = vector<float> (Geometry::*)() const;
                vector<Trend> trends {&Geometry::Mu, &Geometry::Sigma, &Geometry::MuPlus, &Geometry::SigmaPlus, 
                    &Geometry::MuMinus, &Geometry::SigmaMinus, &Geometry::DeltaMu, &Geometry::SigmaDeltaMu };
                vector<TString> variables {"mu", "sigma", "muplus", "sigmaplus", "muminus", "sigmaminus", "deltamu", "sigmadeltamu" };
                vector<float> runs = geom.Run();
                size_t n = runs.size();
                vector<float> emptyvec;
                for(size_t i=0; i < runs.size(); i++)emptyvec.push_back(0.);
                for(size_t iVar=0; iVar < variables.size(); iVar++){
                    Trend trend=trends.at(iVar);
                    TGraphErrors *g = new TGraphErrors(n, runs.data(), (geom.*trend)().data(), emptyvec.data(), emptyvec.data());
                    g->SetTitle(geometry.c_str());
                    g->Write(name+"_"+variables.at(iVar));
                }
                vector<pair<Trend,Trend>> trendspair {make_pair(&Geometry::Mu, &Geometry::Sigma), make_pair(&Geometry::MuPlus, &Geometry::SigmaPlus), 
		    make_pair(&Geometry::MuMinus, &Geometry::SigmaMinus), make_pair(&Geometry::DeltaMu, &Geometry::SigmaDeltaMu) };
                vector<pair<TString,TString>> variablepairs {make_pair("mu", "sigma"), make_pair("muplus", "sigmaplus"), make_pair("muminus", "sigmaminus"), make_pair("deltamu", "sigmadeltamu") };
                for(size_t iVar=0; iVar < variablepairs.size(); iVar++){
                    Trend meantrend=trendspair.at(iVar).first;
                    Trend sigmatrend=trendspair.at(iVar).second;
                    TGraphErrors *g = new TGraphErrors(n, runs.data(), (geom.*meantrend)().data(), emptyvec.data(), (geom.*sigmatrend)().data());
                    g->SetTitle(geometry.c_str());
                    TString graphname = name+"_"+variablepairs.at(iVar).first;
                    graphname+=variablepairs.at(iVar).second;
                    g->Write(graphname);
                }
            }
        }
    }
    fout->Close();

}


void PixelUpdateLines(TCanvas *c, bool showlumi, vector<int>pixelupdateruns){
	vector<TPaveText*> labels;
	double lastlumi=0.;
	c->cd();
	for(int pixelupdaterun : pixelupdateruns){
	       double lumi=0.;
	       if(showlumi)lumi=getintegratedlumiuptorun(pixelupdaterun);
	       else lumi=pixelupdaterun;
	       TLine *line = new TLine (lumi,c->GetUymin(),lumi,c->GetUymax());
	       line->SetLineColor(kBlack);
	       //line->SetLineWidth(1);
	       line->SetLineStyle(9);
	       line->Draw();
	       
	       int ix1;
	       int ix2;
	       int iw = gPad->GetWw();
	       int ih = gPad->GetWh();
	       double x1p,y1p,x2p,y2p;
	       gPad->GetPadPar(x1p,y1p,x2p,y2p);
	       
	       ix1 = (Int_t)(iw*x1p);
	       ix2 = (Int_t)(iw*x2p);
	       double wndc  = TMath::Min(1.,(double)iw/(double)ih);
	       double rw    = wndc/(double)iw;
	       double x1ndc = (double)ix1*rw;
	       double x2ndc = (double)ix2*rw;
	       double rx1,ry1,rx2,ry2;
	       gPad->GetRange(rx1,ry1,rx2,ry2);
	       double rx = (x2ndc-x1ndc)/(rx2-rx1);
	       double _sx;
	       _sx = rx*(lumi-rx1)+x1ndc;
	       bool tooclose = false;
	       if( ((lumi-lastlumi) < (showlumi ? 2 : 500)) && lastlumi!=0 )tooclose=true;
	       TPaveText *box= new TPaveText(_sx+0.001,0.87-tooclose*0.04,_sx+0.045,0.89-tooclose*0.04,"blNDC");
	       TText *textRun = box->AddText(Form("%i",int(pixelupdaterun)));
	       textRun->SetTextSize(0.025);
	       labels.push_back(box);
	       lastlumi=lumi;
	}
	//Drawing in a separate loop to ensure that the labels are drawn on top of the lines
	for(auto label: labels){
	       label->Draw("same");
	}
	c->Update();
}


double getintegratedlumiuptorun(int run, double min, string scalefile){
    TGraph * scale = new TGraph(scalefile.c_str());
    int Nscale=scale->GetN();
    double *xscale=scale->GetX();
    double *yscale=scale->GetY();


    double lumi=min;
    int index=-1;
    for(int j=0;j<Nscale;j++){
        lumi+=yscale[j];
        if(run==xscale[j]){
            index=j;
            continue;
        }else if(run>xscale[j]){
	      index=j-1;
	      continue;
	}
    }
    lumi=min;  
    for(int j=0;j<index;j++)lumi+=yscale[j]/SFactor;

    return lumi;

}
/*! \fn scalebylumi
 *  \brief Scale X-axis of the TGraph and the error on that axis according to the integrated luminosity.
 */
///TO FIX: currently the error on the x axis result in a segmentation fault:

void scalebylumi(TGraphErrors *g, double min, string scalefile){ 
    size_t N=g->GetN();
    vector<double> x,y,xerr,yerr;

    TGraph * scale = new TGraph(scalefile.c_str());
    size_t Nscale=scale->GetN();
    double *xscale=scale->GetX();
    double *yscale=scale->GetY();

    size_t i=0;
    while(i<N){
        double run,yvalue;
	g->GetPoint(i,run,yvalue);
        size_t index=-1;
        for(size_t j=0;j<Nscale;j++){
            if(run==xscale[j]){
                index=j;
                continue;
            }else if(run>xscale[j]) continue;
        }
        if(yscale[index]==0||index<0.){
            N=N-1;
            g->RemovePoint(i);
        }else{
	    double xvalue=min;
            for(size_t j=0;j<index;j++)xvalue+=yscale[j]/SFactor;
	    x   .push_back(xvalue+(yscale[index]/(SFactor*2.)));
	    if(yvalue<=DUMMY){
	      y.push_back(DUMMY);
	      yerr.push_back(0.);
	    }else{
	      y.push_back(yvalue);
	      yerr.push_back(g->GetErrorY(i));
	    }
	    xerr.push_back(yscale[index]/(SFactor*2.));
            i=i+1;
        }

    } 
    g->GetHistogram()->Delete(); 
    g->SetHistogram(0); 
    for(size_t i=0;i<N;i++){ g->SetPoint(i, x.at(i),y.at(i)); g->SetPointError(i, xerr.at(i),yerr.at(i));}

}

void scalebylumi(TGraph *g, double min, string scalefile){ 
    size_t N=g->GetN();
    vector<double> x,y,xerr,yerr;

    TGraph * scale = new TGraph(scalefile.c_str());
    size_t Nscale=scale->GetN();
    double *xscale=scale->GetX();
    double *yscale=scale->GetY();

    size_t i=0;
    while(i<N){
        double run,yvalue;
	g->GetPoint(i,run,yvalue);
        size_t index=-1;
        for(size_t j=0;j<Nscale;j++){
            if(run==xscale[j]){
                index=j;
                continue;
            }else if(run>xscale[j]) continue;
	    
        }
        if(yscale[index]==0||index<0.){
            N=N-1;
            g->RemovePoint(i);
        }else{
	    double xvalue=min;
            for(size_t j=0;j<index;j++)xvalue+=yscale[j]/SFactor;
	    x   .push_back(xvalue+yscale[index]/(SFactor*2.));
	    if(yvalue<=DUMMY){
	      y.push_back(DUMMY);
	    }else{
	      y.push_back(yvalue);
	    }
            i=i+1;
        }

    } 
    g->GetHistogram()->Delete(); 
    g->SetHistogram(0); 
    for(size_t i=0;i<N;i++){
      Double_t xdouble=x.at(i);
      Double_t ydouble=y.at(i);
      g->SetPoint(i, xdouble,ydouble);

    }
}


TH1F *ConvertToHist(TGraphErrors *g){ 
    size_t N=g->GetN();
    double* x=g->GetX();
    double* y=g->GetY();
    double* xerr=g->GetEX();
    vector<float> bins;
    bins.push_back(x[0]-xerr[0]);
    for(size_t i=1;i<N;i++){
      if((x[i-1]+xerr[i-1]) > (bins.back() + pow(10,-6))) bins.push_back(x[i-1]+xerr[i-1]);
      if((x[i]-xerr[i])     > (bins.back() + pow(10,-6))) bins.push_back(x[i]-xerr[i]);
      
    }
    bins.push_back(x[N-1]+xerr[N-1]);
    TString histoname="histo_";
    histoname+=g->GetName();
    TH1F *histo = new TH1F(histoname,g->GetTitle(),bins.size()-1,bins.data());
    for(size_t i=0;i<N;i++){
      histo->Fill(x[i],y[i]);
      histo->SetBinError(histo->FindBin(x[i]),pow(10,-6));
    }
  return histo;
}


/*! \fn PlotDMRTrends
 *  \brief Plot the DMR trends.
 */

void PlotDMRTrends(string label, string type, string myValidation, vector<string> geometries, vector<Color_t> colours, TString outputdir, bool pixelupdate, bool showlumi){
  gErrorIgnoreLevel = kWarning;
    vector<int> pixelupdateruns {314881, 316758, 317527, 318228, 320377};

    vector<TString> structures { "BPIX", "BPIX_y", "FPIX", "FPIX_y", "TIB", "TID", "TOB", "TEC"};

    const map<TString,int> nlayers{ {"BPIX", 4}, {"FPIX", 3}, {"TIB", 4}, {"TID", 3}, {"TOB", 6}, {"TEC", 9} };


    //	vector<string> geometries {"GT", "PIXHLS+MLSTRfix"};
    //	vector<Color_t> colours { kBlack, kRed}; 
    TString filename=myValidation+"DMRtrends_"+type+"_"+label+".root";
    TFile *in= new TFile(filename);
    for (TString& structure: structures) {
        TString structname = structure;
        structname.ReplaceAll("_y", "");
        int layersnumber=nlayers.at(structname);
        for (int layer=0; layer<=layersnumber;layer++){
            vector<TString> variables {"mu", "sigma", "muplus", "sigmaplus", "muminus", "sigmaminus", "deltamu", "sigmadeltamu", "musigma", "muplussigmaplus", "muminussigmaminus", "deltamusigmadeltamu"};
            vector<string> YaxisNames { "#mu [#mum]", "#sigma_{#mu} [#mum]", "#mu outward [#mum]", "#sigma_{#mu outward} [#mum]", "#mu inward [#mum]", "#sigma_{#mu inward} [#mum]", "#Delta#mu [#mum]", "#sigma_{#Delta#mu} [#mum]", "#mu [#mum]", "#mu outward [#mum]", "#mu inward [#mum]", "#Delta#mu [#mum]",}; 
            for(size_t i=0; i < variables.size(); i++){
                TString variable= variables.at(i);
                TCanvas * c = new TCanvas("dummy","",2000,800);
                vector<Color_t>::iterator colour = colours.begin();

                TMultiGraph *mg = new TMultiGraph(structure,structure);
                THStack *mh = new THStack(structure,structure);
		size_t igeom=0;
                for (string geometry: geometries) {
                    TString name = getName(structure, layer, geometry);
                    TGraphErrors *g = dynamic_cast<TGraphErrors*> (in->Get(name+"_"+variables.at(i)));
		    g->SetName(name+"_"+variables.at(i));
                    if(i>=8){
                        g->SetLineWidth(1);
			g->SetLineColor(*colour);
                        g->SetFillColorAlpha(*colour,0.2);
                    }else g->SetMarkerStyle(20);
		    vector<vector<double>> vectors; 
		    //if(showlumi&&i<8)scalebylumi(dynamic_cast<TGraph*>(g));
		    if(showlumi)scalebylumi(g);
		    g->SetLineColor(*colour);
                    g->SetMarkerColor(*colour);
		    TH1F *h = ConvertToHist(g); 
 		    h->SetLineColor(*colour);
 		    h->SetMarkerColor(*colour);
 		    h->SetMarkerSize(0);
		    h->SetLineWidth(2);

                    if(i<8){
		      mg->Add(g,"PL");
		      mh->Add(h,"E");
                    }else{
		      mg->Add(g,"2");
		      mh->Add(h,"E");
                    }
                    ++colour;
		    ++igeom;
                }
                if(i<8){
		  mg->Draw("a");
                }else{
		  mg->Draw("a2");
		}
                double max=0.7;
                double min=-0.5;
                double range=max-min;
                if(variable=="deltamusigmadeltamu")max=1,min=-0.8;
                if(((variable=="sigma"||variable=="sigmaplus"||variable=="sigmaminus"||variable=="sigmadeltamu")&&range>=2)){
                    mg->SetMaximum(0.5);
                    mg->SetMinimum(-0.4);
                }else{
                    mg->SetMaximum(max+range*0.1);
                    mg->SetMinimum(min-range*0.3);
                }

                char* Ytitle= (char *)YaxisNames.at(i).c_str();
                mg->GetYaxis()->SetTitle(Ytitle);
                mg->GetXaxis()->SetTitle(showlumi ? "Integrated lumi [1/fb]" : "IOV number");
                mg->GetYaxis()->SetTitleOffset(.5);
                mg->GetYaxis()->SetTitleSize(.05);
                mg->GetXaxis()->SetTitleSize(.04);
		mg->GetXaxis()->SetLimits(0.,mg->GetXaxis()->GetXmax());
                gStyle->SetOptTitle(0); // TODO
                c->SetLeftMargin(0.11);
                TString typetitle="";
                if(type=="MB")typetitle="Minimum Bias";
                if(type=="SM")typetitle="Single Muon";

                c->Update();

		//gStyle->SetLegendBorderSize(0);
		gStyle->SetLegendTextSize(0.025);

                TLegend *legend = c->BuildLegend(0.35,0.1,0.35,0.1);
                //legend->SetHeader(typetitle.Data());
                //TLegendEntry *header = (TLegendEntry*)legend->GetListOfPrimitives()->First();
                //header->SetTextSize(.04);
		int Ngeom=geometries.size();
                legend->SetNColumns(Ngeom);
                //legend->SetTextSize(0.05);
                TString structtitle = "structure: " +structure;
                if(layer!=0){
                    if(structure=="TID"||structure=="TEC")structtitle+="_disc";
                    else structtitle+="_layer";
                    structtitle+=layer;
                }
                //legend->AddEntry((TObject*)0,structtitle.Data(),"h");
                //TLegendEntry *str = (TLegendEntry*)legend->GetListOfPrimitives()->Last();
                //str->SetTextSize(.03);
                PixelUpdateLines(c, showlumi, pixelupdateruns);

		legend->Draw();
		mh->Draw("nostack same");
                c->Update();
                TString structandlayer = getName(structure,layer,"");
                TString printfile=outputdir+label+"-"+type+"_"+variable+structandlayer;
                c->SaveAs(printfile+".pdf");
                c->SaveAs(printfile+".eps");
                c->SaveAs(printfile+".png");
		//c->Close();
		c->Destructor();
            }

        }

    }
    in->Close();
}

int main (int argc, char * argv[]) { 

	if (argc == 1) {
	        cout << "WARNING: Running function with arguments specified in DMRtrends.cc" << endl << "If you want to specify the arguments from command line run the macro as follows:" << endl << "DMRtrends label pathtoDMRs geometriesandcolourspairs outputdirectory type showpixelupdate showlumi hideproblems" << endl;
		DMRtrends("v3", "/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/acardini/DMRs/EOY18_v3/", {"GT","Pix ML Strip fixed -high IOV Gran-","Pix+Strip ML -low IOV Gran-"}, {kBlue, kRed, kGreen, kCyan}, "/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/alignmentObjects/acardini/DMRsTrends/", "MB", true, true, true); 
		
		return 0;
	}
	else if (argc < 9) {
		cout << "DMRtrends label pathtoDMRs geometriesandcolourspairs outputdirectory type showpixelupdate showlumi hideproblems" << endl;
		
		return 1;
	}

	TString label = argv[1],
		pathtoDMRs = argv[2],
		geometrieandcolours = argv[3], //name1:title1:color1,name2:title2:color2,name3:title3:color3
		outputdirectory = argv[4],
	        type = argv[5];
	bool	showpixelupdate = argv[6],
		showlumi = argv[7],
		hideproblems = argv[8];

	vector<string> geometries;
	vector<Color_t> colours;
	TObjArray *geometrieandcolourspairs = geometrieandcolours.Tokenize(",");
	for (int i=0; i < geometrieandcolourspairs->GetEntries(); i++) {
	        TObjArray *geomandcolourvec = TString(geometrieandcolourspairs->GetName()).Tokenize("|");
		geometries.push_back(geomandcolourvec->At(0)->GetName());
		colours.push_back((Color_t)(atoi(geomandcolourvec->At(1)->GetName())));
	}
	DMRtrends(label.Data(),pathtoDMRs.Data(),geometries,colours,outputdirectory.Data(),type.Data(),showpixelupdate,showlumi,hideproblems);

	
	return 0; 
}
