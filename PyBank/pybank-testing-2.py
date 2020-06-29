# PyBank

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
    print(f"CSV Header: {csv_header}")

# Check the csv is being read
    print(csvreader)

# Create a list to store all of the months
    months_list = []

# Create a list to store the profit/loss values
    profitloss_list = []

    for row in csvreader:
        
        # Add each row in the date column to the months list
        months_list.append(row[0])

# Check the months are being stored in the list
# print (months_list)

# Calculate total number of months included in the dataset
# Check the total number of months is correct
# print (len(months_list))

        # Add each row in the profit/losses column to the profit/loss list
        profitloss_list.append(int(row[1]))

# Check the profit/loss values are being stored in the list 
# print (profitloss_list)

# Calculate net amount of profit/losses over the entire period
net_amount = sum(profitloss_list)

# Check net amount is being calculated correctly
# print(net_amount)

# Calculate average of the changes in profit/losses over the entire period

    # Look at profit/loss column 
    # Retrieve value in next row 
    # Substract value in current row
    # Add difference to the total_change_pl variable

        #total_change_pl = int((row+1)[1])

        # total_change_pl = int(next(row[1]))

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

# Check average change
# print(average_change)

# Calculate greatest increase in profits (date and amount) over the entire period



# Calculate the greatest decrease in losses (date and amount) over the entire period

# Print analysis to the terminal

# Export analysis to text file