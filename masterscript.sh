#!/bin/bash
#detect if we have all arguments

if [ $# == 6 ]; then
    echo "The outputfilenamebase is $1"
    echo "the number of cubes is $2"
    echo "you will be using the virtualplotter: $3"
    echo "you will be using: $4"
    echo "you will be rendering $5 lines"
    echo "processing in inkscape: $6"

else
    echo "please supply all needed arguments: filenamebase, numberofcubes, virtualplotting virtual/real, union bool union/nounion, hiddenlines hidden/not, processing process/noprocess"
    exit
fi

filename=$1_$(date +"%m_%d_%Y_%H%M")
echo $filename

### first generate geometry in blender, pass on filenames from argument, as well as parameters for geometry script
/Applications/Blender/blender.app/Contents/MacOS/blender stroketesting.blend --background --python generateandrender.py -- $filename $2 $4
filename+=0000.svg 
echo $filename
if [ $6 == process ]; then
    cp $PWD/$filename $PWD/processed_$filename
    /usr/local/bin/inkscape $PWD/processed_$filename --verb EditSelectAll --verb SelectionSimplify --verb FileSave --verb FileQuit
    python plotrender.py $PWD/processed_$filename $3 $5
else
    python plotrender.py $PWD/$filename $3 $5
fi
git add $filename
git commit -a -m "plotting $filename"

