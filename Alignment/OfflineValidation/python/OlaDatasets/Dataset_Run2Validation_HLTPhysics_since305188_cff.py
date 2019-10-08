import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/7A59CD51-FFB5-E711-9E0D-02163E019B9D.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/190/00000/6C82FF27-78B5-E711-A055-02163E01A268.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/C8E28A6A-3DB6-E711-B947-02163E019C1A.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/191/00000/9486AC96-7BB5-E711-A591-02163E01A79F.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/188/00000/48C90A68-6EB5-E711-968A-02163E014382.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/199/00000/60EFBFDD-7DB5-E711-852A-02163E019DA3.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/188/00000/3AFA3117-61B5-E711-805C-02163E01A5E6.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/194/00000/9A4930AD-7CB5-E711-BF9F-02163E01A476.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/DA81618B-EAB5-E711-818E-02163E01423F.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/188/00000/3EBC4B2C-67B5-E711-B852-02163E019E20.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/4C80A565-01B6-E711-BF3D-02163E0139A4.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/B430434D-E1B5-E711-B83E-02163E014668.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/198/00000/744F5D22-7DB5-E711-A5F9-02163E0133F9.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/188/00000/D6F9FD1F-64B5-E711-BC5D-02163E0118DA.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/D2EF46C0-CEB5-E711-BDB0-02163E01A5BE.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/197/00000/DEFAF97A-7CB5-E711-82D8-02163E019E58.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/188/00000/54517FDD-72B5-E711-9282-02163E019D66.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/192/00000/B6BAA33A-7BB5-E711-B4B5-02163E01272B.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/188/00000/0412F1B8-5FB5-E711-A123-02163E01A408.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/BA654210-FDB5-E711-A262-02163E013650.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/188/00000/FE4E82EB-64B5-E711-A4B7-02163E013390.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/203/00000/DEE5F2A3-00B6-E711-87CD-02163E013793.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/702BB054-C0B5-E711-8949-02163E0135A2.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/188/00000/E01247A7-93B5-E711-A6C0-02163E0141B9.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/188/00000/3A4E7531-78B5-E711-BB32-02163E019C5A.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/18E376C9-60B6-E711-8CE7-02163E01381C.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/B05D3457-EFB5-E711-BBE9-02163E01A715.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/42EFD0A6-C6B5-E711-9AA8-02163E013720.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/1E7FD3CD-C2B5-E711-8F60-02163E01A219.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/A4A65848-CAB5-E711-96C6-02163E01459C.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/723C7429-BFB5-E711-A627-02163E019B47.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/188/00000/08BAA0CF-6AB5-E711-96BB-02163E011D2C.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/365BA415-DEB5-E711-A8C3-02163E01A39D.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/202/00000/A0F50F3D-BFB5-E711-9E56-02163E019BD7.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/188/00000/182387AB-70B5-E711-92BD-02163E011C94.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
