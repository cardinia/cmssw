import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/201/00000/1C245F80-C577-E711-A927-02163E0146D3.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/155/00000/4E3511A4-B677-E711-AFDF-02163E01469A.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/157/00000/0C561286-C277-E711-9CBC-02163E0133FC.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/226/00000/70BA4392-F377-E711-8CD9-02163E014407.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/177/00000/98AF9EAB-C177-E711-ADE1-02163E01475C.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/166/00000/664CE3E8-C077-E711-8AFA-02163E01254C.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/222/00000/8447BED9-C277-E711-9EA7-02163E019D29.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/155/00000/96762BE5-C277-E711-B8C5-02163E013449.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/155/00000/C6E0ABF2-BD77-E711-B2CA-02163E0143DC.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/165/00000/5EDB6EC3-BF77-E711-AD0A-02163E0141E8.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/211/00000/B0E2B8F0-C677-E711-A2F4-02163E0144D2.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/226/00000/22CF075F-DD77-E711-A317-02163E0141F8.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/228/00000/32B4E587-D777-E711-B7DE-02163E012AEB.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/155/00000/CEA8A970-C777-E711-BD67-02163E0124B2.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/226/00000/86D7FAA0-E177-E711-915F-02163E01441A.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/155/00000/AE0FACA4-D177-E711-8854-02163E0137BB.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/226/00000/447C1FD1-D977-E711-A2AB-02163E01444D.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/221/00000/9823FB31-C577-E711-8B3D-02163E01A33D.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/156/00000/2A85ADFE-CF77-E711-B678-02163E014617.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/155/00000/3C1C86F7-C377-E711-A0F7-02163E013409.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/226/00000/543B2A87-EA77-E711-BB88-02163E014152.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/155/00000/7E557CD5-BF77-E711-B15A-02163E01A442.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/167/00000/04ED4FC0-C077-E711-ACA8-02163E01A7A7.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/182/00000/20C70483-C177-E711-91C1-02163E01475C.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/157/00000/DAE0144D-CD77-E711-982E-02163E019C55.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/157/00000/529D4251-BC77-E711-8D5C-02163E019DAA.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/155/00000/906E571C-B977-E711-BB42-02163E01A296.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/155/00000/4E8B992F-BB77-E711-95E6-02163E013945.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/206/00000/9E3E7FA4-C177-E711-AE9C-02163E0121D4.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/224/00000/426DB648-C377-E711-9451-02163E014251.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/231/00000/EE8C8638-DD77-E711-9D89-02163E01444A.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/155/00000/9CA3C806-D677-E711-9A77-02163E014239.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/157/00000/901701F0-C477-E711-B774-02163E0137D1.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
