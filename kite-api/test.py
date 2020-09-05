import csv
 

# with open('test.csv', mode='a') as csv_file:
#     fieldnames = ['last_price', 'date']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writerrow({})

with open('test.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    print(dir(csv.DictReader()))
    print(reader['last_price'])