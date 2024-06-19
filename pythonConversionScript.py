import csv
import json

# Replace 'input.csv' with the path to your CSV file
input_csv_file = 'english&French.csv'
output_json_file = 'english&French.json'

data = {}

# Read the CSV file
with open(input_csv_file, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if len(row) == 2:  # Ensure there are two columns
            key, value = row
            data[key] = value

# Write the JSON file
with open(output_json_file, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"CSV file '{input_csv_file}' has been converted to JSON file '{output_json_file}'")