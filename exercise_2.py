import csv

with open('first.csv', 'r', encoding='utf-8') as csv_file:
    read_file = csv.reader(csv_file)
    with open('last.csv', 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        for row in read_file:
            writer.writerow([row[2]]) 



