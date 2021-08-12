import csv
import pandas as pd

dataset_1 = []
dataset_2 = []

with open('bright_stars.csv','r') as f:
    csv_reader =csv.reader(f)
    for i in csv_reader:
        dataset_1.append(i)

with open('dwarf_stars.csv','r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        dataset_2.append(i)

star_data_1 = dataset_1[1:]
star_data_2 = dataset_2[1:]

star_data =[]

for i in star_data_1:
    star_data.append(i)

for j in star_data_2:
    star_data.append(j)

with open("final_merged.csv",'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(dataset_1[0])
    csvwriter.writerows(star_data)

df = pd.read_csv('Final_merged.csv')
df = df[df['Distance'].notna()]
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]
del df['Unnamed: 0']
df.to_csv('Final_merged.csv') 