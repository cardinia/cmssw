import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/344/00000/5E1B87EB-6C45-E711-AE22-02163E01A64B.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/342/00000/E229DFE5-7345-E711-ABC9-02163E01A671.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/345/00000/B2D8C6DB-7145-E711-976D-02163E01A726.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/347/00000/44F765E8-FB45-E711-A4AD-02163E01180D.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/346/00000/EA99B1A1-6345-E711-9BF6-02163E01A62D.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/341/00000/1AEA8809-7245-E711-A9FF-02163E01426F.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
