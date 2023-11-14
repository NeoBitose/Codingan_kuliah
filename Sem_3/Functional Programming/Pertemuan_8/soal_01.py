import csv

def gabung_kata(data):
    return '-'.join(data)

with open('file.csv', 'r') as row:
    reader = csv.reader(row, delimiter=',')
    hasil = list(map(gabung_kata, reader))

print(hasil)

