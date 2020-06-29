# Modules
import os
import csv

# Set path for file
election_csv = os.path.join("Resources","election_data.csv")

# Open the CSV file
with open(election_csv,'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    print(f"CSV Header: {csv_header}")

#----------------------------------------------------------------------------------

# Calculate the total number of votes cast


# Create complete list of candidates who received votes


# Calculate percentage of (total?) votes each candidate won


# Calculate total number of votes each candidate won


# Determine the winner of the election based on popular vote (i.e. greatest percentage)