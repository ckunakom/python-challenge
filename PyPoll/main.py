# Import modules for reading CSV file
import os
import csv

# Path to collect data from the Resources folder
pypollpath = os.path.join('Resources', 'election_data.csv')

# Specify path to the file to write to
pypolltxt = os.path.join('analysis', 'election.txt')

candidate = []
li = []
correy = []
khan = []
otooley = []

# Read in the CSV file
with open(pypollpath, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
    
        # Start adding the vote cast row by row, using candidate row... more to come
        candidate.append(row[2])

        # Using if to start counting vote for each candidate by add the count to their respective list
        # Add # vote to 'khan' list
        if "Khan" == row[2]:
            khan.append(1)

        # Add # vote to 'li' list
        elif "Li" == row[2]:
            li.append(1)

        # Add # vote to 'correy' list
        elif "Correy" == row[2]:
            correy.append(1)

        # Add # vote to 'otooley' list
        elif "O'Tooley" == row[2]:
            otooley.append(1)

# The total number of votes cast
count = len(candidate)

# A complete list of candidates who received votes
candidatelist = set(candidate)
# Checking to see who are the candidates using print(candidatelist) / omitted

# The total number of votes each candidate won
khan_ct = len(khan)
li_ct = len(li)
correy_ct = len(correy)
otooley_ct = len(otooley)

# The percentage of votes each candidate won
khan_pct = (khan_ct/count) * 100
li_pct = (li_ct/count) * 100
correy_pct = (correy_ct/count) * 100
otooley_pct = (otooley_ct/count) * 100

# The winner of the election based on popular vote
if khan_ct > li_ct and khan_ct > correy_ct and khan_ct > otooley_ct:
    winner = "Khan"
elif li_ct > khan_ct and li_ct > correy_ct and li_ct > otooley_ct:
    winner = "Li"
elif correy_ct > khan_ct and correy_ct > li_ct and correy_ct > otooley_ct:
    winner = "Correy"
elif otooley_ct > khan_ct and otooley_ct > li_ct and otooley_ct > correy_ct:
    winner = "O'Tooley"


# print("Election Results")
# print("-------------------------")
# print(f"Total Votes: {count}")
# print("-------------------------")
# print(f"Khan: {khan_pct:.3f}% ({khan_ct})")
# print(f"Correy: {correy_pct:.3f}% ({correy_ct})")
# print(f"Li: {li_pct:.3f}% ({li_ct})")
# print(f"O'Tooley: {otooley_pct:.3f}% ({otooley_ct})")
# print("-------------------------")
# print(f"Winner: {winner}")
# print("-------------------------")

# Write in txt file
with open("pypoll.txt", "w") as text_file:
    text_file.write("Election Results")


    text_file.close()