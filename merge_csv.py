import csv
import pandas as pd

data_set1 = []
data_set2 = []

with open("bright_stars.csv", 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data_set1.append(row)

with open("Unit_Converter_Star.csv", 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data_set2.append(row)

headers_1 = data_set1[0]
star_data_1 = data_set1[1:]
headers_2 = data_set2[0]
star_data_2 = data_set2[1:]

headers = headers_1+headers_2
star_data = []

for i in star_data_1:
    star_data.append(i)
for i in star_data_2:
    star_data.append(i)

with open("merged_dataset_stars.csv", 'w', encoding='utf8')as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)

df = pd.read_csv('merged_dataset_stars.csv')
df.tail(8)