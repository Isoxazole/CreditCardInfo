import pandas as pd

filename = "2019-01-20_transaction_download.csv"

data = pd.read_csv(filename)

postedDate, description, category, debit, credit = [], [], [], [], []

headers = list(data.columns.values)

categorySets = list(set(data.Category))

print(categorySets)


def getCategory(categoryChoice):
    categoryData = []
    for num in range(0, len(data)):
        if data.Category[num] == categoryChoice:
            categoryData.append(data.iloc[num])
    return categoryData


entertainment = getCategory("Entertainment")
print(len(entertainment))

gas = getCategory("Gas/Automotive")
print(len(gas))


def getDebitSpent(category):
    debitIndex = 5
    total = 0
    for num in range(0, len(category)):
        try:
            price = int(category[num][debitIndex])
        except ValueError:
            print("This shit isn't a number")
        else:
            total += price
    return total


for category in categorySets:
    tempArray = getCategory(category)
    debitSpent =getDebitSpent(tempArray)
    print("The length of category set %s is " % category + str(len(tempArray)))
    print("The total amount spent in the "
          "category %s is " % category + str(debitSpent))




