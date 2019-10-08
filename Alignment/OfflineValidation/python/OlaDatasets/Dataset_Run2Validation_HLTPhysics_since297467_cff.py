import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/467/00000/B4D582A0-C85A-E711-A094-02163E01A46C.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/483/00000/AE6CF552-215B-E711-B4E3-02163E019DE0.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/469/00000/92264098-E45A-E711-A2C3-02163E019CCC.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/479/00000/52E803BF-EB5A-E711-BB52-02163E0138FA.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/475/00000/7039C63D-DC5A-E711-94CF-02163E0145D1.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/483/00000/5668D2EE-635B-E711-B41D-02163E019CC3.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/474/00000/6C19EDDE-195B-E711-A759-02163E01A3B2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/471/00000/98854CA1-C95A-E711-9DF5-02163E0141A5.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/482/00000/0CEEF735-FD5A-E711-BC39-02163E01A236.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/478/00000/780A93C4-EB5A-E711-A0A2-02163E01A4FB.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/468/00000/3A9DED02-D15A-E711-8D04-02163E01A3B2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/481/00000/58D43E51-F55A-E711-9957-02163E013936.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/480/00000/AE3340B1-ED5A-E711-85D3-02163E019C9A.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/473/00000/DACAF9EB-DB5A-E711-BD7A-02163E01A450.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/476/00000/625E299D-E45A-E711-B879-02163E01191C.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
