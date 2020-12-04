import csv
import os
csvpath = os.path.join('Resources', 'budget_data.csv')
file_to_output = os.path.join("analysis", "budget_analysis.txt")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    months=0 
    lastmonthprofit=0
    totalprofit = 0
    totalchange = 0
    greatestincrease = -999999
    greatestdecrease = 999999
    GImonth = ""
    GDmonth = ""
    for line in csvreader:
        months+=1
        revenue = int(line[1])
        currentmonth = str(line [0])
        currentprofit = revenue
        monthlychange = revenue - lastmonthprofit
        totalprofit = totalprofit + revenue
        astmonthprofit=revenue
        totalchange = round((totalchange + monthlychange),2)
        if monthlychange > greatestincrease:
                greatestincrease = monthlychange
                GImonth = currentmonth
        elif monthlychange < greatestdecrease:
              greatestdecrease = monthlychange
              GDmonth = currentmonth
              print(GImonth) 
        average_change = round((totalchange/months),2) 
        print(average_change)

    superlatives_summary = (
    f"\n\nElFinancial Analysis\n"
    f"xxxxxxxxxxxxxxxxxxxxxxxx\n"
    f"Total Months: {months}\n"
    f"Total Profits: ${totalprofit}\n"
    f"Average Change:  {average_change}\n"
    f"Greatest Increase in Profits:  {GImonth}: ${greatestincrease}\n"
    f"Greatest Decrease in Profits:  {GDmonth}: ${greatestdecrease}\n")
    print(superlatives_summary)

with open(file_to_output, "w") as txt_file:
    txt_file.write(superlatives_summary)