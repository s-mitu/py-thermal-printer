#!/bin/sh
[ -z $1 ] && exit 1

TMPFILE=/tmp/$(date "+%s").png
convert -geometry 384 $1 -remap pattern:gray50 -monochrome -normalize $TMPFILE
./img-print.py $TMPFILE
rm -f $TMPFILE
