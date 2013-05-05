import csv
import os

# first run the extract
os.system('. scripts/constituents.sh')

path = 'data/constituents.csv'

existingr = csv.reader(open(path))
header = existingr.next()

# { symbol: row } dict
existing = dict([ [row[0], row] for row in existingr ])

writer = csv.writer(open(path, 'w'), lineterminator='\n')
writer.writerow(header)

for row in csv.reader(open('cache/constituents.csv')):
    # BRK/B => BRK.B
    symbol = row[0].replace('/', '.')
    if symbol in existing:
        writer.writerow(existing[symbol])
    else:
        writer.writerow(row)

