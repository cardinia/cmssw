#!/bin/bash


for file in *
do 

 mv -v "$file" "$(echo $file | sed 's/Dataset_Alignment_DoubleMuon_Run2018ABCD-TkAlZMuMu-PromptReco-v123_ALCARECO_IOV/Dataset_Alignment_DoubleMuon_Run2018ABCD-TkAlZMuMu-PromptReco-v123_ALCARECO_since/g')" 

done
