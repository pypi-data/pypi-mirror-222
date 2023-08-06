import csv

with open('deleteme.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Identifier'], "is a", row['Type'], "in", row['Region'], "and it's deleteme tag says", row['Tag: deleteme'])
