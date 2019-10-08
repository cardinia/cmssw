import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/296/641/00000/6C6D58B4-E950-E711-BA0D-02163E012268.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/296/649/00000/C6070824-0851-E711-A7A4-02163E0141EA.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/296/662/00000/562888B4-9F52-E711-8106-02163E01225B.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/296/658/00000/D885319D-1151-E711-9A85-02163E01A4E0.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/296/646/00000/F4E47847-F550-E711-8E88-02163E014253.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/296/657/00000/DC5B28F7-0E51-E711-9E66-02163E013936.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/296/660/00000/C0553213-1551-E711-8C7E-02163E0143A4.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/296/656/00000/86E945ED-0E51-E711-9404-02163E013407.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/296/647/00000/C2AA9982-0A51-E711-8363-02163E01429F.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/296/655/00000/8297FBDB-0B51-E711-BD98-02163E01185D.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/296/651/00000/E45E6448-0851-E711-9268-02163E0146F2.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/296/652/00000/5CB7A5D8-0B51-E711-9C6D-02163E01392C.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/296/642/00000/5815D2E1-F950-E711-94B1-02163E0137D4.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
