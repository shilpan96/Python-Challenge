#Modules
import os
import csv

#Path to file 
election_data = os.path.join("Resources","election_data.csv")

#Open the file
with open(election_data,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    #Start the pointer after the header
    header=next(csvreader)
    votes=[]

    # Total Votes 
    for row in csvreader:
        votes.append(row[2])
        total_votes = 0 
        total_votes = len(votes)

    # List of candidates
    candidate_list = []
    for x in votes:
        if x not in candidate_list:
            candidate_list.append(x)


    # Calculate number of votes received for each candidate 
    candidate_num_list =[]
    candidate_percent_list =[]
    candidate_num_list =[ votes.count(item) for item in candidate_list]

    # Calculate percentage of votes received for each candidate 
    y=0
    while y < len(candidate_num_list):
        candidate_percent_list.append(candidate_num_list[y]/total_votes)
        y=y+1

    #Find winner by popular vote

    winner_index = 0
    winner_index = candidate_num_list.index(max(candidate_num_list))
    winner = candidate_list[winner_index]

    #Print results

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    print(candidate_list[0]+ ": " + "{:.3%}".format(candidate_percent_list[0]) + "% (" + str(candidate_num_list[0]) + ")")
    print(candidate_list[1]+ ": " + "{:.3%}".format(candidate_percent_list[1]) + "% (" + str(candidate_num_list[1]) + ")")
    print(candidate_list[2]+ ": " + "{:.3%}".format(candidate_percent_list[2]) + "% (" + str(candidate_num_list[2]) + ")")
    print(candidate_list[3]+ ": " + "{:.3%}".format(candidate_percent_list[3]) + "% (" + str(candidate_num_list[3]) + ")")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# Set variable for output file

output_file = os.path.join("Election_Results.txt")

#Open output file 

with open(output_file, 'w') as text_file:
    text_file.write("Election Results")
    text_file.write("\n-------------------------")
    text_file.write("\nTotal Votes: {total_votes}")
    text_file.write("\n-------------------------")
    text_file.write("\n" + candidate_list[0]+ ": " + "{:.3%}".format(candidate_percent_list[0]) + "% (" + str(candidate_num_list[0]) + ")")
    text_file.write("\n" + candidate_list[1]+ ": " + "{:.3%}".format(candidate_percent_list[1]) + "% (" + str(candidate_num_list[1]) + ")")
    text_file.write("\n" + candidate_list[2]+ ": " + "{:.3%}".format(candidate_percent_list[2]) + "% (" + str(candidate_num_list[2]) + ")")
    text_file.write("\n" + candidate_list[3]+ ": " + "{:.3%}".format(candidate_percent_list[3]) + "% (" + str(candidate_num_list[3]) + ")")
    text_file.write("\n-------------------------")
    text_file.write("\nWinner: {winner}")
    text_file.write("\n-------------------------")
