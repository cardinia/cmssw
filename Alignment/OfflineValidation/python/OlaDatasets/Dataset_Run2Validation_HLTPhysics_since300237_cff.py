import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/237/00000/005850A3-2F78-E711-A18E-02163E01A1F8.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/247/00000/C202441E-5E78-E711-A8B3-02163E019E14.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/263/00000/B2F23914-9C78-E711-9614-02163E01A5DC.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/268/00000/FC26D9CD-B578-E711-85BA-02163E011EB0.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/276/00000/8A0F9BE5-C978-E711-BBED-02163E01A3E1.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/260/00000/4CA9263C-6978-E711-9ED8-02163E0142B7.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/257/00000/6E69AC90-6178-E711-A8C2-02163E01191D.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/244/00000/50DB8800-5378-E711-875A-02163E0141D9.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/237/00000/5CAF945C-4278-E711-8793-02163E01443A.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/255/00000/4A1EF66E-5D78-E711-AC86-02163E01A1D3.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/246/00000/5888D4C0-5578-E711-8065-02163E01237F.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/264/00000/B277D0E6-9E78-E711-A743-02163E011C13.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/237/00000/30E3DE5F-3878-E711-8EF1-02163E011E1A.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/241/00000/7874A8C5-4D78-E711-B3E3-02163E01A292.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/266/00000/CE8213DD-B178-E711-9669-02163E01A5D3.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/278/00000/1408D378-D678-E711-AF5A-02163E01A5CE.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/238/00000/721833D0-4278-E711-8F97-02163E01190B.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/271/00000/08D61953-C178-E711-B845-02163E019E77.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/238/00000/9CE1B384-4C78-E711-B163-02163E0122B9.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/240/00000/5238E30C-6078-E711-99BA-02163E0144E9.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/240/00000/D208F1B9-6378-E711-97D8-02163E0141F6.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/273/00000/7846261C-C078-E711-A282-02163E019BA1.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/237/00000/12FF6787-3478-E711-9FF2-02163E014607.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/259/00000/BAFF741F-6478-E711-B5BD-02163E0121D4.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/237/00000/A42937BE-3A78-E711-88CE-02163E019DAF.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/237/00000/866F0331-3D78-E711-BBC4-02163E01A2CC.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/262/00000/4A31EFD2-7E78-E711-80F6-02163E0121CB.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/261/00000/6CBBBD78-7778-E711-99DD-02163E014580.root',
'/store/data/Run2017C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/300/256/00000/842D2F2C-5F78-E711-9BDF-02163E014772.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
