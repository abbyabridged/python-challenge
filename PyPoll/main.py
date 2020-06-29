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
    # print(f"CSV Header: {csv_header}")
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
# and
# Calculate percentage of votes each candidate won

#  Create an empty dictionary to hold the count of votes for each candidate
candidate_vote_count = {}
# Loop through each entry in candidates list to count the frequency of each candidate (see method here: https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/)
for x in candidates_list:
    if (x in candidate_vote_count):
        candidate_vote_count[x] += 1
    else:
            candidate_vote_count[x] = 1
# For each entry in the count of votes dictionary, print the key value pair (candidate name, count of votes)
# for key,value in candidate_vote_count.items():
        # Format output to show candidate, percentage of votes and count of votes for that candidate
                # print(key,("{:.3f}".format((value/votes_count)*100)), value) # Includes calculation for percentage of votes
        
                # #Check if fomatting works for percentage
                # print("{:.3f}".format((value/votes_count)*100))
                
#----------------------------------------------------------------------------------
# Determine the winner of the election based on popular vote

# Create variable to hold winner vote count
winner_vote_count = max(candidate_vote_count.values())
# print(winner_vote_count)

# Loop through each key value pair in the candidate vote count dictionary to find the winner
for (key,value) in candidate_vote_count.items():
    if value == winner_vote_count:
        # Print winner name
        # print(key)

        # Create variable for winner name    
        winner_name = key 

# Check winner name
# print(winner_name)

#----------------------------------------------------------------------------------
# Print analysis to the terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {str(votes_count)}")
print("----------------------------")
for key,value in candidate_vote_count.items():
    print(key,(": {:.3f}".format((value/votes_count)*100)),"% (",value,")")

print("----------------------------")
print(f"Winner: {str(winner_name)}")
print("----------------------------")

#----------------------------------------------------------------------------------
# Export analysis to text file
with open("Analysis/analysis.txt","w+") as f:
    print("Election Results", file=f)
    print("----------------------------", file=f)
    print(f"Total Votes: {str(votes_count)}", file=f)
    print("----------------------------", file=f)
    for key,value in candidate_vote_count.items():
        print(key,(": {:.3f}".format((value/votes_count)*100)),"% (",value,")", file=f)
    print("----------------------------", file=f)
    print(f"Winner: {str(winner_name)}", file=f)
    print("----------------------------", file=f)
    f.close