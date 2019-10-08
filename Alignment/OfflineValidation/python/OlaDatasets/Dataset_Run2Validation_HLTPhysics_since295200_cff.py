import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/301/00000/3228FBF3-4145-E711-8FF9-02163E0140EB.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/255/00000/D2A89A93-3C45-E711-BF9C-02163E01A4B0.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/284/00000/F6443674-3745-E711-8773-02163E013518.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/204/00000/B86C27B4-3F45-E711-AE7E-02163E01A6E7.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/266/00000/7E4F4159-3745-E711-A38D-02163E014480.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/210/00000/0E9B84CE-4345-E711-A5AF-02163E01381D.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/253/00000/9A20C29B-3645-E711-A556-02163E01A5DB.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/257/00000/586A627E-3845-E711-9114-02163E01A364.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/307/00000/82E3242E-3C45-E711-BA3E-02163E01287D.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/290/00000/56CD6294-3945-E711-8467-02163E019C02.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/300/00000/882A0E1F-3D45-E711-96CE-02163E019D72.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/296/00000/1EB015FD-3645-E711-A0AE-02163E019DC2.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/203/00000/32510E1B-2A45-E711-871B-02163E01A5F3.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/231/00000/64648F36-3945-E711-839B-02163E01A1F1.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/261/00000/149BA2C3-3445-E711-AB0B-02163E011CC4.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/200/00000/F88166E3-3A45-E711-A886-02163E01382E.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/220/00000/3E3A8EF9-3F45-E711-AD0F-02163E0143E8.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/317/00000/9607FAA9-4E45-E711-A4B7-02163E01A270.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/209/00000/96CB09FC-5545-E711-B0EF-02163E01A43D.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/274/00000/1664ECE9-3A45-E711-9837-02163E01A70B.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/293/00000/44709F84-3A45-E711-A5D6-02163E0145BD.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/228/00000/46C3F8B8-3945-E711-9D04-02163E01A334.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/209/00000/0AECF403-3D45-E711-A149-02163E011819.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/285/00000/2A7B07CB-3645-E711-BEAD-02163E01A66A.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/272/00000/5AD7E050-3C45-E711-A86C-02163E01A234.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/292/00000/629161FE-3745-E711-898C-02163E014543.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/230/00000/52F3CF18-3545-E711-B577-02163E01A32E.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/263/00000/E8B4F53E-3745-E711-8B58-02163E01A5A3.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/271/00000/6C4129BA-3645-E711-9123-02163E0134B4.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/303/00000/2CF1A184-3D45-E711-8AA8-02163E01A430.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/259/00000/F8BBBC8C-3845-E711-B026-02163E01A4FC.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/201/00000/945B091D-2F45-E711-8F00-02163E019DE1.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/282/00000/42A3EF5E-3945-E711-8B9D-02163E019BA8.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/311/00000/BE36C348-3F45-E711-A263-02163E0146CB.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/275/00000/A813BDEE-3C45-E711-BDC3-02163E0145D3.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/211/00000/8CC38052-3B45-E711-8052-02163E0144FF.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/202/00000/52C4ED8A-2E45-E711-AD60-02163E011E0F.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/208/00000/F487D0DD-1F45-E711-974D-02163E01A26D.root',
'/store/data/Run2017A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/295/308/00000/6A65C444-3F45-E711-A0F5-02163E019B53.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
