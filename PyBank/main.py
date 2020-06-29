# Modules
import os
import csv

# Set path for file
budget_csv = os.path.join("Resources","budget_data.csv")

# Open the CSV file
with open(budget_csv,'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    # print(f"CSV Header: {csv_header}")

# Check the csv is being read
    # print(csvreader)
#----------------------------------------------------------------------------------
# Create a list to store all of the months
    months_list = []

# Create a list to store the profit/loss values
    profitloss_list = []

    for row in csvreader:
        
        # Add each row in the date column to the months list
        months_list.append(row[0])

# Check the months are being stored in the list
# print (months_list)
#----------------------------------------------------------------------------------
# Calculate total number of months included in the dataset
# Check the total number of months is correct
# print (len(months_list))

        # Add each row in the profit/losses column to the profit/loss list
        profitloss_list.append(int(row[1]))

# Check the profit/loss values are being stored in the list 
# print (profitloss_list)

# Create a variable to hold the number of months
num_months =  int(len(months_list))
# print(num_months)
#----------------------------------------------------------------------------------
# Calculate net amount of profit/losses over the entire period
net_amount = sum(profitloss_list)

# Check net amount is being calculated correctly
# print(net_amount)

# Set variable for profit/losses list length for range defintion
pl_list_len = int(len(profitloss_list))

# Create list to store profit/loss changes
pl_change_list = []

# Loop through the profit/loss list 
for i in range(1, pl_list_len):
    #  Calculate the change in profit/loss for each month, by subtracting the previous month from current month
    pl_change = profitloss_list[i] - profitloss_list[i-1]
    # Add each change to the list of profit/loss changes
    pl_change_list.append(pl_change)

# Check the profit/loss changes list 
# print(pl_change_list)

# Calculate the total profit/loss change and check
# total_pl_change = sum(pl_change_list)
# print(total_pl_change)

# Calculate the average of the changes in profit/losses over the entire period
# Subtract 1 from the profit/loss list length, as change cannot be calculated for first month
average_change =  sum(pl_change_list)/(pl_list_len-1)
# Format average change (print float to 2 decimal places)
average_change = "{:.2f}".format(average_change)
# print(average_change)

# Check average change
# print(average_change)
#----------------------------------------------------------------------------------
# Calculate greatest increase in profits (date and amount) over the entire period
# and
# Calculate the greatest decrease in losses (date and amount) over the entire period

# Check value for greatest increase in profits 
# max(pl_change_list)
# print(max(pl_change_list))

# Set variable for profit/loss change list length for range definition
pl_change_list_len = int(len(pl_change_list))
# print(pl_change_list_len)

# Loop through profit/loss change list
for x in range(0,pl_change_list_len):
    # Create variables to capture the max/min list values (represents greatest increase/decrease in profits)
    greatest_pl_inc = max(pl_change_list)
    greatest_pl_dec = min(pl_change_list)
    # if pl_change_list[x] == greatest_pl_inc:
        # print(greatest_pl_inc)
        # print(pl_change_list.index(greatest_pl_inc))
    # if pl_change_list[x] == greatest_pl_inc:
    #     print(greatest_pl_dec)
    #     print(pl_change_list.index(greatest_pl_dec))

    # Create variables to hold the index number of greatest increase/decrease
    greatest_pl_inc_index = pl_change_list.index(greatest_pl_inc)
    greatest_pl_dec_index = pl_change_list.index(greatest_pl_dec)

# Retrieve the corresponding date from the months list, based on the index number of the greatest increase in profits
# Add 1 to index number as there is an extra value (Jan-10) in months list compared to profit/loss change list
for y in range(0,num_months):
    greatest_pl_inc_month = months_list[greatest_pl_inc_index+1]
    greatest_pl_dec_month = months_list[greatest_pl_dec_index+1]

# Check greatest increase in profits and corresponding month are correct
# print(greatest_pl_inc)
# print(greatest_pl_inc_month)

# Check greatest decrease in profits and corresponding month are correct
# print(greatest_pl_dec)
# print(greatest_pl_dec_month)

#----------------------------------------------------------------------------------
# Print analysis to the terminal

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(num_months)}")
print(f"Total: ${str(net_amount)}")
print(f"Average Change: ${str(average_change)}")
print(f"Greatest Increase in Profits: {str(greatest_pl_inc_month)} (${str(greatest_pl_inc)})")
print(f"Greatest Decrease in Profits: {str(greatest_pl_dec_month)} (${str(greatest_pl_dec)})")
#----------------------------------------------------------------------------------
# Export analysis to text file
with open("Analysis/analysis.txt","w+") as f:
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print(f"Total Months: {str(num_months)}", file=f)
    print(f"Total: ${str(net_amount)}", file=f)
    print(f"Average Change: ${str(average_change)}", file=f)
    print(f"Greatest Increase in Profits: {str(greatest_pl_inc_month)} (${str(greatest_pl_inc)})", file=f)
    print(f"Greatest Decrease in Profits: {str(greatest_pl_dec_month)} (${str(greatest_pl_dec)})",file=f)
    f.close