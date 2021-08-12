import csv
import pandas as pd

dataset_1 = []
dataset_2 = []

with open('bright.csv','r') as f:
    csv_reader =csv.reader(f)
    for i in csv_reader:
        dataset_1.append(i)
        
with open('dwarf.csv','r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        dataset_2.append(i)

planet_data_1 = dataset_1[1:]
planet_data_2 = dataset_2[1:]

planet_data =[]

for i in planet_data_1:
    planet_data.append(i)

for j in planet_data_2:
    planet_data.append(j)

with open("Finale.csv",'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(dataset_1[0])
    csvwriter.writerows(planet_data)

df = pd.read_csv('Finale.csv')
df = df[df['Distance'].notna()]
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]
del df['Unnamed: 0']
df.to_csv('Finale.csv')