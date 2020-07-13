List of companies in the S&P 500 (Standard and Poor's 500). The S&P 500 is a
free-float, capitalization-weighted index of the top 500 publicly listed stocks
in the US (top 500 by market cap). The dataset includes a list of all the
stocks contained therein.

## Data

Information on S&P 500 index used to be available on the [official webpage on the Standard and Poor's website][sp-home]
but until they publish it back, Wikipedia is the best up-to-date and open data source.

* Index listing - see <data/constituents.csv> extracted from Wikipedia's [SP500 list of companies][sp-list].

### Sources

Detailed information on the S&P 500 (primarily in XLS format) used to be obtained
from its [official webpage on the Standard and Poor's website][sp-home] - it was
free but registration was required.
* Index listing - see <data/constituents.csv>
  * used to be extracted from [source Excel file on S&P website][sp-listing-dec-2014] but this no longer contains a list of constituents. (Note this Excel was actually S&P 500 EPS estimates but on sheet 4 it used to have a list of members - [previous file][sp-listing] was just members but that 404s as of Dec 2014) (Note: <del>but note you have to register and login to access</del> - no longer true as of August 2013)
* Historical performance ([source xls on S&P website][sp-historical])

[sp-home]: http://www.spindices.com/indices/equity/sp-500
[sp-list]: http://en.wikipedia.org/wiki/List_of_S%26P_500_companies
[sp-listing-dec-2014]: http://www.spindices.com/documents/additional-material/sp-500-eps-est.xlsx?force_download=true
[sp-listing]: http://us.spindices.com/idsexport/file.xls?hostIdentifier=48190c8c-42c4-46af-8d1a-0cd5db894797&selectedModule=Constituents&selectedSubModule=ConstituentsFullList&indexId=340
[sp-historical]: http://www.standardandpoors.com/prot/spf/docs/indices/SPUSA-500-USDUF--P-US-L--HistoricalData.xls

*Note*: for aggregate information on the S&P (dividends, earnings, etc.) see
[Standard and Poor's 500 Dataset][shiller].

[shiller]: http://data.okfn.org/data/s-and-p-500

### General Financial Notes

Publicly listed US companies are obliged various reports on a regular basis
with the SEC. Of these 2 types are of especial interest to investors and others
interested in their finances and business. These are:

* 10-K = Annual Report
* 10-Q = Quarterly report

## Preparation

You can run the script yourself to update the data and publish them to GitHub : see [scripts README](https://github.com/datasets/s-and-p-500-companies/blob/master/scripts/README.md).

## License

All data is licensed under the [Open Data Commons Public Domain Dedication and
License][pddl]. All code is licensed under the MIT/BSD license.

Note that while no credit is formally required a link back or credit to [Rufus
Pollock][rp] and the [Open Knowledge Foundation][okfn] is much appreciated.

[pddl]: http://opendatacommons.org/licenses/pddl/1.0/
[rp]: http://rufuspollock.com/
[okfn]: http://okfn.org/
