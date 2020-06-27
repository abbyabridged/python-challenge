# PyBank

# Modules
import os
import csv

# Set path for file
budget_csv = os.path.join("budget_data.csv")

# Open the CSV file
with open(budget_csv,'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

# Check the csv is being read
    #print(csvreader)

    #for row in csvreader:
        #print(row)

# Set variables
    total_months = 0
    
    for row in csvreader:
        total_months = int(total_months+1)

print(total_months)

 # Calculate total number of months included in the dataset

    #total_months = int(total_months+1)
    #print(total_months)

 # Calculate net amount of profit/losses over the entire period

    #net_amount = int()

     # Calculate average of the changes in profit/losses over the entire period

    # Calculate greatest increase in profits (date and amount) over the entire period

    # Calculate the greatest decrease in losses (date and amount) over the entire period

    # Print analysis to the terminal
    #print(f"{values_column}")
    #print(f"{PercWon}% of matches won")
    #print(f"{PercLost}% of matches lost")
    #print(f"{PercDraw}% of matches drawn")


    #print(pybank)

# Export analysis to text file

