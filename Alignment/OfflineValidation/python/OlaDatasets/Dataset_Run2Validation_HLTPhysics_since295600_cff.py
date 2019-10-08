import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/603/00000/12FCED99-0747-E711-B6B9-02163E011F19.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/613/00000/48FBA029-2147-E711-AF11-02163E0142EE.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/610/00000/08B31F89-2F47-E711-887C-02163E0140D8.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/616/00000/D22A7F67-1E47-E711-9335-02163E01461A.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/606/00000/10E63E83-1247-E711-B9DF-02163E0137C0.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/613/00000/245B4C74-1747-E711-8B3F-02163E0136DA.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/613/00000/12345371-1A47-E711-914F-02163E01410A.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/613/00000/6A488C18-2847-E711-9841-02163E01474D.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/606/00000/24C4CDA3-2547-E711-8E7A-02163E011B0F.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/605/00000/129C5DF2-F946-E711-B2C5-02163E01A3B6.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/613/00000/94F0CF8A-3647-E711-ACB7-02163E013504.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/605/00000/F6CB0A1A-0247-E711-9AEF-02163E01385D.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/613/00000/7EDE6959-1E47-E711-97E9-02163E014461.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/605/00000/3C5AC8FF-FD46-E711-B4EF-02163E011E1D.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/605/00000/E0B61C09-F046-E711-AA43-02163E019E76.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/600/00000/ACB86E31-1647-E711-844E-02163E0141D1.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/605/00000/2CF0D905-0647-E711-A674-02163E013438.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/602/00000/603F40C5-0C47-E711-99BC-02163E01A1C1.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/606/00000/A4D81085-1747-E711-A261-02163E01350F.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/605/00000/344B37CB-F346-E711-9A85-02163E019E29.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/606/00000/F8FED83B-1E47-E711-8D85-02163E01451B.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/605/00000/C8C5177E-F746-E711-A7A7-02163E019DCE.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/603/00000/CECE1F54-F146-E711-AAF0-02163E014702.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/616/00000/0ECEF244-2547-E711-B4CA-02163E01440D.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/613/00000/DCC2F5FB-2F47-E711-82FC-02163E014198.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/616/00000/5ABFF1F4-9A58-E711-8F34-02163E011E07.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/610/00000/30FFA3A5-2447-E711-8AF1-02163E019E7A.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/603/00000/868BC949-F646-E711-A872-02163E011F69.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/608/00000/5C26FDD4-5247-E711-B6F4-02163E0138BB.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/608/00000/1606EBAB-2147-E711-BF90-02163E0121FC.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/605/00000/A0AF7825-F646-E711-B738-02163E01A31C.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/603/00000/86246C49-2E47-E711-A608-02163E01A1FE.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/605/00000/660F9934-FB46-E711-BE95-02163E01A6D0.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/604/00000/A61FF135-F246-E711-A50D-02163E013497.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/605/00000/C02BE841-F146-E711-9747-02163E01A1F7.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/605/00000/345D7CD9-1547-E711-AF9E-02163E014120.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/600/00000/120655E8-F246-E711-A1B1-02163E01A5E6.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
