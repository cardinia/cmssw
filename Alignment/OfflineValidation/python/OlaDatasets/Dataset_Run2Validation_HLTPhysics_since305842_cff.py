import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/842/00000/5C4A6660-8DC1-E711-97E5-02163E014248.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/897/00000/FC6B397F-01C2-E711-A755-02163E01A2F8.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/7418F73F-D6C2-E711-A98D-02163E019CA2.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/843/00000/149757A4-80C1-E711-B79A-02163E019C3A.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/856/00000/86A678DE-8AC1-E711-9015-02163E0142E3.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/90431A23-70C2-E711-837A-02163E011EE5.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/842/00000/825ED4AA-90C1-E711-9931-02163E011A98.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/A060BB4A-39C2-E711-8F62-02163E01A503.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/DCA05442-22C2-E711-9326-02163E01A2EA.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/CCE72ED2-12C2-E711-AC4F-02163E011E00.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/876/00000/98B90BB4-DEC1-E711-B9A9-02163E011ACE.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/CC7D25D1-27C2-E711-AC0C-02163E01A1E1.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/722D4635-57C2-E711-B268-02163E0145ED.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/849/00000/BCD671F5-8CC1-E711-93C5-02163E013594.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/851/00000/3C7D4282-8BC1-E711-A723-02163E01426A.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/E4E19A46-25C2-E711-A389-02163E0146BB.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/8C06C847-66C2-E711-855B-02163E013512.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/842/00000/C2DBBE01-C9C1-E711-9B2C-02163E01338F.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/845/00000/3248EEC0-8FC1-E711-B13E-02163E0136D4.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/891/00000/36498FA8-DEC1-E711-AFCD-02163E019CB6.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/847/00000/547498C9-89C1-E711-9A86-02163E01A5DA.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/E42EF719-EEC2-E711-97AE-02163E01A34A.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/842/00000/B8E5739B-93C1-E711-B403-02163E01392D.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/873/00000/92D43C8B-D5C1-E711-A887-02163E019C11.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/D8E0DF42-37C2-E711-B144-02163E01A6E5.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/A0BB12F7-11C2-E711-BB52-02163E014585.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/426F4775-18C2-E711-8E19-02163E01A310.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/EED5063B-2BC2-E711-AC4C-02163E01A456.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/895/00000/D0C0AABC-F2C1-E711-9594-02163E01A1D8.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/862/00000/24F057C6-D5C2-E711-A464-02163E01470D.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/894/00000/16B9D193-DEC1-E711-9B57-02163E01A441.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/868/00000/6A6DF0F2-D0C1-E711-ADB1-02163E01338E.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/896/00000/8C41F62D-F9C1-E711-9B5E-02163E019E43.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/875/00000/62675555-D6C1-E711-86C0-02163E01A3BF.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
