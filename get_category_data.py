import csv
import datetime

FILENAME = "2019-01-20_transaction_download.csv"
data = []
global categories
def read_file_data(path):
    with open(path, newline="") as csvfile:
        file_reader = csv.reader(csvfile)
        categories = next(file_reader)
        print(categories)
        for row in file_reader:
            data.append(row)
            print(row)

count = {}
def get_count_categories(data, index):
    for row in data:
        category = row[index]
        count.setdefault(row[index], 0)
        count[category] += 1
    print(count)

# takes argument of data and indexes which need to have date converted
def convert_date_format(data, indexes):
    for row in data:
        for index in indexes:
            date = row[index]
            try:
                row[index] = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%m/%d/%y')
            except ValueError:
                raise ValueError("Incorrect formant, should be YYYY-MM-DD")
        print(row)

read_file_data(FILENAME)
get_count_categories(data, 4)
convert_date_format(data,[0,1])