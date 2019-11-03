import csv

data = {}
with open('./data.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader) # skip the headers
    for row in reader:
        epoch, _, _, tracker, value, *rest = row
        if not tracker in data:
            data[tracker] = []
        data[tracker].append((int(epoch) / 1000, float(value)))

def get_row(key):
    try:
        row = data[key]
        return row
    except KeyError:
        return False

