import os
import csv
import pathlib

csv_path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'Resources', "budget_data.csv")

revenue = []
date = []
revenue_change = []

with open(csv_path, "r") as csvfileinteracter:
    csv_reader = csv.reader(csvfileinteracter, delimiter=",")
    next(csv_reader, None)
    for row in csv_reader:
        revenue.append(float(row[1]))
        date.append(row[0])
        total_months = len(date)
        total_revenue = sum(revenue)
        avg_rev_change = round(total_revenue/total_months, 0)


    for i in range(1, len(revenue)):
        revenue_change.append(revenue[i] - revenue[i-1])
        inc_rev_change = max(revenue_change)
        dec_rev_change = min(revenue_change)
        inc_date = str(date[revenue_change.index(max(revenue_change))])
        dec_date = str(date[revenue_change.index(min(revenue_change))])



Financial_Analysis = os.path.join("FinancialAnalysis.txt")
with open(Financial_Analysis, 'w', newline="") as datafile:
    csvWriter = csv.writer(datafile)
    csvWriter.writerow(["Financial Analysis"])
    csvWriter.writerow(["----------------------------"])
    csvWriter.writerow(["Total Months: " + str(total_months)])
    csvWriter.writerow(["Total Revenue: $" + str(int(total_revenue))])
    csvWriter.writerow(["Average Revenue Change: $" + str(int(avg_rev_change))])
    csvWriter.writerow(["Greatest Increase in Revenue: " + str(inc_date) + " " + "($" + str(int(inc_rev_change)) + ")"])
    csvWriter.writerow(["Greatest Decrease in Revenue: " + str(dec_date) + " " + "($" + str(int(dec_rev_change)) + ")"])


print("Financial Analysis")
print("--------------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(int(total_revenue)))
print("Average Change: $" + str(int(avg_rev_change)))
print("Greatest Increase in Profits: " + inc_date + " ($" + str(int(inc_rev_change)))
print("Greatest Decrease in Profits: " + dec_date + " ($" + str(int(dec_rev_change)))
