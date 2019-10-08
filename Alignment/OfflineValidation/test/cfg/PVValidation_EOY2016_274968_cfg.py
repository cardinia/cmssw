import FWCore.ParameterSet.Config as cms
import sys
 
isDA = True
isMC = False
allFromGT = True
applyBows = True
applyExtraConditions = False

process = cms.Process("PrimaryVertexValidation") 

###################################################################
def customiseAlignmentAndAPE(process):
###################################################################
    if not hasattr(process.GlobalTag,'toGet'):
        process.GlobalTag.toGet=cms.VPSet()
    process.GlobalTag.toGet.extend( cms.VPSet(cms.PSet(record = cms.string("TrackerAlignmentRcd"),
                                                       tag = cms.string("TrackerAlignment_v19_offline"),
                                                       connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                                                       ),
                                              cms.PSet(record = cms.string("TrackerAlignmentErrorExtendedRcd"),
                                                       tag = cms.string("TrackerAlignmentExtendedErrors_v6_offline_IOVs"),
                                                       connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                                                       )
                                              )
                                    )
    return process

###################################################################
def customiseKinksAndBows(process):
###################################################################
     if not hasattr(process.GlobalTag,'toGet'):
          process.GlobalTag.toGet=cms.VPSet()
     process.GlobalTag.toGet.extend(cms.VPSet(cms.PSet(record = cms.string("TrackerSurfaceDeformationRcd"),
                                                       tag = cms.string("TrackerSurfaceDeformations_v9_offline"),
                                                       connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                                                       ),        
                                              )
                                    )
     return process

###################################################################
# Event source and run selection
###################################################################
readFiles = cms.untracked.vstring()
readFiles.extend(['/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/46208861-CF09-E911-BEE7-0025907277CE.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/00000/6CA6226A-F908-E911-8153-141877642F9D.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/7C06426E-6509-E911-8F4A-E0071B7A48A0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/BC7CD5D4-6409-E911-BA1B-EC0D9A822606.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/D2F76F53-6509-E911-B438-24BE05CEEC21.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/64873F41-CC09-E911-BADE-0CC47A6C06C6.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/E20640C0-4F09-E911-9DEA-0CC47AA53D68.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/C860B42D-E60A-E911-9C98-B083FED07198.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/BA536E34-E60A-E911-B03D-0CC47AFC3C64.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/CA4C1A1A-6609-E911-A3B7-B083FED138B3.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/08A6649C-6609-E911-9B16-00259073E520.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/60B75A05-4E09-E911-B3E0-246E96D14D9C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/565AB370-C809-E911-878E-246E96D14AB0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/0ECCD306-E309-E911-8E5F-901B0E542974.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/00000/B6275939-F608-E911-9D5C-B083FED03632.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/00000/6EAB4367-1A09-E911-80AF-B083FECFC6ED.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/6AE8841A-5109-E911-9F6D-5065F38122A1.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/74BE3792-6409-E911-84EC-24BE05BDBE21.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/2C15B2FD-6509-E911-91A0-24BE05CE1E01.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/70FC79D4-6409-E911-A3AA-24BE05CECB51.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/7AC0DA44-6609-E911-8AFC-24BE05C616E1.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/E060D57B-6509-E911-80FD-0025901D08BF.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/06680628-6509-E911-A5A1-14187763663C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/A6BB4A71-6609-E911-9C67-246E96D14E34.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/A071F85F-CE09-E911-A16B-0CC47AFC3D32.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/00000/781526EA-F008-E911-A40F-0025905B85CC.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/E8B9AD82-6109-E911-B98D-5065F3816201.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/38B20ABB-4C09-E911-9F85-24BE05C62711.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/0E37238A-B409-E911-A88A-EC0D9A82264E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/00000/BA55BB7E-1C09-E911-86A0-0CC47A4C8E98.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/00000/42A543F4-1E09-E911-9D70-003048FFD76C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/6224122C-C909-E911-AFA0-44A84223FF3C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/00000/FE496040-C309-E911-B7AC-44A84223FF3C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/66844BC5-6509-E911-AEE4-E0071B7AC770.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/9AA220DF-5109-E911-B566-24BE05C666B1.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/0A87FA00-6609-E911-8901-EC0D9A822626.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/D892EE0C-5009-E911-94D4-0CC47A13D09C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/D68BD769-8B09-E911-8F37-0CC47AA53D66.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/ECA292C6-5009-E911-A918-AC1F6BB177EC.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/EEE232B5-D909-E911-9EB7-0CC47A0AD4A4.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/2E6926FA-A610-E911-85D1-0CC47A4C8E5E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/00000/C8311144-4409-E911-A5CB-0025905B85D2.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/00000/8E2C5E32-1B09-E911-8517-0025905A607A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/C2BB70E4-5109-E911-A992-008CFA1112BC.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/58E8DF70-4D09-E911-AF07-0CC47AA98A32.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/86F2717E-6609-E911-A2B1-0CC47AD24D28.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/00000/DC2B26BD-EE08-E911-9817-0025905A60B2.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/00000/1E1294CD-1F09-E911-83BF-0025905A60BE.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/769AB45C-5309-E911-9670-008CFA1113B0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/422580E3-260A-E911-81A8-44A84225C629.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/5A887D95-5209-E911-9352-EC0D9A822626.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/1C09B0F3-6509-E911-A2FF-24BE05CECB71.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/6420B83F-6709-E911-87D8-0CC47AD98C8C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/58FD2D27-6609-E911-BADA-90B11C2CC76A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/BC9C7248-6609-E911-8FB9-002590D9D8BA.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/00000/98846639-F008-E911-9429-0CC47A4D75EE.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/6E1C27B9-6409-E911-8F1A-246E96D10CC4.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/F8989809-3C0A-E911-8F73-246E96D14B5C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/00000/76A56AA3-F608-E911-9394-14187764311A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/00000/EA31033D-F608-E911-AC4F-246E96D14B5C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/94F12F11-5409-E911-8D62-0CC47AD98B8E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/E6FF2B30-4C09-E911-BD3A-0CC47AA53D5A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/B8D5FE6B-4F09-E911-B559-008CFA197480.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/CAFC4D54-6B09-E911-8D84-008CFA1978F0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/30F074CF-4C09-E911-AF29-008CFA1113B0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/7299BD30-6709-E911-9E78-246E96D14C70.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/C0111E6B-CE09-E911-A4B8-246E96D14B5C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/BCD010B5-F80A-E911-AAC9-90B11C2CC96F.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/A046DDBF-5009-E911-944F-24BE05C488E1.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/94314BC0-5309-E911-8A45-EC0D9A8222DE.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/20000/E24CAD1D-5309-E911-8739-0CC47A6C138A.root'])
process.source = cms.Source("PoolSource",
                            fileNames = readFiles ,
                            duplicateCheckMode = cms.untracked.string('checkAllFilesOpened')
                            )

#process.load("Alignment.OfflineValidation.DATASETTEMPLATE");
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

runboundary = 274968
process.source.firstRun = cms.untracked.uint32(int(runboundary))
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(50000) )

###################################################################
# JSON Filtering
###################################################################
if isMC:
     print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: This is Simulation!"
     runboundary = 1
else:
     print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: This is DATA!"
     import FWCore.PythonUtilities.LumiList as LumiList
     process.source.lumisToProcess = LumiList.LumiList(filename ='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt').getVLuminosityBlockRange()

###################################################################
# Messages
###################################################################
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

####################################################################
# Produce the Transient Track Record in the event
####################################################################
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

####################################################################
# Get the Magnetic Field
####################################################################
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

###################################################################
# Standard loads
###################################################################
process.load("Configuration.Geometry.GeometryRecoDB_cff")

####################################################################
# Get the BeamSpot
####################################################################
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")

####################################################################
# Get the GlogalTag
####################################################################
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_2016LegacyRepro_v4', '')

if allFromGT:
     print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: All is taken from GT"
else:
     ####################################################################
     # Get Alignment constants and APE
     ####################################################################
     process=customiseAlignmentAndAPE(process)

     ####################################################################
     # Kinks and Bows (optional)
     ####################################################################
     if applyBows:
          print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: Applying TrackerSurfaceDeformations!"
          process=customiseKinksAndBows(process)
     else:
          print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: MultiPVValidation: Not applying TrackerSurfaceDeformations!"

     ####################################################################
     # Extra corrections not included in the GT
     ####################################################################
     if applyExtraConditions:

          import CalibTracker.Configuration.Common.PoolDBESSource_cfi
          ##### END OF EXTRA CONDITIONS
 
     else:
          print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: Not applying extra calibration constants!"
     
####################################################################
# Load and Configure event selection
####################################################################
process.primaryVertexFilter = cms.EDFilter("VertexSelector",
                                             src = cms.InputTag("offlinePrimaryVertices"),
                                             cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
                                             filter = cms.bool(True)
                                             )

process.noscraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  src =  cms.untracked.InputTag("ALCARECOTkAlMinBias"),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
                                  )

process.load("Alignment.CommonAlignment.filterOutLowPt_cfi")
process.filterOutLowPt.applyfilter = True
process.filterOutLowPt.src = "ALCARECOTkAlMinBias"
process.filterOutLowPt.numtrack = 0
process.filterOutLowPt.thresh = 1
process.filterOutLowPt.ptmin  = 0.5
process.filterOutLowPt.runControl = True
process.filterOutLowPt.runControlNumber = [runboundary]

if isMC:
     process.goodvertexSkim = cms.Sequence(process.noscraping+process.filterOutLowPt)
else:
     process.goodvertexSkim = cms.Sequence(process.primaryVertexFilter + process.noscraping + process.filterOutLowPt)

####################################################################
# Load and Configure Measurement Tracker Event
# (this would be needed in case NavigationSchool is set != from ''
####################################################################
# process.load("RecoTracker.MeasurementDet.MeasurementTrackerEventProducer_cfi") 
# process.MeasurementTrackerEvent.pixelClusterProducer = 'ALCARECOTkAlMinBias'
# process.MeasurementTrackerEvent.stripClusterProducer = 'ALCARECOTkAlMinBias'
# process.MeasurementTrackerEvent.inactivePixelDetectorLabels = cms.VInputTag()
# process.MeasurementTrackerEvent.inactiveStripDetectorLabels = cms.VInputTag()

####################################################################
# Load and Configure TrackRefitter
####################################################################
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
import RecoTracker.TrackProducer.TrackRefitters_cff
process.FinalTrackRefitter = RecoTracker.TrackProducer.TrackRefitter_cfi.TrackRefitter.clone()
process.FinalTrackRefitter.src = "ALCARECOTkAlMinBias"
process.FinalTrackRefitter.TrajectoryInEvent = True
process.FinalTrackRefitter.NavigationSchool = ''
process.FinalTrackRefitter.TTRHBuilder = "WithAngleAndTemplate"

####################################################################
# Load and Configure common selection sequence
####################################################################
# import Alignment.CommonAlignment.tools.trackselectionRefitting as trackselRefit
# process.seqTrackselRefit = trackselRefit.getSequence(process,'ALCARECOTkAlMinBias')
# process.HighPurityTrackSelector.trackQualities = cms.vstring()
# process.HighPurityTrackSelector.pMin     = cms.double(0.)
# process.TrackerTrackHitFilter.usePixelQualityFlag = cms.bool(False)
# #process.TrackerTrackHitFilter.commands   = cms.vstring("drop PXB 1")
# process.AlignmentTrackSelector.pMin      = cms.double(0.)
# process.AlignmentTrackSelector.ptMin     = cms.double(0.)
# process.AlignmentTrackSelector.nHitMin2D = cms.uint32(0)
# process.AlignmentTrackSelector.nHitMin   = cms.double(0.)
# process.AlignmentTrackSelector.d0Min     = cms.double(-999999.0)
# process.AlignmentTrackSelector.d0Max     = cms.double(+999999.0)                  
# process.AlignmentTrackSelector.dzMin     = cms.double(-999999.0)
# process.AlignmentTrackSelector.dzMax     = cms.double(+999999.0)  

####################################################################
# Output file
####################################################################
process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("PVValidation_EOY2016_274968.root")
                                  )                                    

####################################################################
# Deterministic annealing clustering
####################################################################
if isDA:
     print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: Running DA Algorithm!"
     process.PVValidation = cms.EDAnalyzer("PrimaryVertexValidation",
                                           TrackCollectionTag = cms.InputTag("FinalTrackRefitter"),
                                           VertexCollectionTag = cms.InputTag("offlinePrimaryVertices"),  
                                           Debug = cms.bool(False),
                                           storeNtuple = cms.bool(False),
                                           useTracksFromRecoVtx = cms.bool(False),
                                           isLightNtuple = cms.bool(True),
                                           askFirstLayerHit = cms.bool(False),
                                           probePt  = cms.untracked.double(0.5),
                                           probeEta = cms.untracked.double(2.7),
                                           runControl = cms.untracked.bool(True),
                                           intLumi = cms.untracked.double(181.431363784),
                                           runControlNumber = cms.untracked.vuint32(int(runboundary)),
                                           
                                           TkFilterParameters = cms.PSet(algorithm=cms.string('filter'),                           
                                                                         maxNormalizedChi2 = cms.double(5.0),                        # chi2ndof < 5                  
                                                                         minPixelLayersWithHits = cms.int32(2),                      # PX hits > 2                       
                                                                         minSiliconLayersWithHits = cms.int32(5),                    # TK hits > 5  
                                                                         maxD0Significance = cms.double(5.0),                        # fake cut (requiring 1 PXB hit)     
                                                                         minPt = cms.double(0.0),                                    # better for softish events                        
                                                                         maxEta = cms.double(5.0),                                   # as per recommendation in PR #18330
                                                                         trackQuality = cms.string("any")
                                                                         ),
                                           
                                           ## MM 04.05.2017 (use settings as in: https://github.com/cms-sw/cmssw/pull/18330)
                                           TkClusParameters=cms.PSet(algorithm=cms.string('DA_vect'),
                                                                     TkDAClusParameters = cms.PSet(coolingFactor = cms.double(0.6),  # moderate annealing speed
                                                                                                   Tmin = cms.double(2.0),           # end of vertex splitting
                                                                                                   Tpurge = cms.double(2.0),         # cleaning 
                                                                                                   Tstop = cms.double(0.5),          # end of annealing
                                                                                                   vertexSize = cms.double(0.006),   # added in quadrature to track-z resolutions
                                                                                                   d0CutOff = cms.double(3.),        # downweight high IP tracks
                                                                                                   dzCutOff = cms.double(3.),        # outlier rejection after freeze-out (T<Tmin)   
                                                                                                   zmerge = cms.double(1e-2),        # merge intermediat clusters separated by less than zmerge
                                                                                                   uniquetrkweight = cms.double(0.8) # require at least two tracks with this weight at T=Tpurge                                                                    
                                                                                                   )
                                                                     )
                                           )

####################################################################
# GAP clustering
####################################################################
else:
     print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: Running GAP Algorithm!"
     process.PVValidation = cms.EDAnalyzer("PrimaryVertexValidation",
                                           TrackCollectionTag = cms.InputTag("FinalTrackRefitter"),
                                           VertexCollectionTag = cms.InputTag("offlinePrimaryVertices"), 
                                           Debug = cms.bool(False),
                                           isLightNtuple = cms.bool(True),
                                           storeNtuple = cms.bool(False),
                                           useTracksFromRecoVtx = cms.bool(False),
                                           askFirstLayerHit = cms.bool(False),
                                           probePt = cms.untracked.double(0.5),
                                           probeEta = cms.untracked.double(2.7),
                                           runControl = cms.untracked.bool(True),
                                           runControlNumber = cms.untracked.vuint32(int(runboundary)),
                                           
                                           TkFilterParameters = cms.PSet(algorithm=cms.string('filter'),                             
                                                                         maxNormalizedChi2 = cms.double(5.0),                        # chi2ndof < 20                  
                                                                         minPixelLayersWithHits=cms.int32(2),                        # PX hits > 2                   
                                                                         minSiliconLayersWithHits = cms.int32(5),                    # TK hits > 5                   
                                                                         maxD0Significance = cms.double(5.0),                        # fake cut (requiring 1 PXB hit)
                                                                         minPt = cms.double(0.0),                                    # better for softish events     
                                                                         maxEta = cms.double(5.0),                                   # as per recommendation in PR #18330
                                                                         trackQuality = cms.string("any")
                                                                         ),
                                        
                                           TkClusParameters = cms.PSet(algorithm   = cms.string('gap'),
                                                                       TkGapClusParameters = cms.PSet(zSeparation = cms.double(0.2)  # 0.2 cm max separation betw. clusters
                                                                                                      ) 
                                                                       )
                                           )

####################################################################
# Path
####################################################################
process.p = cms.Path(process.goodvertexSkim*
                     # in case the common refitting sequence is removed
                     process.offlineBeamSpot*
                     #process.seqTrackselRefit*
                     # in case the navigation shool is removed
                     #process.MeasurementTrackerEvent*
                     # in case the common refitting sequence is removed
                     process.FinalTrackRefitter*
                     process.PVValidation)
