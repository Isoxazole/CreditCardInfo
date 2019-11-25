import csv
import datetime
import calendar


class CapitalOneConvert:

    # Initialize all data into a list and set the indexes for the different categories
    def __init__(self, filename, date_index=0, desc_index=3, cat_index=4, debit_index=5, credit_index=6):
        self.filename = filename
        self.data = []
        self.date_index = date_index
        self.desc_index = desc_index
        self.cat_index = cat_index
        self.debt_index = debit_index
        self.credit_index = credit_index

        with open(filename, newline="") as csvfile:
            file_reader = csv.reader(csvfile)
            categories = next(file_reader)
            print(categories)
            for row in file_reader:
                self.data.append(row)
                print(row)

    # Returns the count of transactions for each purchase category
    def get_count_categories(self):
        count = {}
        for row in self.data:
            category = row[self.cat_index]
            count.setdefault(category, 0)
            count[category] += 1
        return count

    # takes argument of data and indexes which need to have date converted
    def clean_date_format(self):
        for row in self.data:
            date = row[self.date_index]
            try:
                row[self.date_index] = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%m/%d/%y')
            except ValueError:
                raise ValueError("Incorrect format, should be YYYY-MM-DD")

    def sort_trans_category(self):
        sorted_categories = {}
        for row in self.data:
            category = row[self.cat_index]
            sorted_categories.setdefault(category, []).append(row)
        return sorted_categories

    def sort_by_month(self):
        sorted_months = {}
        for row in self.data:
            date = row[self.date_index]
            month_num = datetime.datetime.strptime(date, '%m/%d/%y').month
            month = calendar.month_name[month_num]
            sorted_months.setdefault(month, []).append(row)
        return sorted_months
shit = CapitalOneConvert("2019-01-20_transaction_download.csv")
print(shit.get_count_categories())
shit.clean_date_format()
print(shit.data)
data_sort_category = shit.sort_trans_category()
data_sort_month = shit.sort_by_month()

for key, value in data_sort_category.items():
    print(key)
    print(value, "\n")

for key, value in data_sort_month.items():
    print(key)
    print(value, "\n")

