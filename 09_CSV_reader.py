#Utilizando modulo CSV para lectura de archvios con extension CSV
import csv 

filename = 'employees.csv'

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)


