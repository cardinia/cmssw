import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/184/00000/02924048-1F6C-E711-9F90-02163E01432C.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/184/00000/9ABDD053-0B6C-E711-BAFA-02163E014567.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/214/00000/04AD2B50-696C-E711-84FE-02163E01A409.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/222/00000/1215C752-736C-E711-AC4C-02163E01285E.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/223/00000/EA204F8B-7E6C-E711-B2ED-02163E014767.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/189/00000/C87CAE34-326C-E711-915B-02163E012339.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/227/00000/509350F1-936C-E711-AA31-02163E01419D.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/195/00000/92528D81-526C-E711-A6AF-02163E01A2B1.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/226/00000/32003761-806C-E711-8469-02163E0135FC.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/188/00000/EC713FCE-F36B-E711-A95D-02163E019C23.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/185/00000/D4D50A7A-036C-E711-8366-02163E019C4D.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/187/00000/02B6A415-F26B-E711-A6B5-02163E011A0F.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/184/00000/0CAD16B3-136C-E711-8CB7-02163E01A5C2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/207/00000/C4E1868B-6A6C-E711-82E5-02163E0128AB.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/218/00000/68C21129-6D6C-E711-A7F7-02163E01A5AC.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/198/00000/66A0699E-5F6C-E711-AAB4-02163E011E1A.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/184/00000/FE1249E4-FD6B-E711-8E94-02163E01A604.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/184/00000/9CEFF202-016C-E711-BA4A-02163E01A3EF.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
