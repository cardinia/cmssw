import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/434/00000/4ABD78B4-735A-E711-A2D5-02163E013501.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/429/00000/C6E92EBF-465A-E711-A6A2-02163E01A5ED.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/462/00000/5CC693FC-815A-E711-9E3E-02163E01A5AC.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/430/00000/82675471-585A-E711-B975-02163E01A252.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/446/00000/3832C57A-765A-E711-87D5-02163E011F99.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/437/00000/A03A8016-6E5A-E711-907D-02163E0146DC.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/436/00000/A6C433B5-685A-E711-96CE-02163E01A50C.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/452/00000/804BE87D-805A-E711-878C-02163E013676.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/433/00000/929CC981-6A5A-E711-884E-02163E019CC6.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/435/00000/282536EE-725A-E711-9DB9-02163E011F2C.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/464/00000/D4C72139-A75A-E711-B470-02163E0142C5.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/463/00000/969E28BA-815A-E711-898B-02163E014175.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/443/00000/C026CBA8-755A-E711-9FE6-02163E014408.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/433/00000/A4035892-665A-E711-BCA7-02163E011DD2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/430/00000/94936C0D-4D5A-E711-89DF-02163E01A269.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/432/00000/A232AC82-635A-E711-A532-02163E012A94.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/434/00000/28F82C13-705A-E711-BE71-02163E01A354.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/465/00000/0C48DE66-B45A-E711-9676-02163E01A3B8.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/431/00000/AE732845-695A-E711-8DDB-02163E019BF2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/432/00000/66CEB11A-5C5A-E711-BF87-02163E0119EE.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/431/00000/66D34F93-595A-E711-98C3-02163E01A295.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/439/00000/386242DE-6F5A-E711-915B-02163E012B0C.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
