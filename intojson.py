import csv
import json


def convert_csv_to_json():
    """
    Converts a CSV file to a JSON file.
    """
    data = []
    with open("jobs.csv", "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    with open("jobs.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)  # indent for pretty printing
