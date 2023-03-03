# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Specify the file to read
file_data = os.path.join("../PyBank/Resources/budget_data.csv")

total_months = 0
net_profit_loss = 0
value = 0
change = 0
month = []
profits = []

#Read CSV
with open(file_data, "r") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Read the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Reading the first row 
    first_row = next(csvreader)
    total_months += 1
    net_profit_loss += int(first_row[1])
    value = int(first_row[1])
    
    #Loop through rows 
    for row in csvreader:
        # Track the Dates
        month.append(row[0])
        
        # Calculate monthly profit/loss change
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        net_profit_loss = net_profit_loss + int(row[1])

    #Average change in "Profit/Losses between months over entire period"
    average_change = sum(profits)/len(profits)

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = month[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = month[worst_index]

   

#Show Results
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(net_profit_loss)}")
print(f"Average Change: ${str(round(average_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Export to .txt file
output = open("../PyBank/Analysis/output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(net_profit_loss)}")
line5 = str(f"Average Change: ${str(round(average_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))