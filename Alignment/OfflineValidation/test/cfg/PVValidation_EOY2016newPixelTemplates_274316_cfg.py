import FWCore.ParameterSet.Config as cms
import sys
 
isDA = True
isMC = False
allFromGT = False
applyBows = True
applyExtraConditions = True

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
readFiles.extend(['/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/6AFC781F-6709-E911-ACBB-0242AC130002.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/4CFEDC47-CE09-E911-9A63-0CC47AFC3C80.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/F6BDA01A-6509-E911-A3C1-001E67A4069F.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/34F9D660-6509-E911-BEE8-008CFAC91A64.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/705145B7-0B0A-E911-AED5-008CFA582C5C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/02A144E6-6509-E911-9F7D-E0071B6C9DB0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/0C07DBCC-8709-E911-9C00-24BE05C626B1.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/2634AD61-6609-E911-80E7-EC0D9A8221D6.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/FE1A710B-6C09-E911-8E06-0CC47A6C1864.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/62C2703B-AE09-E911-BA0D-008CFAC93BF0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/1296918E-6609-E911-A66F-0025901D08E4.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/5E655CBC-6609-E911-9345-E0071B7B2380.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/F6CC260C-6609-E911-A727-24BE05BDCEF1.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/3C2E1355-6609-E911-A404-E0071B73B6D0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/824FE688-6609-E911-8C5F-0CC47A6C06C2.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/62D08587-6709-E911-8CE3-24BE05CE5D21.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/5AAD9076-6609-E911-A334-0CC47AA989C0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/42AC245E-6809-E911-9307-0242AC130002.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/6A564332-6709-E911-AFF1-0242AC130002.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/7A69B0A9-F009-E911-A208-D4856459C3E0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/16E5201F-CB09-E911-B757-008CFAC94180.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/FA984C50-6809-E911-92D2-0CC47AD990C4.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/3CDAAC74-9709-E911-B38C-E0071B749C40.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/2C630E5D-6609-E911-BA85-EC0D9A82237E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/86BCFB57-6609-E911-863B-5065F381A2F1.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/E0830500-6609-E911-B692-E0071B6C9DB0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/6A0D8C83-6609-E911-B9CC-24BE05C648A1.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/8455F980-6709-E911-B751-0242AC130002.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/34DA2058-6609-E911-B988-008CFAC91D04.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/44FB0259-6609-E911-915E-008CFAC94058.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/DABB115D-6609-E911-A5B8-008CFAC91CAC.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/4A9C4270-B309-E911-9E48-141877637B68.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/14759EAB-C909-E911-BF23-246E96D10990.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/C87C8463-6609-E911-A9D9-E0071B73B6F0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/246D6F87-320A-E911-9853-246E96D14C50.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/C88FE4E5-6609-E911-99DA-AC1F6BB17832.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/BC8C1C59-6609-E911-A86D-008CFAE45060.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/A49CECBD-6609-E911-89CA-002590821320.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/F41ED219-5809-E911-8B93-5065F38162B1.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/9271B85D-C909-E911-9B6A-B083FED07198.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/CC56AE1E-6709-E911-B62B-002590D9DA9C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/741A3EC7-6809-E911-9BFC-0025901AC404.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/6E70D983-6609-E911-88C3-008CFA11139C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/D66F7051-030A-E911-9372-0CC47AD9901E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/22A5F862-6609-E911-B63F-E0071B73C600.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/CCD3C7A3-6409-E911-B300-24BE05CEEC21.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/DEC9E5BA-6809-E911-A33F-506B4BB16026.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/7AAEA284-6609-E911-BEB0-EC0D9A8221EE.root'])
process.source = cms.Source("PoolSource",
                            fileNames = readFiles ,
                            duplicateCheckMode = cms.untracked.string('checkAllFilesOpened')
                            )

#process.load("Alignment.OfflineValidation.DATASETTEMPLATE");
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

runboundary = 274316
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
 
          process.conditionsInSiPixelTemplateDBObjectRcd= CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone( 
               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'), 
               toGet = cms.VPSet(cms.PSet(record = cms.string('SiPixelTemplateDBObjectRcd'), 
                                          tag = cms.string('SiPixelTemplateDBObject_38T_v16_offline'), 
                                           ) 
                                 ) 
               ) 
          process.prefer_conditionsInSiPixelTemplateDBObjectRcd = cms.ESPrefer("PoolDBESSource", "conditionsInSiPixelTemplateDBObjectRcd") 
 
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
                                   fileName=cms.string("PVValidation_EOY2016newPixelTemplates_274316.root")
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
                                           intLumi = cms.untracked.double(127.368727122),
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
