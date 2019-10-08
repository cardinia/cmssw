import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/608/00000/1E3E880D-635D-E711-A02E-02163E01A4B2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/614/00000/F0C8178F-775D-E711-BE43-02163E011BB7.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/609/00000/D2CE2F23-615D-E711-AA09-02163E01356F.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/613/00000/2A8188C6-6E5D-E711-91A7-02163E0119EE.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/605/00000/E6BF9B2F-4D5D-E711-A8C8-02163E01A5E2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/612/00000/22352495-625D-E711-BFD7-02163E019BC4.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/604/00000/E60D0D5E-1A61-E711-A388-02163E011B0F.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/604/00000/DA62B5C0-3D5D-E711-AEBD-02163E01425B.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/603/00000/F44460F5-3E5D-E711-8B5F-02163E019CBF.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/599/00000/06D888B4-1B5D-E711-95FE-02163E01A505.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/606/00000/C0C6C6C3-615D-E711-96AF-02163E01A54A.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/599/00000/C4725FBB-0D5D-E711-981A-02163E019BB8.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/605/00000/D810FDFD-1761-E711-9E40-02163E0133E6.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/599/00000/66A1A90E-185D-E711-AA78-02163E01A28D.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/603/00000/96116E21-235D-E711-9149-02163E01189E.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/603/00000/868878CF-305D-E711-A2DB-02163E0140D5.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/604/00000/5CDEBAC8-465D-E711-83E8-02163E01A4A6.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/606/00000/50E1BE9F-655D-E711-BB94-02163E013406.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/603/00000/B6B072D2-355D-E711-9588-02163E01190F.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/618/00000/DE4D6A03-7F5D-E711-9D0A-02163E0128F8.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/617/00000/42B5E0D2-7C5D-E711-AEA0-02163E011810.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/599/00000/3A47A283-125D-E711-A01F-02163E0128F8.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/599/00000/FEB46C83-3E5D-E711-986A-02163E0133B4.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/598/00000/9883CD62-E65C-E711-942F-02163E012307.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/610/00000/4638AEAD-615D-E711-8E14-02163E01361F.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/605/00000/A054E453-555D-E711-BF8E-02163E0144B1.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/603/00000/0E319026-285D-E711-AD85-02163E01A5B7.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
