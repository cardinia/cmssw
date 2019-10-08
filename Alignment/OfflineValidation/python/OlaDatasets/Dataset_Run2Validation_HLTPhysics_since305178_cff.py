import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/181/00000/DAA972E0-C6B4-E711-A38A-02163E019BA4.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/183/00000/BA99C0C1-4EB5-E711-BF0F-02163E01A204.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/183/00000/C2A0A45E-41B5-E711-8046-02163E01456D.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/186/00000/ECA9EA5B-5CB5-E711-A9FC-02163E01A34B.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/178/00000/BA8DEDD6-F0B4-E711-A254-02163E01A4EE.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/186/00000/10CA1A6D-18B5-E711-B35D-02163E01A79A.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/183/00000/548BB66D-2BB5-E711-A7E2-02163E0129F7.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/185/00000/02D426E2-C8B4-E711-B625-02163E01A6F0.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/180/00000/284F93A9-C6B4-E711-B077-02163E0143C3.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/178/00000/B60E3948-DFB4-E711-8D19-02163E011E15.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/183/00000/061CB23E-49B5-E711-8375-02163E011E2E.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/182/00000/B81855D9-C6B4-E711-9F09-02163E014708.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/183/00000/309BF556-08B5-E711-8FB3-02163E01A5D3.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/186/00000/5AA762AE-26B5-E711-A8F5-02163E01468C.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/186/00000/98071052-1EB5-E711-A45E-02163E01A76D.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/179/00000/B473BBF6-E1B4-E711-8F2F-02163E01465E.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/183/00000/F6EF4AFC-EDB4-E711-9D27-02163E0135FD.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/183/00000/8E8FD964-FBB4-E711-B52B-02163E01A4C5.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/187/00000/9EE448FA-09B5-E711-8CE4-02163E01192C.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/186/00000/A203EA61-6FB5-E711-9949-02163E011881.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/186/00000/78D0DD42-34B5-E711-AB3E-02163E014295.root',
'/store/data/Run2017F/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/305/184/00000/CA55F727-C8B4-E711-BF65-02163E01A3AE.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
