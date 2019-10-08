#!/bin/bash 
MAIL=$USER@mail.cern.ch 
OUT_DIR=/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG
FILE=/tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016 testUL16_EOY16_EOY16new_mp3218merged_RunG.root
echo $HOST | mail -s "Harvesting job started" $USER@mail.cern.ch 
cd /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/alignmentObjects/paconnor/CMSSW_10_6_0/src
eval `scram r -sh` 
mkdir -p /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278820.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278821.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278822.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278873.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278874.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278875.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278923.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278957.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278962.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278963.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278969.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278975.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278976.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278986.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279024.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279029.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279071.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279080.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279115.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279116.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279479.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279480.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279488.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279489.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279588.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279653.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279654.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279656.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279658.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279667.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279681.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279682.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279683.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279684.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279685.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279691.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279694.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279715.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279716.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279760.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279766.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279767.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279794.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279823.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279841.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279844.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279887.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279931.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279966.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279975.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279993.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279994.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279995.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280002.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280006.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280007.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280013.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280014.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280015.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280016.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280017.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280018.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280020.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280023.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280024.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280187.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280188.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280190.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280191.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280194.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280242.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280249.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280251.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280327.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280330.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280349.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280363.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280364.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280383.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280384.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280385.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG 
hadd /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016testUL16_EOY16_EOY16new_mp3218merged_RunG.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278820.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278821.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278822.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278873.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278874.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278875.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278923.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278957.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278962.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278963.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278969.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278975.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278976.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_278986.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279024.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279029.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279071.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279080.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279115.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279116.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279479.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279480.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279488.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279489.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279588.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279653.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279654.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279656.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279658.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279667.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279681.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279682.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279683.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279684.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279685.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279691.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279694.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279715.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279716.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279760.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279766.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279767.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279794.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279823.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279841.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279844.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279887.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279931.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279966.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279975.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279993.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279994.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_279995.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280002.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280006.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280007.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280013.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280014.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280015.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280016.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280017.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280018.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280020.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280023.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280024.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280187.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280188.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280190.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280191.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280194.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280242.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280249.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280251.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280327.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280330.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280349.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280363.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280364.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280383.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280384.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunG/PVValidation_EOY2016_280385.root 
echo "xrdcp -f $FILE root://eoscms//eos/cms$OUT_DIR" 
xrdcp -f $FILE root://eoscms//eos/cms$OUT_DIR 
echo "Harvesting for testUL16_EOY16_EOY16new_mp3218merged_RunG task is complete; please find output at $OUT_DIR " | mail -s "Harvesting for testUL16_EOY16_EOY16new_mp3218merged_RunG completed" $MAIL 
