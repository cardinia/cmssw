import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/296/968/00000/160A84B9-B355-E711-BA64-02163E014189.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/296/982/00000/C2FF2AFB-F655-E711-8518-02163E0122BF.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/296/977/00000/2658DF18-FA55-E711-80CB-02163E019B25.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/296/969/00000/7A0A9CF6-D655-E711-8E5F-02163E01437B.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/297/003/00000/DEDEDCD1-0956-E711-9559-02163E013642.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/296/967/00000/C43BDECC-BB55-E711-BEB0-02163E014234.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/296/976/00000/A08E9B3A-EE55-E711-B877-02163E011806.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/296/972/00000/AE1D73E3-DF55-E711-88B1-02163E019CDA.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/296/978/00000/E0349FBD-0856-E711-BC92-02163E011AA4.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/296/970/00000/985DEEBA-D655-E711-A4A9-02163E01273C.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/296/971/00000/F03C2B20-CB55-E711-A206-02163E01A39F.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/296/966/00000/C857014A-B055-E711-937B-02163E0142DE.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/296/977/00000/C69CD38F-EB55-E711-84A4-02163E019CCE.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/296/985/00000/88C27528-F155-E711-91A5-02163E014459.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
