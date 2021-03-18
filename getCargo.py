import csv

filename = "TinyRailsCargo.csv"

rows = []
cargo = dict()

with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
        
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 

    #print(len(rows))

for resource in rows:
    cargo[resource[0]] = 0