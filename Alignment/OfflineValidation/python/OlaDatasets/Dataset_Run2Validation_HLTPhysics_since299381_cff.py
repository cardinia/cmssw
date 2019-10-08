import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/400/00000/52B17B37-016E-E711-BC81-02163E01A5B9.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/396/00000/0283536B-2D6E-E711-A0A7-02163E019D80.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/404/00000/E01A7D2E-026E-E711-ACCD-02163E01A43C.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/440/00000/EEC87BAB-7C70-E711-847C-02163E0139CE.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/383/00000/2A003798-E16D-E711-9DF0-02163E014607.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/395/00000/AA64937D-156E-E711-BE23-02163E01A2C3.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/387/00000/4E469C83-E06D-E711-9E98-02163E011A4D.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/394/00000/9CBDA6EB-FD6D-E711-BCFB-02163E014265.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/388/00000/A817C313-EA6D-E711-9F49-02163E01A7A5.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/381/00000/FE34A2AD-EE6D-E711-A53C-02163E01A1FE.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/436/00000/FE8034FB-7E70-E711-94B6-02163E0136A3.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/420/00000/48CD36E4-2C6E-E711-9977-02163E011A23.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/419/00000/88A53DF7-0E6E-E711-817D-02163E011F1B.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
