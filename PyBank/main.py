 # PyBank

# Read in the csv file budget_data.csv
import os
import csv

# Set path for file
budget_csv = os.path.join("budget_data.csv")

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

#Define the function and have it accept the 'budget_data' as its sole parameter
def pybank(budget_data):

# Assign values to variables with descriptive names
    #date_column = int(budget_data[0])
    values_column = int(budget_data[0])

    #-----------------------

    # Calculate total number of months included in the dataset

    #total_months = profit_loss

    total_months = sum (1 for row in csvreader)-1
    print(total_months)

    # Calculate net amount of profit/losses over the entire period

    net_amount = sum(values_column)
        
    print(net_amount)

    # Calculate average of the changes in profit/losses over the entire period



    # Calculate greatest increase in profits (date and amount) over the entire period

    # Calculate the greatest decrease in losses (date and amount) over the entire period

    # Print analysis to the terminal
    #print(f"{values_column}")
    #print(f"{PercWon}% of matches won")
    #print(f"{PercLost}% of matches lost")
    #print(f"{PercDraw}% of matches drawn")


    print(pybank)

# Export analysis to text file

