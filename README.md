<a href="https://datahub.io/core/s-and-p-500-companies"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25)" alt="badge" /></a>

# S&P 500 Companies Dataset

List of companies in the S&P 500 (Standard and Poor's 500). The S&P 500 is a free-float, capitalization-weighted index of the top 500 publicly listed stocks in the US (top 500 by market cap). The dataset includes a list of all the stocks contained therein.

## Data

Information on S&P 500 index used to be available on the [official webpage on the Standard and Poor's website][sp-home] but until they publish it back, Wikipedia's [SP500 list of companies][sp-list] is the best up-to-date and open data source.

## Sources

Detailed information on the S&P 500 (primarily in XLS format) used to be obtained from its [official webpage on the Standard and Poor's website][sp-home] - it was free but registration was required.

[sp-home]: http://www.spindices.com/indices/equity/sp-500

> **Note**
> For aggregate information on the S&P (dividends, earnings, etc.) see [Standard and Poor's 500 Dataset][shiller].

[shiller]: http://data.okfn.org/data/s-and-p-500

## General Financial Notes

Publicly listed US companies are obliged various reports on a regular basis with the SEC. Of these 2 types are of especial interest to investors and others interested in their finances and business. These are:

- 10-K = Annual Report
- 10-Q = Quarterly report

## Development

The pipeline relies on Python, so you'll need to have it installed on your machine. Then:

1. Create a virtual environment in a directory using Python's venv module: `python3 -m venv .env`
2. Activate the virtual environment: `source .env/bin/activate`
3. Install the dependencies: `pip install -r scripts/requirements.txt`
4. Run the scripts: `python scripts/scrape.py`

Alternatively, you can use the provided Makefile to run the scraping with a simple `make`. It'll create a virtual environment, install the dependencies and run the script.

## License

All data is licensed under the [Open Data Commons Public Domain Dedication and License][pddl]. All code is licensed under the MIT/BSD license.

Note that while no credit is formally required a link back or credit to [Rufus Pollock][rp] and the [Open Knowledge Foundation][okfn] is much appreciated.

[pddl]: http://opendatacommons.org/licenses/pddl/1.0/
[rp]: http://rufuspollock.com/
[okfn]: http://okfn.org/
