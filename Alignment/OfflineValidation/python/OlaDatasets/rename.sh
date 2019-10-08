#!/bin/bash


for file in /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/alignmentObjects/paconnor/CMSSW_10_6_0/src/Alignment/OfflineValidation/python/OlaDatasets/*
do 

 #mv -v "$file" "$(echo $file | sed 's/IsoMu_UL16_bigStat_since/Dataset_Run2Validation_IsoMu_since/g')" 
 mv -v "$file" "$(echo $file | sed 's/Dataset_Validation_HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO_v2_since/Dataset_Run2Validation_HLTPhysics_since/g')" 


 
done
