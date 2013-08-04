List of companies in the S&P 500 (Standard and Poor's 500). The S&P 500 is a free-float, capitalization-weighted index of the top 500 publicly
listed stocks in the US (top 500 by market cap). The dataset includes a list of
all the stocks contained therein and their associated financials.

## Data

Detailed information on the S&P 500 (primarily in xls format) can be obtained
from its [official webpage on the Standard and Poor's website][sp-home] - it's
free but registration is required.

* Index listing - see <data/constituents.csv> extracted from [source xls on S&P
  website][sp-listing] (<del>but note you have to register and login to
  access</del> - no longer true as of August 2013)
* Constituent financials - see <data/constituents-financials.csv> (source via Yahoo Finance)
* Historical performance ([source xls on S&P website][sp-historical])

Notes:

* Market Capitalization and EBIDTA are in Billions

[sp-home]: http://www.standardandpoors.com/indices/sp-500/en/us/?indexId=spusa-500-usduf--p-us-l--
[sp-listing]: http://us.spindices.com/idsexport/file.xls?hostIdentifier=48190c8c-42c4-46af-8d1a-0cd5db894797&selectedModule=Constituents&selectedSubModule=ConstituentsFullList&indexId=340
[sp-historical]: http://www.standardandpoors.com/prot/spf/docs/indices/SPUSA-500-USDUF--P-US-L--HistoricalData.xls

### Additional materials

Also provided is a [S&P 500 Google Docs spreadsheet][gdocs] incorporating
all of the CSVs. This is licensed under the same terms as all the other data.

*Note*: for aggregate information on the S&P (dividends, earnings etc) see
[Standard and Poor's 500 Dataset][shiller]

[gdocs]: https://docs.google.com/spreadsheet/ccc?key=0Aon3JiuouxLUdDU5S2NrbVJHRWVBRWxvU1dlOUQ2WUE#gid=0
[shiller]: http://data.okfn.org/data/s-and-p-500

### Preparation

You need python plus [dataconverters][] library tool installed to run the
scripts. You also probably need to be on Linux/Unix or Mac for the shell
scripts to work.

[dataconverters]: http://okfnlabs.org/dataconverters/

#### constituents.csv

Run python script (this in turn runs the shell script
`scripts/constituents.sh`):

      python scripts/constituents.py

####  constituents-financials.csv

Run python script:

    python scripts/process.py

## General Financial Notes

Publicly listed US companies are obliged various reports on a regular basis
with the SEC. Of these 2 types are of especial interest to investors and others
interested in their finances and business. These are:

* 10-K = Annual Report
* 10-Q = Quarterly report

## License

All data is licensed under the [Open Data Commons Public Domain Dedication and
License][pddl]. All code is licensed under the MIT/BSD license.

Note that while no credit is formally required a link back or credit to [Rufus
Pollock][rp] and the [Open Knowledge Foundation][okfn] is much appreciated.

[pddl]: http://opendatacommons.org/licenses/pddl/1.0/
[rp]: http://dev.rufuspollock.org/
[okfn]: http://okfn.org/

