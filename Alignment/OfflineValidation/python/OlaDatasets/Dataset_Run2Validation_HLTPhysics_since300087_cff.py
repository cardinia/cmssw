import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/120/00000/B4277617-1877-E711-95B7-02163E012957.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/106/00000/9208F631-3C77-E711-8799-02163E013809.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/122/00000/520D991E-4277-E711-BEC6-02163E011F68.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/126/00000/8490B1E2-6E77-E711-A5CC-02163E0137CF.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/122/00000/AA71A59C-4B77-E711-93D6-02163E0133A4.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/123/00000/8E41B6D7-6977-E711-A850-02163E014194.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/151/00000/FEC16919-7077-E711-9CA3-02163E014172.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/111/00000/2ED88E78-1477-E711-8647-02163E0144F7.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/133/00000/0CA61400-7477-E711-B38C-02163E0133A4.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/087/00000/B4A416C5-1077-E711-9FEA-02163E0142AB.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/107/00000/2EE8834B-5077-E711-8504-02163E013683.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/105/00000/38E9F99D-1377-E711-8E6F-02163E01A725.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/122/00000/BCBF4158-4D77-E711-B32A-02163E019CC8.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/124/00000/A0ACDED1-7E77-E711-AABD-02163E0122AD.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/132/00000/B8DFE663-7177-E711-9839-02163E0118BB.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/115/00000/3440C28A-1A77-E711-81F8-02163E01A4BA.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/114/00000/628C72E6-1B77-E711-8281-02163E0122E0.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/123/00000/38D9B563-6577-E711-9AF7-02163E019C89.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/117/00000/9E2ED80E-4177-E711-85AF-02163E019E74.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/129/00000/DE44E7B8-7277-E711-8B1F-02163E019B6A.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/122/00000/3AE50688-5077-E711-8744-02163E0144FB.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/119/00000/0298908C-1A77-E711-A41D-02163E019E8D.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/123/00000/AAA8805E-7277-E711-BB53-02163E019CBC.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/124/00000/7EA7DACD-7177-E711-97B7-02163E01A5A7.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/122/00000/F0793F11-5D77-E711-BFA4-02163E019DF0.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/122/00000/2C6A01D3-3E77-E711-B71C-02163E0145BB.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/112/00000/0AE0FF98-1777-E711-A7F7-02163E019BCC.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/140/00000/362C3A21-7377-E711-9768-02163E0143EC.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/122/00000/CA52542A-4577-E711-B612-02163E019E6B.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/093/00000/1E75A0C0-0F77-E711-AB5B-02163E011815.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/113/00000/78B46FB5-1677-E711-961B-02163E0144E0.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/088/00000/76069F72-1177-E711-BAB1-02163E013864.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/122/00000/D477FFA5-4E77-E711-B838-02163E01412A.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/102/00000/02B1B65A-1277-E711-8681-02163E0129BB.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/087/00000/66F9F25D-1777-E711-A8AE-02163E01A65F.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/104/00000/DEB481E1-1277-E711-9DC0-02163E01A4AC.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/092/00000/9A841E1F-1177-E711-9FF7-02163E019E71.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/153/00000/9C995D01-7477-E711-AC86-02163E01A442.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/122/00000/ACA544DE-5777-E711-8661-02163E01A3AC.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/147/00000/F26F35D3-7077-E711-927C-02163E011E00.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/121/00000/EE80BBAE-2077-E711-85C6-02163E01188F.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/118/00000/0EE4E6EF-1777-E711-8442-02163E01A3EB.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/127/00000/4245390C-7377-E711-BF9A-02163E014720.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/122/00000/66FF01E1-4277-E711-9B46-02163E012BA6.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/094/00000/CC69DF2D-1177-E711-AC1F-02163E0144EA.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/122/00000/AA6BB8FC-4777-E711-ADC7-02163E01A2C3.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/101/00000/A07F0FA1-1077-E711-9972-02163E01A1DD.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
