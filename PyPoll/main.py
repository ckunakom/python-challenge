# Import modules for reading CSV file
import os
import csv

# Path to collect data from the Resources folder
pypollpath = os.path.join('Resources', 'election_data.csv')

# Define the function to find the number of votes, percentage for each candidate and the winner 
def poll_result(total_votes, candidates):
    
    candidate_result = ""

    # Iterate over a dictionary to get:
    # - total number of votes each candidate won
    # - percentage of votes each candidate won
    for candidate_name, vote_count in candidates.items():
        percentage = vote_count / total_votes * 100
        candidate_result += f"\n{candidate_name}: {percentage:.3f}% ({vote_count})"

    # The winner of the election based on popular vote
    winner = max(candidates, key=candidates.get)

    return "Election Results" +\
        "\n-------------------------" +\
        f"\nTotal Votes: {total_votes}" +\
        "\n-------------------------" +\
        candidate_result +\
        "\n-------------------------" +\
        f"\nWinner: {winner}" +\
        "\n-------------------------"

# Create an empty dictionary to add all the candidates and the # of votes after the loop
candidates = {}
# Starting point for counting # of votes
total_votes = 0

# Read in the CSV file
with open(pypollpath, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        
        total_votes = total_votes + 1

        name = row [2]
        
        if name not in candidates:
            # add the candidate to dictionary
            candidates[name] = 1

        else:
            # add 1 to the candidate
            candidates[name] = candidates[name] + 1

# Save the result strings into the variable, so...
result_string = poll_result(total_votes, candidates)
print(result_string)

# Specify path to the file to write to
pypolltxt = os.path.join("analysis","pypoll.txt")

# Write in txt file
with open(pypolltxt, "w") as text_file:

    # Call on the result_string and print to txt file w/o calculating the poll results again
    text_file.write(result_string)
    
    text_file.close()