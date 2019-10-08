import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/293/00000/98CE9354-4979-E711-9B42-02163E019C35.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/284/00000/50DC3D21-4479-E711-B9CE-02163E0118CB.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/313/00000/DAB9B8D7-6479-E711-95CA-02163E01442B.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/317/00000/D23EFF5E-6F79-E711-8A1E-02163E013744.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/361/00000/8C0C9183-8E7B-E711-BBC0-02163E019CC7.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/280/00000/866229A3-1579-E711-9AF9-02163E01A441.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/312/00000/72162B79-6179-E711-A7D7-02163E011878.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/328/00000/FE9D9E49-AF79-E711-9632-02163E013811.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/322/00000/6E148BEB-A379-E711-B967-02163E011A42.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/342/00000/707AC1D3-BD79-E711-BC67-02163E01445C.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/314/00000/303BDC08-6679-E711-A4D8-02163E011C14.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/280/00000/22D4C2DE-F17D-E711-9848-02163E01A5E0.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/284/00000/FC65D7A1-3F79-E711-BCF0-02163E019BCD.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/282/00000/7CB7D4B7-4B79-E711-B128-02163E0145F6.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/323/00000/E2DFD8A0-A779-E711-8030-02163E019E22.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/344/00000/2CD467B2-BE79-E711-B4B3-02163E01A4CA.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/284/00000/2CDE61CA-4D79-E711-A8BF-02163E019D9B.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/280/00000/8433C1D5-1279-E711-9842-02163E0133C2.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/280/00000/F86473FF-2279-E711-A007-02163E01A4F0.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/282/00000/6023F62B-3979-E711-AFD6-02163E01A250.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/360/00000/60432C6B-8D7B-E711-8F0E-02163E01A534.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/310/00000/E4CCFEA5-5B79-E711-9F55-02163E011A36.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/280/00000/E449BED1-1179-E711-A47E-02163E0124EA.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/284/00000/18048493-4179-E711-9265-02163E01A4C9.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/357/00000/E4CAF29A-C979-E711-958B-02163E01A6D1.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/325/00000/E40AB88C-AF79-E711-8158-02163E013841.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/333/00000/F8ECAA95-B379-E711-95F9-02163E011DF9.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/348/00000/FA57B5D2-C779-E711-ABD7-02163E0141DB.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/280/00000/70BE40D0-1279-E711-AA8C-02163E012410.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/339/00000/EEE6C31F-BC79-E711-AE11-02163E01A4C2.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/349/00000/E8BFB387-C379-E711-B131-02163E019E87.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
