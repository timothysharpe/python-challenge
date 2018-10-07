import os
import csv

# Print CSV File

csv_path = os.path.join("..", "PyBank", "budget_data.csv")

with open(csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    for row in csv_reader:
        print(row)

#Total Months


csv_path = os.path.join("..","PyBank","budget_data.csv")
month_total=0
net_profit=0

with open(csv_path, newline='') as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")
    next(budget_reader, None)
    for row in budget_reader:
        month_total +=1
        net_profit +=int(row[1])

    print(f"The total months in this data set is {month_total}")
    print(f"The net Profit/Losses in this data set is {net_profit}")
   


#Total amount of Profit/Losses









    




