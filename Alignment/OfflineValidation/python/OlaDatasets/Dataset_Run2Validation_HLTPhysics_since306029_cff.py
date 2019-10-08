import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/030/00000/C042142D-4BC3-E711-A125-02163E01375A.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/038/00000/3038E37D-9DC3-E711-ACB2-02163E013858.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/029/00000/46180130-EBC3-E711-991F-02163E01A502.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/036/00000/889798A5-13C3-E711-B0D3-02163E01390C.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/034/00000/DEE4169D-13C3-E711-9D92-02163E0142BD.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/041/00000/605F0964-B7C3-E711-A26C-02163E0142C5.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/041/00000/A495E7EF-B9C3-E711-B228-02163E013524.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/041/00000/A256289A-83C3-E711-BB13-02163E01A5B8.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/038/00000/78F4E9B7-D5C3-E711-8991-02163E01361C.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/041/00000/E46F76DF-7BC3-E711-B6C4-02163E019E82.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/041/00000/70A1E6BB-76C3-E711-B6EC-02163E011A0C.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/038/00000/3A679CDF-5DC3-E711-B34F-02163E013942.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/031/00000/24DA2E8C-0DC3-E711-851B-02163E0144DE.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/030/00000/28B61DCB-4FC3-E711-9958-02163E019D02.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/038/00000/8472C1F4-5AC3-E711-B45F-02163E0134A3.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/032/00000/6229EC5C-10C3-E711-BDCE-02163E01A65B.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/030/00000/886581E1-5CC3-E711-8382-02163E01A5B6.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/041/00000/AC6D8F10-07C4-E711-90DC-02163E0141F8.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/037/00000/B8C68DD9-49C3-E711-A9EA-02163E01A385.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/041/00000/C4FC378E-8FC3-E711-834B-02163E012846.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/041/00000/BE4A8C1F-93C4-E711-B666-02163E01A44D.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
