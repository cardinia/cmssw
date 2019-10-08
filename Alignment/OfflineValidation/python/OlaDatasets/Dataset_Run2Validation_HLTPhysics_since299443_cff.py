import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/448/00000/D863F3CA-8370-E711-9A9F-02163E01A529.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/475/00000/58263313-8770-E711-8D42-02163E012090.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/446/00000/809D87EB-8370-E711-9C13-02163E011DAE.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/479/00000/2614C455-B170-E711-B6BB-02163E019D1D.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/472/00000/2E4EE526-8270-E711-B304-02163E011D9A.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/443/00000/CE8A1C6E-A470-E711-B8B8-02163E01A73F.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/451/00000/EE2AE9E8-8370-E711-BAF4-02163E011F1B.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/458/00000/A00B5DEF-8070-E711-B5AD-02163E0134AE.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/478/00000/885E6C71-A570-E711-AE4D-02163E013542.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/450/00000/CC6081AF-AC70-E711-8AB6-02163E01411B.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/299/443/00000/083686C0-3971-E711-B247-02163E011F02.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
