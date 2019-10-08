#!/bin/bash 
MAIL=$USER@mail.cern.ch 
OUT_DIR=/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF
FILE=/tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016 testUL16_EOY16_EOY16new_mp3218merged_RunF.root
echo $HOST | mail -s "Harvesting job started" $USER@mail.cern.ch 
cd /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/alignmentObjects/paconnor/CMSSW_10_6_0/src
eval `scram r -sh` 
mkdir -p /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277932.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277934.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277935.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277981.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277983.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277984.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277985.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277990.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277991.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277992.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278017.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278018.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278167.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278175.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278193.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278239.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278240.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278273.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278274.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278288.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278289.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278290.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278308.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278309.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278310.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278315.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278345.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278346.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278349.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278366.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278406.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278509.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278761.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278769.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278770.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278801.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278802.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278803.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278804.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278805.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278807.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
xrdcp root://eoscms//eos/cms/store/group/alca_trackeralign/tkello/test_out/2016UltraLegacytestUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278808.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF 
hadd /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016testUL16_EOY16_EOY16new_mp3218merged_RunF.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277932.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277934.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277935.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277981.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277983.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277984.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277985.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277990.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277991.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_277992.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278017.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278018.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278167.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278175.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278193.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278239.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278240.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278273.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278274.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278288.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278289.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278290.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278308.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278309.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278310.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278315.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278345.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278346.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278349.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278366.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278406.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278509.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278761.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278769.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278770.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278801.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278802.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278803.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278804.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278805.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278807.root /tmp/$USER/testUL16_EOY16_EOY16new_mp3218merged_RunF/PVValidation_EOY2016_278808.root 
echo "xrdcp -f $FILE root://eoscms//eos/cms$OUT_DIR" 
xrdcp -f $FILE root://eoscms//eos/cms$OUT_DIR 
echo "Harvesting for testUL16_EOY16_EOY16new_mp3218merged_RunF task is complete; please find output at $OUT_DIR " | mail -s "Harvesting for testUL16_EOY16_EOY16new_mp3218merged_RunF completed" $MAIL 
