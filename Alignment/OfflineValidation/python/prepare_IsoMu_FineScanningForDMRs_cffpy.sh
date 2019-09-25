#!/bin/zsh


createCffPyFile () {
    IOV=$1

    echo 'IOV   = ' $IOV

    cat IsoMu_UL16_FineScanningForDMRs_IOVXXXXXX_cff.py |  sed -e "s/IOV_Vali_XXXXXX.json/IOV_Vali_${IOV}.json/g"  > IsoMu_UL16_FineScanningForDMRs_since${IOV}_cff.py
   
}


for iov in  278271 278770 278771 278790 278795 278800 278801 278805 279000 279479 

   
    do
        createCffPyFile $iov
    done







