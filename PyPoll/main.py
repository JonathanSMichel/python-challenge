# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Specify the file to read
file_data = os.path.join("../PyPoll/Resources/election_data.csv")


vote_list=[]
percentage_of_votes=[]
total_candidate_votes=[]
candidate=[]
total_votes=0

#Read CSV
with open(file_data, "r") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    #loop through data
    for row in csvreader:
        
        if row[2] not in candidate:
            candidate.append(row[2])
            index = candidate.index(row[2])
            total_candidate_votes.append(1)
        else:
            index = candidate.index(row[2])
            total_candidate_votes[index] += 1

    #Total Votes
    total_votes=len(total_candidate_votes)

    # Calculate the percentage of votes candidate won
    for votes in total_candidate_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percentage_of_votes.append(percentage)
    
    # Calulate the winner of the election
    winner = max(total_candidate_votes)
    index = total_candidate_votes.index(winner)
    winner = candidate[index]

# Show Results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidate)):
    print(f"{candidate[i]}: {str(percentage_of_votes[i])} ({str(total_candidate_votes[i])})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

# Export to .txt file
output = open("../PyPoll/Analysis/output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidate)):
    line = str(f"{candidate[i]}: {str(percentage_of_votes[i])} ({str(total_candidate_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winner}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
