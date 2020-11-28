#Utilizando modulo CSV para lectura de archvios con extension CSV
import csv 

filename = 'employees.csv'

with open(filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        #print(row)
         s = row.get('Salary')
         n = row.get('Name')
         print(f'{n} earns {s}')


