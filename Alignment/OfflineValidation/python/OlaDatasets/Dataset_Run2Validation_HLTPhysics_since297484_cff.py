import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/488/00000/ECF4B7AE-965B-E711-AFC3-02163E019D99.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/485/00000/0E73E8DB-485B-E711-B91E-02163E014741.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/491/00000/FAA968EF-9B5B-E711-AFD6-02163E01A39D.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/486/00000/3A1E62F8-625B-E711-B5A8-02163E0119F4.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/484/00000/5A617739-275B-E711-BB20-02163E0139CE.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/486/00000/EC816275-665B-E711-A102-02163E01A39B.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/484/00000/66705C4D-2C5B-E711-98BF-02163E014459.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/486/00000/4875D60B-7B5B-E711-84FE-02163E012019.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/487/00000/728DD585-9C5B-E711-AFB3-02163E01A5E2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/484/00000/5EB06B18-3D5B-E711-80CB-02163E019C17.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/487/00000/22F798A0-815B-E711-B349-02163E01A1B7.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/486/00000/D2A2D5A5-6B5B-E711-A935-02163E0140DA.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/486/00000/C602D672-685B-E711-84B0-02163E01A672.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/485/00000/00B464D4-465B-E711-96A0-02163E01386F.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/485/00000/6CD4A1B1-595B-E711-B169-02163E011B6B.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/493/00000/6E1DCB03-A25B-E711-AC3D-02163E01383A.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/490/00000/ACE44AD4-8D5B-E711-A5E0-02163E014338.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/488/00000/42D3928A-B55B-E711-A507-02163E019BC1.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/487/00000/EEFA3550-A15B-E711-935A-02163E0134D8.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/485/00000/0482ADB5-725B-E711-A77A-02163E019C17.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/492/00000/A8A86E17-995B-E711-BA82-02163E019BC1.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/487/00000/4AD6809D-865B-E711-BA38-02163E019C5B.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
