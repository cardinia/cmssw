import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/457/00000/E65168E8-3846-E711-A1F1-02163E013935.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/458/00000/C6D70A5D-2046-E711-971C-02163E0122C7.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/459/00000/C2E8F312-2446-E711-AE6B-02163E019CC0.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
