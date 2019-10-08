import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/381/00000/08A9BB50-CD45-E711-81AA-02163E01A489.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/435/00000/EC1E0ED9-ED45-E711-B91B-02163E01A68C.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/429/00000/96FA074F-EE45-E711-9D81-02163E019BE1.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/393/00000/9AEC14B7-F645-E711-93A6-02163E014745.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/381/00000/2817DCA8-C145-E711-B1B7-02163E011A47.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/390/00000/0026BFDF-CA45-E711-B736-02163E011C45.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/392/00000/26E58DB1-F945-E711-9D53-02163E019DE1.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/394/00000/36648F74-E245-E711-A19A-02163E019B4B.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/434/00000/D474E956-F245-E711-AB84-02163E014570.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/427/00000/8294701C-EC45-E711-97B8-02163E01A1F8.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/390/00000/B47561B0-D645-E711-85DB-02163E011C71.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/389/00000/70C8CE5D-BC45-E711-8C4D-02163E014647.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/390/00000/E06FA5B0-D045-E711-93FE-02163E01A33E.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/433/00000/FCEE01E8-F145-E711-BB30-02163E01185E.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/381/00000/2A4E6AB4-C145-E711-9FC2-02163E011F24.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/420/00000/EA18D9CB-F145-E711-B5F4-02163E014188.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/391/00000/4C3378ED-E645-E711-8DED-02163E01A2E3.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/391/00000/38B6CF66-DE45-E711-B5A9-02163E01A2C2.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/397/00000/D2EE29B6-EE45-E711-8164-02163E01A591.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/381/00000/78902667-C745-E711-BE18-02163E019CB1.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/390/00000/28DE5E2D-DF45-E711-83A4-02163E01A586.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/390/00000/1ECFFBA3-EE45-E711-88E5-02163E019E64.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/390/00000/BEAEB31F-C845-E711-81AB-02163E01A795.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/404/00000/CCC3F6C1-EC45-E711-8B93-02163E01A407.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/395/00000/D84EFFD0-FC45-E711-AD64-02163E019BDA.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/395/00000/5A8567CE-F745-E711-B4FA-02163E014294.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/395/00000/1AA8D257-0C46-E711-92A0-02163E01A3A7.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
