
#include "MuonAnalysis/MomentumScaleCalibration/test/Macros/RooFit/MultiHistoOverlapAll_Z.C"
#include <sstream>
#include <vector>

template <typename T> string separatebycommas(vector<T> v){
  if (v.size()==0) return "";
  stringstream s;
  s << v[0];
  for (unsigned int i = 1; i < v.size(); i++) s << "," << v[i];
  return s.str();
}

void TkAlMergeZmumuPlots(){
  vector<string> filenames; vector<string> titles; vector<int> colors; vector<int> linestyles;

    filenames.push_back("root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/validation_Zmumu_mp3217_mp3218/Zmumu_EOY2016_newTemplates/ZMuMuValidation/ZmumuValidation/UL16/BiasCheck.root");  titles.push_back("UL16");  colors.push_back(1);  linestyles.push_back(2101);
    filenames.push_back("root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/validation_Zmumu_mp3217_mp3218/Zmumu_EOY2016_newTemplates/ZMuMuValidation/ZmumuValidation/UL16newtemplates/BiasCheck.root");  titles.push_back("UL16 new templates");  colors.push_back(600);  linestyles.push_back(2101);
    filenames.push_back("root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/validation_Zmumu_mp3217_mp3218/Zmumu_EOY2016_newTemplates/ZMuMuValidation/ZmumuValidation/mp3217/BiasCheck.root");  titles.push_back("only pixel multi IOV");  colors.push_back(632);  linestyles.push_back(2101);
    filenames.push_back("root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/validation_Zmumu_mp3217_mp3218/Zmumu_EOY2016_newTemplates/ZMuMuValidation/ZmumuValidation/mp3218/BiasCheck.root");  titles.push_back("pixel+strips multi IOV");  colors.push_back(418);  linestyles.push_back(2101);

  vector<int> linestyles_new, markerstyles_new;
  for (unsigned int j=0; j<linestyles.size(); j++){ linestyles_new.push_back(linestyles.at(j) % 100); markerstyles_new.push_back(linestyles.at(j) / 100); }

  TkAlStyle::legendheader = "Alignments";
  TkAlStyle::set(CUSTOM, NONE, "EOY2016", "Data");

  MultiHistoOverlapAll_Z(separatebycommas(filenames), separatebycommas(titles), separatebycommas(colors), separatebycommas(linestyles_new), separatebycommas(markerstyles_new), "/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/jmetwall/Zmumu_EOY2016_newTemplates/ZMuMuPlots", false, false, 90.85, 91.4);
}
