txt_data = "I like pizza"


file_path = "output.txt"


with open(file_path, 'w') as file:
    file.write(txt_data)
    # print(f"txt file '{file_path}' was created")


employees = ['Eugene', 'Squidward', 'Spongebob', 'Patrick']



file_path = "output.txt"

try:
    with open(file_path, 'w') as file:
        # file.write('\n' + txt_data)
        for employee in employees:
            file.write(employee + '\n')
        # print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists, x only work when it does not already exists that")



    # Outputting Jsonfiles

import json

employee = {
    'name': 'spingebob',
    'age' : 30,
    'job': 'frycook'
}

file_path = "output.json"

try:
    with open(file_path, 'w') as file:
        json.dump(employee, file, indent=4) #this convert the python dictionary(employee) to a json string
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists, x only work when it does not already exists that")


# With csv(Comma seperated Values)
import csv

employees = [['Name', 'Age', 'Job'], 
            ['Spongebob', 30, 'Frycook'], 
            ['Patrick', 50, 'none'],
            ['Sandy', 27, 'Scientist']]

file_path = "output.csv"

try:
    with open(file_path, 'w', newline = '') as file:
        
        writer = csv.writer(file) #writer is an object it provides methods for writing data to a csv file
        for row in employees:
            writer.writerow(row)
        print(f"CSV file '{file_path}' was created")
except FileExistsError:
    print("That file already exists, x only work when it does not already exists that")
