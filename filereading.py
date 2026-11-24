file_path = "output.txt"

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("file does not exist")

# READING JSON FILES
import json

file_path = 'output.json'


try:
    with open(file_path, 'r') as file:
        content = json.load(file)
        print(content)

except FileNotFoundError:
    print("file does not exist")


import csv


file_path = 'output.csv'

try:
    with open(file_path, 'r') as file:
        content = csv.reader(file)
        for line in content:
            print(line)
     

except FileNotFoundError:
    print('That file was not found')