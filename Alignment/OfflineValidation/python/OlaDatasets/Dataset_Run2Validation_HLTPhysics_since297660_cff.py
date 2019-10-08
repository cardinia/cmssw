import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/661/00000/7EDBA4B0-095E-E711-B5C5-02163E013442.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/660/00000/62E85D96-FC5D-E711-9B6B-02163E012281.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/660/00000/BA7B01D9-F85D-E711-8B99-02163E01476C.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/667/00000/0CFCA71C-235E-E711-9EF2-02163E013935.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/669/00000/308BF2E7-275E-E711-9E62-02163E011C40.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/662/00000/40337206-095E-E711-BBAE-02163E0128F8.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/660/00000/E620E1E0-0D5E-E711-A404-02163E01A29F.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/664/00000/5CC4E40F-125E-E711-9183-02163E01A5E2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/665/00000/360EBBAF-1D5E-E711-86FB-02163E01A4AA.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/663/00000/6AE8672A-0B5E-E711-B288-02163E011F08.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/666/00000/948D4488-335E-E711-BD0F-02163E019BA0.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/665/00000/104A5E19-195E-E711-8F2C-02163E0142DE.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/661/00000/4C9B0E05-045E-E711-9660-02163E01476C.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/668/00000/CAAFE861-2B5E-E711-9439-02163E0146AC.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
