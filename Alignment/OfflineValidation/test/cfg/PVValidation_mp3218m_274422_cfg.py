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
                                                       tag = cms.string("Alignments"),
                                                       connect = cms.string("sqlite_file:/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/mp3218/jobData/jobm/alignments_MP.db")
                                                       ),
                                              cms.PSet(record = cms.string("TrackerAlignmentErrorExtendedRcd"),
                                                       tag = cms.string("APEs"),
                                                       connect = cms.string("sqlite_file:/afs/cern.ch/work/j/jschulz/public/merged_dbFiles/merged_mp3218.db")
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
                                                       tag = cms.string("Deformations"),
                                                       connect = cms.string("sqlite_file:/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/mp3218/jobData/jobm/alignments_MP.db")
                                                       ),        
                                              )
                                    )
     return process

###################################################################
# Event source and run selection
###################################################################
readFiles = cms.untracked.vstring()
readFiles.extend(['/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/D265F02D-6009-E911-BFD0-0CC47A4D769A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/6E3B9696-6209-E911-A995-0025905B85CC.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/42B78A13-6509-E911-B0E2-0CC47A78A446.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/0C919B46-3709-E911-BE9C-0CC47A7C35C8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/6404B6C5-3609-E911-88F4-0CC47A78A478.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/4C066FAA-3609-E911-AF47-0CC47A4D7634.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/1EB5BF2D-7309-E911-A6E4-0CC47A78A340.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/AC7BC3BA-7909-E911-B620-0025905B855A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/BC028664-8509-E911-9F1F-0025905A6136.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/708BE6C7-A709-E911-AF2D-0CC47A78A340.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/EC0444E7-D509-E911-B00C-0CC47A78A3F8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/A017FC11-3709-E911-9143-1418776420DF.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/C07A828D-6109-E911-B499-0CC47A7C3628.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/BC39F002-6409-E911-9243-0025905A48D6.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/E4796121-3009-E911-8D61-0CC47A4C8EB6.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/98E85D51-6809-E911-8F9A-0CC47A4D75F0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/84421531-6D09-E911-8ABE-0025905A48F0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/A4BB6061-7609-E911-84B3-0CC47A7C35C8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/88C38B25-7D09-E911-8CBD-0CC47A78A3F4.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/C8C5E047-3709-E911-BDA3-0025905A605E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/D0029017-3709-E911-A91A-0CC47A4C8F12.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/FE4E2069-7F0A-E911-B0CA-549F3525B154.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/98D4F06A-5709-E911-ACCF-0CC47A7C354A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/B04BE970-5B09-E911-AE9B-0CC47A4D7690.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/56621387-5E09-E911-B766-0CC47A4D7634.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/8EDD7B2D-6009-E911-94EE-0CC47A7C3472.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/6C77112F-6009-E911-B7A2-0CC47A7C347E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/52DE285B-6109-E911-A9B3-0CC47A7C347E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/2842E411-6509-E911-B97E-0CC47A4C8EA8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/88F9EBA7-6909-E911-905E-0CC47A4C8EEA.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/7C5E07A1-6F09-E911-B991-0CC47A4C8EC8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/E499E798-7109-E911-B53B-0025905A60DE.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/2EDF7DBF-7A09-E911-9C9F-0CC47A7C3424.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/1C935A5E-8509-E911-B5E4-0025905A6138.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/B81480C2-4709-E911-B52F-0025905A48D0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/34F66E27-5A09-E911-899C-0CC47A4D764C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/F4A7C4F6-6309-E911-849C-0CC47A78A446.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/52A8EC57-6809-E911-85B5-0025905B8594.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/40CA7CEC-6A09-E911-94E9-0CC47A4D7640.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/4E9B63EA-6A09-E911-A041-0CC47A4C8E14.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/3EDF21F3-6A09-E911-8024-0025905A60B8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/06C2AAD0-3609-E911-9622-0CC47A78A30E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/EEAE4830-3709-E911-8AB6-0CC47A4C8E28.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/ACED5C1E-7409-E911-9485-0CC47A7C3444.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/14C461AD-AB09-E911-AD08-0CC47A4D768C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/584AD0FD-6309-E911-98B3-0025905B8600.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/283230DA-6509-E911-8E66-0CC47A4C8E82.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/6EEE4228-3009-E911-A712-0CC47A7C3444.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/48018ACB-8009-E911-A8BB-0025905A6070.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/7E9DB154-8509-E911-8EBD-0CC47A4D75F8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/F437194E-3709-E911-8305-0025905A60B0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/CEA60322-7F0A-E911-B167-44A84225C8FF.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/92C9AF45-5609-E911-90BD-0CC47A7C3422.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/94B6D9A8-5C09-E911-80EF-0CC47A4D75F4.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/10B547EE-2E09-E911-99AC-0CC47A4C8E2E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/ECE8EC97-6109-E911-BB28-0025905B85DC.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/C03108F9-6309-E911-97F3-0CC47A4C8EC6.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/2424A932-6509-E911-828D-0CC47A4C8ECA.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/FEB0D32D-7409-E911-B6E1-0025905A6092.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/84DBC785-7709-E911-B708-0CC47A78A3F8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/40708214-3809-E911-91B8-0025905B860E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/D23C632E-8E09-E911-B626-0CC47A4D7678.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/4ACB112A-3809-E911-A878-0CC47A4C8E16.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/5E00BB84-5E09-E911-9737-0CC47A4C8E20.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/90651A52-6809-E911-BA1F-0CC47A4D765E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/768ABCF2-6A09-E911-BC1C-0025905A6068.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/ACFBFCE7-2E09-E911-9262-0CC47A4D7604.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/901A45B3-3609-E911-9BC3-0CC47A4C8EA8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/7452882C-6D09-E911-A808-0CC47A4C8ECE.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/B2BBACA4-6F09-E911-96A4-0025905A607A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/343E1DEB-3609-E911-AC4F-0CC47A4C8E14.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/8AFF1D0F-3709-E911-B93E-0CC47A4C8E16.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/EE0AE809-8A09-E911-9889-0CC47A4D7692.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/96B512EA-3609-E911-A9CD-0025905B8604.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/C4DFE389-9A09-E911-B984-801844E561C0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/5CFE3214-6509-E911-B73B-0CC47A7C35A4.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/E89D976C-6809-E911-A7A8-0CC47A4C8ECA.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/0A4C82A5-6F09-E911-B4A5-0025905B85D0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/C409A2A2-7109-E911-9770-0025905A60AA.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/5EC5C060-7609-E911-94D0-0CC47A4D7616.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/F6B4E822-7D09-E911-A258-0CC47A78A3B4.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/E0BA1A7C-7F09-E911-8BF1-0CC47A4C8E96.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/90073071-3709-E911-9220-0CC47A4D75EC.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/E0566BCF-8F09-E911-BFCE-0025905A60DA.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/6855B501-230A-E911-B582-44A84225C8DB.root'])
process.source = cms.Source("PoolSource",
                            fileNames = readFiles ,
                            duplicateCheckMode = cms.untracked.string('checkAllFilesOpened')
                            )

#process.load("Alignment.OfflineValidation.DATASETTEMPLATE");
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

runboundary = 274422
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
                                   fileName=cms.string("PVValidation_mp3218m_274422.root")
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
                                           intLumi = cms.untracked.double(261.910146315),
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
