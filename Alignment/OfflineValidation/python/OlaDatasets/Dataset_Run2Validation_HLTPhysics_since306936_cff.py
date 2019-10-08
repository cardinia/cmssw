import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/080/00000/B2B70B8E-FDD3-E711-A6F7-02163E019B65.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/081/00000/FA15A183-FED3-E711-ADB1-02163E019E85.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/007/00000/E0BD9EF6-5CD1-E711-9A72-02163E011F7B.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/064/00000/5A446218-1BD3-E711-AE7D-02163E01A790.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/022/00000/C094E654-FFD1-E711-B568-02163E011EE2.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/037/00000/6CF28A79-0ED2-E711-8DA4-02163E01A552.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/049/00000/CE68B00D-7CD2-E711-AB87-02163E01A1B8.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/047/00000/768AE586-6DD2-E711-9881-02163E01A38E.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/016/00000/BC333A6A-DDD1-E711-B8F6-02163E019C3A.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/005/00000/6C144091-52D1-E711-A57E-02163E011DDC.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/013/00000/267F3580-62D1-E711-95B7-02163E019DA1.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/051/00000/20312FB2-ACD2-E711-B578-02163E019B1E.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/053/00000/524AC9BD-ACD2-E711-BC1B-02163E01471F.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/072/00000/D66524EF-2AD3-E711-9E1B-02163E011C08.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/079/00000/2C8DD8C6-FDD3-E711-A123-02163E01A211.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/065/00000/CCFBBB64-23D3-E711-8157-02163E01195D.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/050/00000/8C96D500-82D2-E711-AB87-02163E01A2F4.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/075/00000/E66D2C05-7CD3-E711-93FA-02163E01377D.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/024/00000/88C94EA1-07D2-E711-A699-02163E01A20C.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/042/00000/00291F96-3DD2-E711-9B34-02163E0138EE.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/063/00000/142EACAF-1DD3-E711-952C-02163E019B6E.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/052/00000/56A0B471-A9D2-E711-BC7C-02163E014675.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/038/00000/E04B86CC-10D2-E711-97EB-02163E019D0E.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/078/00000/7697F891-FAD3-E711-B01F-02163E014450.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/048/00000/103C9A32-7BD2-E711-8371-02163E01A452.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/070/00000/B0C65E42-2BD3-E711-8E27-02163E014162.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/014/00000/52ECADD9-C9D1-E711-B74F-02163E014162.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/003/00000/5A5E6649-4BD1-E711-8AF5-02163E019C8F.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/032/00000/7653C607-07D2-E711-9906-02163E01A20C.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/035/00000/1E379AC5-0CD2-E711-AD6D-02163E01A56F.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/001/00000/4AEF0F51-4BD1-E711-97DF-02163E019D82.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/017/00000/6E24C6B9-FAD1-E711-AACC-02163E0145EA.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/055/00000/1C047040-F0D2-E711-A5EE-02163E0144AA.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/062/00000/8CE813AE-1BD3-E711-8ADE-02163E01A340.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/076/00000/CAB004EF-F6D3-E711-9D33-02163E01A229.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/044/00000/9E3B157D-3CD2-E711-8043-02163E0136BC.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/045/00000/E8DD1B46-3FD2-E711-9C81-02163E01A478.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/015/00000/9674E5DF-CED1-E711-A3AE-02163E013642.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/073/00000/C2669279-63D3-E711-B13E-02163E011932.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/040/00000/600C93DE-15D2-E711-A229-02163E01A3B5.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/046/00000/DC685424-45D2-E711-BC47-02163E01A748.root',
'/store/data/Run2017H/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/307/004/00000/9CD9596B-4BD1-E711-B9C0-02163E011870.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
