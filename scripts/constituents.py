from bs4 import BeautifulSoup
import csv
from os import mkdir
from os.path import exists, join
import urllib.request as request


datadir = join('..', 'data')
if not exists(datadir):
    mkdir(datadir)

if not exists('tmp'):
    mkdir('tmp')

source = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
cache = join('tmp', 'List_of_S%26P_500_companies.html')

def retrieve():
    request.urlretrieve(source, cache)

def extract():
    source_page = open(cache).read()
    soup = BeautifulSoup(source_page, 'html.parser')
    table = soup.find("table", { "class" : "wikitable sortable" })

    # Fail now if we haven't found the right table
    header = table.findAll('th')
    if header[0].string != "Ticker symbol" or header[1].string != "Security":
        raise Exception("Can't parse wikipedia's table!")

    # Retreive the values in the table
    records = []
    rows = table.findAll('tr')
    for row in rows:
        fields = row.findAll('td')
        if fields:
            symbol = fields[0].string
            # fix as now they have links to the companies on WP
            name = ' '.join(fields[1].stripped_strings)
            sector = fields[3].string
            records.append([symbol, name, sector])

    header = ['Symbol', 'Name', 'Sector']
    writer = csv.writer(open('../data/constituents.csv', 'w'), lineterminator='\n')
    writer.writerow(header)
    # Sorting ensure easy tracking of modifications
    records.sort(key=lambda s: s[1].lower())
    writer.writerows(records)    

def process():
    retrieve()
    extract()

if __name__ == '__main__':
    process()

