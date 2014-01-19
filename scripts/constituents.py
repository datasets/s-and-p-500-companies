import csv
import os
import urllib
import dataconverters.xls

# first run the extract
# os.system('. scripts/constituents.sh')
source = "http://us.spindices.com/idsexport/file.xls?hostIdentifier=48190c8c-42c4-46af-8d1a-0cd5db894797&selectedModule=Constituents&selectedSubModule=ConstituentsFullList&indexId=340"
xlspath = 'cache/constituents.xls'
path = 'data/constituents.csv'

def execute():
    urllib.urlretrieve(source, xlspath)

    existingr = csv.reader(open(path))
    header = existingr.next()
    # { symbol: row } dict
    existing = dict([ [row[0], row] for row in existingr ])

    # have to set explicit encoding as otherwise bad encoding error
    # ERROR *** codepage 21010 -> encoding 'unknown_codepage_21010' -> LookupError: unknown encoding: unknown_codepage_21010
    records, metadata = dataconverters.xls.parse(open(xlspath),
                excel_type='xls',
                encoding='utf8'
                )

    fields = [ f['id'] for f in metadata['fields'] ]
    # order is company name | symbol
    records = [ [ x[fields[0]], fixsymbol(x[fields[1]]) ] for x in records ]
    # chop header and footer bumpf
    records = records[6:]
    records = records[:-4]
    records.sort(key=lambda s: s[0].lower())

    writer = csv.writer(open(path, 'w'), lineterminator='\n')
    writer.writerow(header)
    for row in records:
        symbol = row[1]
        # faff around so that we preserve the existing sector info
        # have to add new sector info by hand ...
        if symbol in existing:
            writer.writerow(existing[symbol])
        else:
            print('New entry in list: %s' % row)
            row.reverse()
            writer.writerow(row + [''])

# BRK/B or BRK.B => BRK-B (this is what yahoo needs)
def fixsymbol(symbol):
    symbol = symbol.replace('/', '-')
    symbol = symbol.replace('.', '-')
    return symbol

execute()

