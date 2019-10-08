import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/298/996/00000/7EA23899-196A-E711-8E8E-02163E013960.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/061/00000/447961B4-5F6B-E711-9537-02163E01A638.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/060/00000/BE26639A-8D6A-E711-BF63-02163E01A6B2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/056/00000/423A4A47-766A-E711-9146-02163E0135FC.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/020/00000/DAB2ADAB-2F6A-E711-AFB7-02163E0143B5.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/051/00000/22FCA894-6E6A-E711-83D7-02163E01A616.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/008/00000/C2B519A4-176A-E711-B817-02163E013390.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/028/00000/80C6D958-3D6A-E711-9A52-02163E01A3A5.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/027/00000/561876E5-3C6A-E711-A8C4-02163E01A5E2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/012/00000/FAF70FDD-186A-E711-AEF1-02163E01A505.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/025/00000/D6C2C428-3A6A-E711-8DA3-02163E019C43.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/019/00000/D8A85EDA-2E6A-E711-B194-02163E0139BB.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/298/996/00000/9C9D6F70-1F6A-E711-9011-02163E01263F.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/031/00000/E86AA099-4B6B-E711-A891-02163E011A09.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/298/998/00000/8292E155-0B6A-E711-B842-02163E01A250.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/038/00000/9207EA33-5E6A-E711-BE00-02163E013811.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/013/00000/2A6D63A9-2B6A-E711-B052-02163E011911.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/039/00000/006901E6-606A-E711-B62E-02163E01A3C0.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/054/00000/C8079E1B-736A-E711-932A-02163E0135EF.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/026/00000/CC266BD6-3B6A-E711-A6C7-02163E01A6B4.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/000/00000/16B4DCEF-246A-E711-AD47-02163E013390.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/061/00000/DEACD49A-BB6A-E711-B7C8-02163E011B61.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/011/00000/4679A0AC-186A-E711-BBA9-02163E01A6F7.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/005/00000/E0D8B768-146A-E711-A6A8-02163E0119BC.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/042/00000/706115A1-746A-E711-B21E-02163E01A582.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/298/997/00000/1AE2A098-1C6A-E711-98C6-02163E011DD8.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/002/00000/8E281677-136A-E711-90A4-02163E019BD7.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/040/00000/E43FB830-636A-E711-86E3-02163E013816.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/061/00000/109BC179-B66A-E711-8246-02163E0143DE.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/299/030/00000/DCB10FA8-436A-E711-B230-02163E01189B.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
