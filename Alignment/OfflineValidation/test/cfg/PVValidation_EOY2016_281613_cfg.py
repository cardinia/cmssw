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
readFiles.extend(['/store/data/Run2016H/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018-v1/20000/E0E8881E-F211-E911-9663-0CC47A4C8E34.root','/store/data/Run2016H/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018-v1/20000/B2E7C156-CE11-E911-92BC-0CC47A78A4B0.root','/store/data/Run2016H/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018-v1/20000/02DE429E-F111-E911-8CB6-0CC47A7C351E.root','/store/data/Run2016H/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018-v1/20000/146450A3-F111-E911-BF4A-0CC47A4C8E46.root','/store/data/Run2016H/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018-v1/20000/98AD39A1-F111-E911-8613-0CC47A4D7698.root'])
process.source = cms.Source("PoolSource",
                            fileNames = readFiles ,
                            duplicateCheckMode = cms.untracked.string('checkAllFilesOpened')
                            )

#process.load("Alignment.OfflineValidation.DATASETTEMPLATE");
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

runboundary = 281613
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
                                   fileName=cms.string("PVValidation_EOY2016_281613.root")
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
                                           intLumi = cms.untracked.double(9.557943606),
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
