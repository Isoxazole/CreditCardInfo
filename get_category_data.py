import csv
import datetime

FILENAME = "2019-01-20_transaction_download.csv"
data = []
global categories
global purchase_categories
###########################################################
#variables
DATE_INDEX = 0
DESCRIPTION_INDEX = 3
CATEGORY_INDEX = 4
DEBIT_INDEX = 5
CREDIT_INDEX = 6
###########################################################

def read_file_data(path):
    with open(path, newline="") as csvfile:
        file_reader = csv.reader(csvfile)
        categories = next(file_reader)
        print(categories)
        for row in file_reader:
            data.append(row)
            print(row)

# Gets the total count for each of the types of purchases
# Also gets the purchase categories

count = {}
def get_count_categories(index):
    for row in data:
        category = row[index]
        count.setdefault(row[index], 0)
        count[category] += 1
    return list(count.keys())

# takes argument of data and indexes which need to have date converted
def clean_date_format(indexes):
    for row in data:
        for index in indexes:
            date = row[index]
            try:
                row[index] = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%m/%d/%y')
            except ValueError:
                raise ValueError("Incorrect format, should be YYYY-MM-DD")
        print(row)

def get_analysis(category):
    num_total_trans = 0
    num_debit_trans = 0
    total_debit = 0
    total_credit = 0
    for row in data:
        if row[CATEGORY_INDEX] == category:
            num_total_trans += 1

            if row[DEBIT_INDEX] != '':
                total_debit += float(row[DEBIT_INDEX])
                num_debit_trans += 1
            else:
                total_credit += float(row[CREDIT_INDEX])
    avg_cost = float(total_debit / num_debit_trans) if num_debit_trans != 0 else 0

    return [num_total_trans, num_debit_trans, total_debit, total_credit, avg_cost]


data_json = {}

def analyze_categories():
    for purchase_category in purchase_categories:
        index = purchase_categories.index(purchase_category)
        num_total_trans, num_debit_trans, total_debit, total_credit, avg_cost = get_analysis(purchase_category)
        purchase_categories[index]= {"num_total_trans": num_total_trans,
                                      "num_debit_trans": num_debit_trans,
                                      "total_debit": total_debit,
                                      "total_credit": total_credit,
                                      "avg_cost": avg_cost}
        data_json[purchase_category] = purchase_categories[index]
    for key, value in data_json.items():
        print(key, " = ", value)
read_file_data(FILENAME)
purchase_categories = get_count_categories(CATEGORY_INDEX)
print(purchase_categories)
clean_date_format([0, 1])
analyze_categories()