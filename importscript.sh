#!/bin/bash
cd ./
pwd
n=3
fileToMove=""
ls -1 *.json | sed 's/.json$//' | while read col; do
   echo  $col;
   fileToMove="$col.json $fileToMove";
 
   if ((  ++count % $n == 0 )) ; then
         wait
         mv -f $fileToMove ./dirToMove/
   fi
 
done
