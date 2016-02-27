import urllib
import csv

def correctToBillions(item):
    if item.endswith('M'):
        return float(item[:-1]) / 1000
    elif item.endswith('B'):
        return item[:-1]
    else:
        return item

items = [
    ['l1', 'Price'], # strictly this is ask price
    ['y', 'Dividend Yield'],
    ['r', 'Price/Earnings'],
    ['e', 'Earnings/Share'],
    ['b4', 'Book Value'],
    ['j', '52 week low'],
    ['k', '52 week high'],
    ['j1', 'Market Cap'],
    ['j4', 'EBITDA'],
    ['p5', 'Price/Sales'],
    ['p6', 'Price/Book']
]
params = ''.join([ x[0] for x in items ])

url = 'http://download.finance.yahoo.com/d/quotes.csv?'
edgar = 'http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK='


reader = csv.reader(open('../data/constituents.csv'))
outrows = [ row for row in reader ]
symbols = [ row[0] for row in outrows[1:] ]

outrows[0] += [ item[1] for item in items ] + ['SEC Filings']

for idx in range(0,len(symbols),20):
    query = url + 's=' + '+'.join(symbols[idx:idx+20]) + '&f=' + params
    fo = urllib.urlopen(query)
    tmpcsv  = csv.reader(fo)
    rows = [ row for row in tmpcsv ]
    for count, row in enumerate(rows):
        realidx = idx + count + 1
        # change n/a to empty cell
        row = [ x.replace('N/A', '') for x in row ]
        # market cap and ebitda have 'B' or 'M' in them sometimes
        row[7] = correctToBillions(row[7])
        row[8] = correctToBillions(row[8])
        # add the edgar link
        row.append(edgar + symbols[realidx-1])
        outrows[realidx] = outrows[realidx] + row
    print('Processed: %s rows' % (idx + 20))

fo = open('../data/constituents-financials.csv', 'w')
writer = csv.writer(fo, lineterminator='\n')
writer.writerows(outrows)
fo.close()
