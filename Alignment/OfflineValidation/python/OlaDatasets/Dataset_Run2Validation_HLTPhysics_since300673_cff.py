import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/679/00000/243669DA-E17D-E711-94A2-02163E019E58.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/769/00000/54D66481-3C7E-E711-9F0E-02163E01A5E7.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/744/00000/F487667A-0E7E-E711-98E8-02163E01A1E4.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/772/00000/1E79D925-437E-E711-9F99-02163E0143F0.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/777/00000/6E5AA8B7-D37E-E711-93F5-02163E019E53.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/675/00000/340AE671-EE7D-E711-9A3D-02163E014210.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/676/00000/969D3B06-FB7D-E711-BE91-02163E01A5D4.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/775/00000/14D5755A-577E-E711-8F40-02163E01420B.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/702/00000/14BA8802-E57D-E711-8AED-02163E011CDB.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/771/00000/26F5B9BC-387E-E711-871A-02163E01A36A.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/683/00000/B61193D7-E37D-E711-AA62-02163E019B60.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/735/00000/08A89FF9-E07D-E711-A798-02163E01A2C0.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/740/00000/C09D7876-F17D-E711-98EB-02163E01A3C2.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/777/00000/DE688354-EC7E-E711-9CDF-02163E01A3BE.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/745/00000/9CCE75BB-157E-E711-B441-02163E01430D.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/773/00000/98D3ABBB-4C7E-E711-A9FA-02163E01347B.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/777/00000/32E4ACBD-D57E-E711-80B3-02163E014217.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/749/00000/D8560AE3-217E-E711-A23C-02163E011CDB.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/673/00000/621F8A30-F87D-E711-861F-02163E019B84.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/742/00000/3AE33CA8-BC84-E711-B817-02163E013913.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/768/00000/F40BF870-2F7E-E711-9D52-02163E0137E7.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/742/00000/26C54FAE-BC84-E711-9101-02163E01A6AE.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/678/00000/0095A100-E47D-E711-A62A-02163E01A5F0.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/730/00000/2CEBDD0F-DF7D-E711-9DD7-02163E014410.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/742/00000/66B0D7AC-7F7E-E711-960F-02163E01A541.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/725/00000/2A6C14EA-E07D-E711-AB76-02163E01A5DC.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/736/00000/EEB3C4AB-EA7D-E711-B1DA-02163E01A48C.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/721/00000/7A088353-DB7D-E711-AC9A-02163E019D88.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/761/00000/E6F5F8B0-3F7E-E711-97F8-02163E0144F9.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/300/777/00000/203AC48C-EC7E-E711-BB1C-02163E012A42.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
