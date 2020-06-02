#Modules
import os
import csv

# Path to collect data from the Resources folder
filepath = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(filepath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    firstrow = next (csvreader)
    prev = firstrow[1]
    months = []
    total_months = 0
    budget =[]
    total_budget = 0

    # Total Months
    for row in csvreader:
        months.append(row[0])
        #total_months += 1
    total_months = len(months)

    # Total Budget 
    for row in csvreader:
        budget.append(row[1])
        total_budget += row[1]

    #Profit Change
    profit_change = []
    for row in csvreader:
        change = row[1] - prev
        prev = row[1]
        profit_change.append(change)


    #Average Change
    average_change = [sum(profit_change)]/len(profit_change)
    

    #Greatest Increase in Profits
    grt_inc = max(profit_change) 
    

    #Greatest Decrease in Profits 
    grt_dec = min(profit_change)  

    #Print Results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months : $ {total_months}")
    print(f"Total: $ {total_budget}")
    print(f"Average Change : {average_change} ")
    print(f"Greatest Increase in Profits: {grt_inc}  ")
    print(f"Greatest Decrease in Profits:  {grt_dec} ")
   

    # Set variable for output file

output_file = os.path.join("Budget Analysis.txt")

#Open output file 

with open(output_file, 'w') as text_file:
    text_file.write("Financial Analysis")
    text_file.write("----------------------------")
    text_file.write(f"Total Months : $ {total_months}")
    text_file.write(f"Total: $ {total_budget}")
    text_file.write("Average Change : {} ")
    text_file.write(f"Greatest Increase in Profits:   ")
    text_file.write(f"Greatest Decrease in Profits:   ")


