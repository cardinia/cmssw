import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/120/00000/1E981355-C5B4-E711-AAF6-02163E0121D7.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/115/00000/2465322C-C5B4-E711-9A3A-02163E019DE8.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/136/00000/C6365441-C5B4-E711-9E49-02163E014720.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/141/00000/9870FA3E-C5B4-E711-B71D-02163E014360.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/156/00000/74D2A893-C5B4-E711-9EF2-02163E019BF3.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/169/00000/3AC18BAB-C5B4-E711-ADB9-02163E011A67.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/177/00000/9AA885B5-C5B4-E711-A0FE-02163E0140E4.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/151/00000/743094AE-C5B4-E711-BC58-02163E019CA9.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/166/00000/DA9D0D9E-C5B4-E711-B734-02163E01A2E7.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/139/00000/2A0E9169-C5B4-E711-ACFF-02163E019CA4.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/163/00000/F0A15E9C-C5B4-E711-A286-02163E01A3EA.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/143/00000/E2AC8F6E-C5B4-E711-A898-02163E019DDD.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/113/00000/46F1F289-BCB4-E711-AEE3-02163E019BD6.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/114/00000/1419C47E-B0B4-E711-B802-02163E0137CD.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
