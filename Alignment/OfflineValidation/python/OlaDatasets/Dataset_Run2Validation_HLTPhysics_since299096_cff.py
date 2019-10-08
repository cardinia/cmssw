import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/149/00000/ECF7944B-9B6B-E711-9459-02163E01A422.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/170/00000/D61A1B38-AD6B-E711-9902-02163E01A4FC.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/147/00000/CC98226D-5C6B-E711-8DF1-02163E011E55.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/164/00000/76313BD3-AE6B-E711-8099-02163E019DE0.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/154/00000/34D9BBDE-8F6B-E711-911B-02163E014184.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/183/00000/723C256B-DA6B-E711-ABFE-02163E011A36.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/156/00000/887A8E05-976B-E711-9E2F-02163E01A4F2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/180/00000/742BBF6D-E86B-E711-912B-02163E01A3B8.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/152/00000/C459F1EB-876B-E711-B555-02163E0133E7.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/155/00000/340880A9-906B-E711-BB46-02163E014252.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/178/00000/C8880067-E86B-E711-B811-02163E012645.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/149/00000/D64979BD-906B-E711-9902-02163E019E4B.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/171/00000/60F1B360-AE6B-E711-9978-02163E01A212.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/101/00000/E808371B-276B-E711-83EE-02163E0144F2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/146/00000/523C4E7B-536B-E711-9583-02163E0133A4.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/149/00000/F264FBB2-BE6B-E711-AF3F-02163E0135A0.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/149/00000/B09CE816-AF6B-E711-8593-02163E013740.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/161/00000/3EAFE691-9F6B-E711-8982-02163E01A587.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/158/00000/9C4F815F-9D6B-E711-8320-02163E019BBE.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/096/00000/40F035D6-1E6B-E711-9DDC-02163E019CBC.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
