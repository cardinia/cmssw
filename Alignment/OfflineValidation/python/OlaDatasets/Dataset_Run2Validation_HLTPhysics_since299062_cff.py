import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/067/00000/D4389D56-FB6A-E711-883B-02163E0143B5.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/062/00000/00A0823A-C76A-E711-BE73-02163E019D47.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/062/00000/363C51EA-C16A-E711-8BCD-02163E011E00.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/065/00000/FA30E10C-DE6A-E711-B550-02163E0134D1.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/073/00000/6077435C-EE6A-E711-BCC9-02163E0142F6.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/064/00000/9000DE80-E96A-E711-855C-02163E01A6B4.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/062/00000/32615400-CE6A-E711-A75C-02163E01A5D4.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/084/00000/E6D9849C-016B-E711-897C-02163E011BFE.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/065/00000/9CC4B1EF-EA6A-E711-8EA6-02163E0123FD.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/067/00000/DA572070-F86A-E711-B44E-02163E01A3D6.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/067/00000/5E65DC7F-FF6A-E711-88A7-02163E0135A0.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/081/00000/F275BA52-FF6A-E711-BAF1-02163E011A09.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/072/00000/76317397-EA6A-E711-8D85-02163E01A1CE.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/076/00000/A8BF750A-F16A-E711-BDA8-02163E011B75.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
