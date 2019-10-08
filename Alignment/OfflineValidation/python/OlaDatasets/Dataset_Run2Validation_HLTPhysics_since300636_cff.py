import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/638/00000/8E46BFE5-DD7D-E711-8C13-02163E01A665.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/643/00000/A89E0D52-D97D-E711-9960-02163E014210.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/636/00000/F885A65E-D47D-E711-A765-02163E01391F.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/636/00000/367B09AE-E97D-E711-A141-02163E01341D.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/636/00000/72B37658-D67D-E711-AEF1-02163E01A4AD.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/645/00000/5A8A0089-DA7D-E711-A2F9-02163E013431.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/636/00000/D010D1DF-D97D-E711-B7C7-02163E014761.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/636/00000/E2494F11-F37D-E711-95E3-02163E011DBD.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/665/00000/883CDA5E-E67D-E711-ADE2-02163E01A674.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/654/00000/D0796564-DA7D-E711-BE65-02163E01451D.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/636/00000/986BB5BB-DD7D-E711-BA6D-02163E019CC9.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/661/00000/A0A59E9B-E17D-E711-83E5-02163E01A407.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
