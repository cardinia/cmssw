import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/457/00000/28120D6D-FA7B-E711-B181-02163E013748.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/414/00000/D6694B85-F87B-E711-8438-02163E01A4CA.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/450/00000/426D4BD4-F87B-E711-918F-02163E01A586.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/407/00000/04C3D0FC-FB7B-E711-B417-02163E0144DD.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/403/00000/2E64A2B9-387C-E711-AB25-02163E0134D6.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/451/00000/9AB8CD5C-FF7B-E711-872B-02163E019BBF.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/400/00000/F06D648C-007C-E711-AF5A-02163E019BCD.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/447/00000/FA5C428B-F87B-E711-A28B-02163E011ECA.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/412/00000/3E3B9F44-F77B-E711-92F0-02163E011904.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/405/00000/76A3A42B-FC7B-E711-AAF0-02163E01A523.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/401/00000/9437099B-167C-E711-A3D9-02163E0126F2.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/424/00000/326012B7-F87B-E711-87C7-02163E011CF5.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/406/00000/466F4208-F57B-E711-AF5E-02163E019CB4.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/400/00000/F4913BCF-F07B-E711-A314-02163E01A5C6.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/401/00000/524C6367-047C-E711-8F2D-02163E01A3EB.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/399/00000/16326AA2-CD7B-E711-B083-02163E01A5E0.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/401/00000/507BF955-207C-E711-98A7-02163E014210.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/404/00000/5A833E2B-FE7B-E711-A1FE-02163E013599.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/413/00000/2A57E7E5-F67B-E711-B187-02163E011F8F.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/410/00000/3237DB96-F67B-E711-8127-02163E019D9F.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/409/00000/2E6069AB-F77B-E711-92C4-02163E019CB4.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/400/00000/B2D1832F-EB7B-E711-8176-02163E019D1B.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/400/00000/C0844812-0F7C-E711-A35E-02163E011AA4.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/446/00000/82356270-FC7B-E711-803E-02163E0145F5.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/455/00000/24E2EF6A-F87B-E711-83FC-02163E0143D6.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/400/00000/502EA21B-F57B-E711-A311-02163E01A64D.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
