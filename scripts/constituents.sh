#!/bin/bash

## download

# the following assumes you have done this by hand
curl "http://us.spindices.com/idsexport/file.xls?hostIdentifier=48190c8c-42c4-46af-8d1a-0cd5db894797&selectedModule=Constituents&selectedSubModule=ConstituentsFullList&indexId=340" > cache/constituents.xls

## extract a clean csv list of current consitutents

# have to set explicit encoding as otherwise bad encoding error
# ERROR *** codepage 21010 -> encoding 'unknown_codepage_21010' -> LookupError: unknown encoding: unknown_codepage_21010
dataconvert cache/constituents.xls _.csv --encoding=utf8 | \
# chop header and footer
  tail -n +8 |
  head -n -8 |
# fix up trailing space
  sed 's/$//g' |
# sort by company name (not symbol)
  sort |
# reverse columns
  awk -F , '{print $2 "," $1 }' \
  > cache/constituents.csv

