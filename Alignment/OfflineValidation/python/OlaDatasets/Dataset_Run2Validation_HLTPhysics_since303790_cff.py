import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017E/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/303/824/00000/BC38894D-4DA3-E711-8E26-02163E019CA7.root',
'/store/data/Run2017E/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/303/824/00000/A29CB484-2DA3-E711-912B-02163E01A592.root',
'/store/data/Run2017E/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/303/814/00000/98300626-43A2-E711-92D2-02163E014711.root',
'/store/data/Run2017E/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/303/806/00000/D0CC102D-3FA2-E711-8E86-02163E019D50.root',
'/store/data/Run2017E/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/303/815/00000/EE910DE5-47A2-E711-B609-02163E0143D3.root',
'/store/data/Run2017E/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/303/819/00000/9203D61C-69A2-E711-B1BB-02163E01444E.root',
'/store/data/Run2017E/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/303/820/00000/18EBAA37-F7A2-E711-9C86-02163E011ADA.root',
'/store/data/Run2017E/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/303/817/00000/C021348E-84A2-E711-9B25-02163E01A6ED.root',
'/store/data/Run2017E/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/303/824/00000/A41C8E75-45A3-E711-859B-02163E0143A3.root',
'/store/data/Run2017E/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/303/813/00000/0E7DC172-41A2-E711-AF9F-02163E01A678.root',
'/store/data/Run2017E/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/303/824/00000/7488DF7E-22A3-E711-94FF-02163E0142CC.root',
'/store/data/Run2017E/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/303/817/00000/56E5A39D-A1A2-E711-9945-02163E019BB4.root',
'/store/data/Run2017E/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/303/816/00000/2475B496-49A2-E711-B69B-02163E019CAD.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
