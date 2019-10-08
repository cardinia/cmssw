import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/557/00000/90A6AC1E-A45C-E711-A05F-02163E013420.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/558/00000/B8FB97F2-945C-E711-83CB-02163E01A69D.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/593/00000/227AF6A0-DB5C-E711-AA09-02163E011B4E.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/562/00000/FE9C3B69-C05C-E711-9A5E-02163E013565.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/585/00000/1443710F-D35C-E711-8063-02163E01A280.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/557/00000/D0074FCA-8C5C-E711-9DAB-02163E0144DB.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/589/00000/38D23798-DA5C-E711-8777-02163E011CFA.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/558/00000/D045DD67-AA5C-E711-92E9-02163E0146E8.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/595/00000/84CA2E49-DF5C-E711-A74D-02163E01180A.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/562/00000/7AD2402B-BB5C-E711-A439-02163E01A3D9.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/563/00000/380C2126-CA5C-E711-B467-02163E0139DD.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/586/00000/FE5C4376-D25C-E711-8F66-02163E01431B.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/577/00000/54C12E67-CD5C-E711-9999-02163E01A207.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/558/00000/E43891F2-9B5C-E711-A0FD-02163E019BC1.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/557/00000/5427530C-945C-E711-8CDA-02163E0144AC.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/557/00000/7E45A5C7-565D-E711-901D-02163E01A77C.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/560/00000/EEE0BCF3-AD5C-E711-939C-02163E0134F4.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/557/00000/5E322EA1-875C-E711-9962-02163E01A42A.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/587/00000/B4EF9AB1-D35C-E711-97DD-02163E011F7B.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/597/00000/AA87FF7C-DE5C-E711-8182-02163E0145F6.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/559/00000/C4EF2457-8F5C-E711-9D8A-02163E01462D.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/562/00000/546776E5-CF5C-E711-9950-02163E019CBC.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
