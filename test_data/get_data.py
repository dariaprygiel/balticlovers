import csv


def read_test_data_from_csv(file_path):
    test_data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            test_data.append(row)
    return test_data
