The S&P 500 dataset contains data on the S&P 500 index (aka Standard and Poor's
500) -- a free-float, capitalization-weighted index of the top 500 publicly
listed stocks in the US (top 500 by market cap). The dataset includes a list of
all the stocks contained therein and their associated financials.

## Data

Detailed information on the S&P 500 (primarily in xls format) can be obtained
from its [official webpage on the Standard and Poor's website][sp-home] - it's
free but registration is required.

* Index listing - see <data/constituents.csv> ([source xls on S&P
  website][sp-listing] - but note you have to register and login to access)
* Constituent financials - see <data/constituents-financials.csv> (source via Yahoo Finance)
* Historical performance ([source xls on S&P website][sp-historical])

Notes:

* Market Capitalization and EBIDTA are in Billions

[sp-home]: http://www.standardandpoors.com/indices/sp-500/en/us/?indexId=spusa-500-usduf--p-us-l--
[sp-listing]: http://www.standardandpoors.com/prot/spf/docs/indices/SPUSA-500-USDUF--P-US-L--Constituents.xls
[sp-historical]: http://www.standardandpoors.com/prot/spf/docs/indices/SPUSA-500-USDUF--P-US-L--HistoricalData.xls

### Additional materials

Also provided is a [S&P 500 Google Docs spreadsheet][gdocs] incorporating
all of the CSVs. This is licensed under the same terms as all the other data.

*Note*: for aggregate information on the S&P (dividends, earnings etc) see
[Standard and Poors 500 Shiller Dataset][shiller]

[gdocs]: https://docs.google.com/spreadsheet/ccc?key=0Aon3JiuouxLUdDU5S2NrbVJHRWVBRWxvU1dlOUQ2WUE#gid=0
[shiller]: https://github.com/datasets/standard-and-poors-500-shiller

### Preparation

#### constituents.csv

1. Source constituents file from S&P and place in cache/ (would like to automate but login required)
2. Then run script:

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

