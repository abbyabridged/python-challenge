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

# Create a list to store votes (assumes each vote in list is unique)
    votes_list = []

# Create a list to store candidates
    candidates_list = []

# Loop through each row in csv and add to votes list and candidates
    for row in csvreader:
        votes_list.append(row[0])
        candidates_list.append(row[2])

# Create a variable to hold number of votes
    votes_count = int(len(votes_list))
    # Check number of votes
    # print(votes_count)

#----------------------------------------------------------------------------------
# Create complete list of candidates who received votes

# Create a variable to hold unique candidate names (using sets)
candidates_set = set(candidates_list)
# Check unique candidate names
# for x in candidates_set:
#     print(x)

#----------------------------------------------------------------------------------
# Calculate total number of votes each candidate won

# Create variables to hold number of votes for each candidate
votes_khan = 0
votes_correy = 0
votes_li = 0
votes_otooley = 0

for x in candidates_list:
    if candidates_list[x] == "Khan":
        votes_khan + 1 

print(votes_khan)

# Calculate percentage of votes each candidate won



# Determine the winner of the election based on popular vote (i.e. greatest percentage)