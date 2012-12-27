'''Use Yahoo finance API to retrieve key financial (inspiration and thanks to http://www.gummy-stuff.org/Yahoo-data.htm)
'''
import urllib
import csv


sp500 = 'https://docs.google.com/spreadsheet/pub?key=0Aon3JiuouxLUdDU5S2NrbVJHRWVBRWxvU1dlOUQ2WUE&single=true&gid=0&output=csv'
local = 'data/s-and-p-500-basics.csv'

items = [
    ['s', 'symbol'],
    ['n', 'name'],
    ['l1', 'price'], # strictly this is ask price
    ['y', 'dividend yield'],
    ['d', 'dividend/share'],
    ['e', 'earnings/share'],
    ['b4', 'book value'],
    ['j', '52 week low'],
    ['k', '52 week high'],
    ['j1', 'market capitalization'],
    ['j4', 'ebitda'],
    ['p5', 'price/sales'],
    ['p6', 'price/book'],
    ['r', 'price/earnings'],
]
params = ''.join([ x[0] for x in items ])

reader = csv.DictReader(open(local))
symbols = []
newcsv = ','.join([ x[1] for x in items ]) + '\n'
for row in reader:
    symbols.append(row['Ticker Symbol'])
    if len(symbols) == 20:
        query = 'http://finance.yahoo.com/d/quotes.csv?s=' + '+'.join(symbols) + '&f=' + params
        fo = urllib.urlopen(query)
        newcsv += fo.read()
        symbols = []

fo = open('data/s-and-p-500-financials.csv', 'w')
fo.write(newcsv)
fo.close()

