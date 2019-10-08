import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v3/RunGConfig/IOV_Align_306460.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/D0C0011F-2E22-E811-8A0E-0CC47A010854.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/D66BA3A6-F421-E811-9DE4-3C4A92F8FC32.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/A2F51E7F-0E22-E811-969F-38EAA78D8ACC.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/7263D2B4-1422-E811-BB0A-10604BA8FC24.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/9694F890-2122-E811-BFF3-1458D04923EC.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/5A492520-2E22-E811-8CC3-8CDCD4A99E08.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/504CC5AF-E721-E811-BF08-FA163E25AA37.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/686B689F-FA21-E811-A8D3-FA163E61E995.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/86EE0911-0A22-E811-9611-FA163E29E7C4.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/B255CFB6-1522-E811-B32B-FA163EE631F9.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/8A6EA1E1-B322-E811-BA67-FA163E40D682.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/440729E9-B322-E811-B5C3-FA163E7A8FA1.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/C422227D-0E22-E811-B377-3417EBE70663.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/782162C5-1422-E811-9D94-0CC47A7E6A4C.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/6C202059-1B22-E811-842C-0CC47A7E6820.root',
'/store/data/Run2017G/HLTPhysics/ALCARECO/TkAlMinBias-17Nov2017-v1/30000/F2D0DB7B-2E22-E811-A57D-002590DE6E30.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
