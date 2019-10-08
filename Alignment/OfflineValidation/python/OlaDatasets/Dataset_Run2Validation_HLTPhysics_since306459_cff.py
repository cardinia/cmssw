import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/459/00000/FA0DCD71-ACC8-E711-88EE-FA163EC87CE2.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/459/00000/34CE2D76-ACC8-E711-BEDF-FA163E9EE39B.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/459/00000/8604D983-ACC8-E711-B61B-FA163EEFD829.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/459/00000/482D1076-ACC8-E711-904D-FA163E6A987E.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/459/00000/CAF54B77-ACC8-E711-BE77-FA163E166E6E.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/459/00000/B6CF1682-ACC8-E711-8F5F-02163E014B19.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/459/00000/10C2F79A-ACC8-E711-911C-02163E013169.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/459/00000/DC670F94-ACC8-E711-9B5B-02163E017658.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/459/00000/58DA6973-ACC8-E711-AC41-FA163EFEBB03.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/306/459/00000/CC9DC981-ACC8-E711-800C-FA163E93E987.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
