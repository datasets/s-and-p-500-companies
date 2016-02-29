from bs4 import BeautifulSoup
import csv
from os import mkdir
from os.path import exists, join
datadir = join('..', 'data')
if not exists(datadir):
    mkdir(datadir)
source_page = open('List_of_S%26P_500_companies.html').read()
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
        name = fields[1].string
        sector = fields[3].string
        records.append([symbol, name, sector])

header = ['Symbol', 'Name', 'Sector']
writer = csv.writer(open('../data/constituents.csv', 'w'), lineterminator='\n')
writer.writerow(header)
# Sorting ensure easy tracking of modifications
records.sort(key=lambda s: s[1].lower())
writer.writerows(records)    
