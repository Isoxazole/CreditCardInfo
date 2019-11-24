import csv
from matplotlib import pyplot



filename = "2019-01-20_transaction_download.csv"

with open(filename) as f:
    reader = csv.reader(f)

    postedDate, description, category, debit, credit = [], [], [], [], []

    headers = next(reader)

    def getHeaderIndex(choiceList, categoryChoice):

        return choiceList.index(categoryChoice)


    print(getHeaderIndex(headers, "Category"))

    for row in reader:
        category.append(row[getHeaderIndex(headers, "Category")])

    categorySet = list(set(category))
    print(categorySet)

    for row in reader:
        print(row)




