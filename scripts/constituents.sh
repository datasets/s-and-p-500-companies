#!/bin/bash

## download

# this will not work so you have to register and login to download :-(
# the following assumes you have done this by hand
# curl http://www.standardandpoors.com/prot/spf/docs/indices/SPUSA-500-USDUF--P-US-L--Constituents.xls > cache/SPUSA-500-USDUF--P-US-L--Constituents.xls

## extract a clean csv list of current consitutents

# have to set explicit encoding as otherwise bad encoding error
# ERROR *** codepage 21010 -> encoding 'unknown_codepage_21010' -> LookupError: unknown encoding: unknown_codepage_21010
dataconvert cache/SPUSA-500-USDUF--P-US-L--Constituents.xls _.csv --encoding=utf8 | \
# chop header
  tail -n +2 |
# fix up trailing space
  sed 's/ $//g' | \
# chop first column
  cut -d , -f 2,3 | \
# sort by company name (not symbol)
  sort | \
# reverse columns
  awk -F , '{print $2 "," $1 }' \
  > cache/constituents.csv

