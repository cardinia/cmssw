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
readFiles.extend(['/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/C8170971-5709-E911-9402-0025905B85C0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/281CFEA2-5809-E911-A18C-0CC47A7C354A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/E235D7B4-2109-E911-85AF-0CC47A4D7644.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/4E89AE2F-6009-E911-945D-0CC47A7C347E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/02FB9A3B-6009-E911-89E2-0025905B858A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/6E3B9696-6209-E911-A995-0025905B85CC.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/A8FBB6ED-2709-E911-84BC-0CC47A7C3430.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/1EB5BF2D-7309-E911-A6E4-0CC47A78A340.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/708BE6C7-A709-E911-AF2D-0CC47A78A340.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/EC0444E7-D509-E911-B00C-0CC47A78A3F8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/462588B1-9309-E911-BBD2-008CFAC93C44.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/2CEF7FB8-E409-E911-92D0-EC0D9A8221CE.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/DADFCB0E-5409-E911-921F-0CC47A4D7630.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/B8CB14A3-2A09-E911-8041-0CC47A4D767A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/76AC983B-6009-E911-A614-0025905B858A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/764A602D-1D09-E911-8DBA-0CC47A4D76B6.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/FEDCFCF7-6309-E911-99F7-0CC47A4C8EE8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/98E85D51-6809-E911-8F9A-0CC47A4D75F0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/84421531-6D09-E911-8ABE-0025905A48F0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/FEE80995-2B09-E911-B385-0025905A6090.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/62C2703B-AE09-E911-BA0D-008CFAC93BF0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/D4ED1F44-6D09-E911-AF4E-E0071B749C80.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/4E250CFB-9009-E911-BEE9-008CFA1113D8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/FE7C8682-2809-E911-B880-0CC47A78A408.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/98D4F06A-5709-E911-ACCF-0CC47A7C354A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/B04BE970-5B09-E911-AE9B-0CC47A4D7690.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/98E7E77B-2809-E911-8994-0CC47A7C34E6.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/56621387-5E09-E911-B766-0CC47A4D7634.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/C059442F-6009-E911-B56B-0CC47A7C347E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/7E83F8F8-6309-E911-B60E-0CC47A74527A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/A227FF5D-2B09-E911-9FA9-0CC47A4C8EC6.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/6E454725-1E09-E911-BBAA-0CC47A4D76D0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/FA843C7E-2709-E911-BA3D-0CC47A4D7650.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/EECAEE4A-2809-E911-8A8A-0CC47A4D765A.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/92C34355-6809-E911-A06B-0CC47A4C8EEA.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/569488CA-2809-E911-9D61-0025905A610C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/56227754-6D09-E911-9096-008CFA197B54.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/2C9D03FC-5609-E911-9740-0242AC130002.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/EE8798E1-2A09-E911-AB3B-0CC47A4C8F26.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/420BEDBA-2A09-E911-9263-0CC47A78A42E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/6878D915-5A09-E911-A27D-0CC47A4D75F4.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/34F66E27-5A09-E911-899C-0CC47A4D764C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/1EDB21B2-5C09-E911-A8E9-0025905B8592.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/F2C847F5-6309-E911-9A74-0CC47A78A4B8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/D4B59385-2709-E911-889E-0CC47A4D769C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/AC4B247C-2809-E911-95F7-0CC47A4D76CC.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/02E5D630-6D09-E911-A06B-0025905A60DE.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/14C461AD-AB09-E911-AD08-0CC47A4D768C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/062FBA36-6D09-E911-B2D6-008CFAC91EB8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/3CA7378B-5B09-E911-9CD3-0CC47A2B0700.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/E865A553-1F09-E911-B2AE-0CC47A78A3E8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/70C9A57C-2809-E911-A426-0CC47A4D7604.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/F2569EFD-2109-E911-AB78-0025905A60DE.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/90CFDE86-8C09-E911-B160-0025905A6122.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/0E88C01F-2209-E911-9484-0CC47A4D76CC.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/92C9AF45-5609-E911-90BD-0CC47A7C3422.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/0E488EE3-2A09-E911-A488-0CC47A78A340.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/A00272AE-2009-E911-BD66-0CC47A4D7606.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/560A7E81-2909-E911-8121-0CC47A4C8F26.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/A4C040AB-2909-E911-ACDF-0CC47A7C34C8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/6475DD8E-6109-E911-B92C-0CC47A4D768C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/ECE8EC97-6109-E911-BB28-0025905B85DC.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/EAA51322-1E09-E911-87EB-0CC47A4D764C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/2424A932-6509-E911-828D-0CC47A4C8ECA.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/1E4E6FF7-2909-E911-874F-003048FFCBB8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/8E882B3D-2809-E911-A507-0CC47A4D75F2.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/0EE0E3EE-9509-E911-9FE2-0025905A6080.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/521F2105-BA09-E911-A61B-008CFAC93C1C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/249FB845-6D09-E911-8103-008CFAC941F4.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/7C830981-6D09-E911-BDA3-002590488694.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/A465F934-D309-E911-B1F4-0CC47AFC3C76.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/A6F32C30-6009-E911-9F7D-0CC47A7C34EE.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/44AB782F-1F09-E911-A47D-0CC47A7452DA.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/004E8F65-2809-E911-9AFE-0CC47A4D7638.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/2C2082F0-2909-E911-8554-0025905A60CA.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/F2736170-AB09-E911-8D54-0CC47A7C35D8.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/18F7EF0D-080A-E911-8752-008CFA1974E4.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/B4D9A017-CA09-E911-8D26-0CC47A2AED04.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/A4FCAF94-A309-E911-97C0-248A07C6D770.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/DE9CC12F-1D09-E911-83EF-0CC47A4D7666.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/A65E7B9D-2009-E911-8AE9-0CC47A4C8E22.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/6EDE65BC-2909-E911-82C5-0CC47A4C8E46.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/D4F64C43-2909-E911-87F9-0CC47A4D768E.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/B674AB3A-1E09-E911-B8CD-0025905A60D2.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/D2C7C084-2709-E911-9FED-0025905AA9F0.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/7EF37238-7F0A-E911-83E3-0025905A611C.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/280000/567D6C31-0D0A-E911-AE80-0025907277FE.root','/store/data/Run2016B/HLTPhysics/ALCARECO/TkAlMinBias-07Dec2018_ver2-v1/80000/2E29FEFB-D209-E911-AFA8-0CC47AD99116.root'])
process.source = cms.Source("PoolSource",
                            fileNames = readFiles ,
                            duplicateCheckMode = cms.untracked.string('checkAllFilesOpened')
                            )

#process.load("Alignment.OfflineValidation.DATASETTEMPLATE");
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

runboundary = 274388
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
                                   fileName=cms.string("PVValidation_mp3218m_274388.root")
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
                                           intLumi = cms.untracked.double(239.301076013),
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
