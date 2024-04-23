#!/bin/bash
cd $1
pwd
n=10
fileToMove=""
ls -1 *.json | sed 's/.json$//' | while read col; do
   echo  $col;
   mongoimport --uri "mongodb+srv://temp_michael:am2SWrMoMX9I8vZp@dev-pluto-azure-eun-001.bgj1m.mongodb.net/dev-lsauthmigration-002"  --collection "lsauth_test_vm_multi_5" --file $col.json  --type json&
     fileToMove= "${col},${fileToMove}"
  (( ++count % n == 0 )) && wait
  mv -R ${fileToMove} ./dirToMove/	
done
