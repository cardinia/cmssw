import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/297/004/00000/C01C9C8B-2056-E711-B898-02163E0144CA.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/297/006/00000/78673223-1D56-E711-AA27-02163E013817.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/297/007/00000/22A5D8B0-4756-E711-8F5F-02163E019D9C.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/297/010/00000/8665C4B3-2A56-E711-A70C-02163E01183E.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/297/009/00000/5A2163D1-1A56-E711-9C97-02163E01432D.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/297/011/00000/CE124A8A-1F56-E711-9222-02163E01A472.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
