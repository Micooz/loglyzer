#! /bin/bash

files=`ls .`
for file in $files ; do
    if [ ${file##*.} = "ui" ] ; then
        pyuic5 -o "ui_"${file%.*}".py" $file
    fi
done
