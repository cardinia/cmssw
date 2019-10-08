import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/514/00000/8852C720-7D7C-E711-8FE1-02163E0143F9.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/497/00000/4AAA8FF7-737C-E711-A7C5-02163E01A538.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/497/00000/96E3BA75-907C-E711-81BC-02163E01A273.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/514/00000/8EA3C7D8-9F7C-E711-83AF-02163E0144F9.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/498/00000/DE47AA4E-677C-E711-9C41-02163E0145B3.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/505/00000/A04E18CF-557C-E711-BDCE-02163E019D1A.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/507/00000/C63EBEEE-567C-E711-8D38-02163E01A4BE.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/499/00000/0AD2B883-547C-E711-A754-02163E0143DF.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/500/00000/D6F52DDA-577C-E711-8EE4-02163E012786.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/501/00000/188374A1-527C-E711-9B28-02163E01198E.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/506/00000/888874C4-557C-E711-A7FA-02163E0138DD.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
