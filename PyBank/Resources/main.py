import os

import csv
#1. Open csv file
with open('budget_data.csv', 'r') as f:
    csv_reader = csv.reader(f, skipinitialspace=True, quotechar="'")
    next(csv_reader)
  #2 calculate intermediate values for each row n csv. 
    print (csv_reader)
    months=0 #2a. defines variables outside of the for loop
    lastmonthprofit=0
    totalprofit = 0
    totalchange = 0
    greatestincrease = -999999          #3c. Lines 29-32 define variables for the final analysis
    greatestdecrease = 999999           
    GImonth=""
    GDmonth=""
    for line in csv_reader: #2b. starts a for loop to calculate primary values from data
        print(line) #2c. this line tests whether csv file is still linked to code
        months+=1
        revenue = int(line[1])
        currentmonth = str(line [0]) #2d. Lines 16-19 draw data directly from the csv file. This will be used to perform the analysis. 
        currentprofit = revenue      
        monthlychange = revenue - lastmonthprofit
        totalprofit = totalprofit + revenue
        lastmonthprofit=revenue #2e. Lines 19-22 use the data retrieved from 2c and 2d to calculate intermediate values
        totalchange = round((totalchange + monthlychange),2) #2f. Lines 21 and 23 perform second-order calculations for further analysis. 
    if monthlychange > greatestincrease: #2h. Line 30-39 sets up a subloop that finds the months where the greatest increase and greatest decrease in profitability occured. 

          greatestincrease = monthlychange
          GImonth = currentmonth 

    elif monthlychange < greatestdecrease:

        greatestdecrease = monthlychange
        GDmonth = currentmonth
        
        print(GImonth) #2i. This line tests the if statement on lines 30 and 35
        
        #3. With intermediate values on hand, calculate the final values required for report. 
average_change = round((totalchange/months),2) #3a. This ine uses intermediate alues to obtain a final value
print(average_change)               #3b. This line tests whether the calculation in 3a was performed correctly. 

#4 Once all necessary calculations are finished, we are ready to report results
print("Financial Analysis")
print("xxxxxxxxxxxxxxxx")
print(f"Total Months: + (months)")
print(f"Total Profits: + $(totalprofit)")
print(f"Average Change: + $(average_change)")
print(f"Greatest Increase in Profits: + (GImonth): + $(greatestincrease)")
print(f"GreatestDecreaseinProfits: + (GDmonth): + (greatestdecrease)")

output_path = os.path.join('..', 'Analysis','Analysis_of_Finncial_Data_with_Python.txt')
with open('output_path', 'w') as text:

    text.write("Financial Analysis\n")
    text.write("xxxxxxxxxxxxxxxx\n")
    text.write((f"Total Period in Months: (months)\n")
    #text.write(f"Total Profits:  $({totalprofit})\n")
    text.write(f"Average Change: ${average_change}\n")