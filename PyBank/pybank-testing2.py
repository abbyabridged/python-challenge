# PyBank

# Read in the csv file budget_data.csv
import os
import csv

# Set path for file
csvpath = os.path.join("budget_data.csv")

# Read in the CSV file
with open(csvpath, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

#Set variables

total_months = int(csvreader[1])
#total_months = 0

#net_amount = int()

for row in csvreader:

 # Calculate total number of months included in the dataset
    #total_months = int(total_months+1)
    #print(total_months)

    print(total_months)

 # Calculate net amount of profit/losses over the entire period

    #net_amount = int()

     # Calculate average of the changes in profit/losses over the entire period

    # Calculate greatest increase in profits (date and amount) over the entire period

    # Calculate the greatest decrease in losses (date and amount) over the entire period

    # Print analysis to the terminal

    #print(pybank)

# Export analysis to text file

