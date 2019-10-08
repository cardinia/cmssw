#!/bin/bash 
export EOS_MGM_URL=root://eoscms.cern.ch 
JobName=PVValidation_mp3218m_280020 
echo  "Job started at " `date` 
CMSSW_DIR=/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/alignmentObjects/paconnor/CMSSW_10_6_0/src 
OUT_DIR=/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG 
LXBATCH_DIR=$PWD 
cd ${CMSSW_DIR} 
eval `scramv1 runtime -sh` 
echo "batch dir: $LXBATCH_DIR release: $CMSSW_DIR release base: $CMSSW_RELEASE_BASE" 
cd $LXBATCH_DIR 
cp /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/alignmentObjects/paconnor/CMSSW_10_6_0/src/Alignment/OfflineValidation/test/cfg/PVValidation_mp3218m_280020_cfg.py . 
echo "cmsRun PVValidation_mp3218m_280020_cfg.py" 
cmsRun PVValidation_mp3218m_280020_cfg.py 
echo "Content of working dir is "`ls -lh` 
for RootOutputFile in $(ls *root ); do xrdcp -f ${RootOutputFile} root://eoscms//eos/cms${OUT_DIR}/${RootOutputFile} ; done 
echo  "Job ended at " `date` 
exit 0 
