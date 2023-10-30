import csv

list_data = [["222410103010"], ["222410103057"], ["222410103084"], ["222410103089"]]
file_csv = "Nim.csv"

def tambah_data(data):
  with open(file_csv, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(data)

list(map(tambah_data, list_data))