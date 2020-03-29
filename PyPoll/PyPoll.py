import os
import csv
import locale

ElectionData_csv = os.path.join("Resources", "election_data.csv")

#Create lists to store our desired variables/data.

votes = []
candidates = []

#Reading the data

with open(ElectionData_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #Obtaining the required output values.
    
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])
        number_of_votes = int(len(votes))

    #Cleaning up the candidates list to obtain individual counts and percentages.

    khan = int(candidates.count("Khan"))
    correy = int(candidates.count("Correy"))
    li = int(candidates.count("Li"))
    otooley = int(candidates.count("O'Tooley"))
    khan_percentage = float(khan/number_of_votes)
    correy_percentage = float(correy/number_of_votes)
    li_percentage = float(li/number_of_votes)
    otooley_percentage = float(otooley/number_of_votes)

    #Determining the winner
    if khan > correy and khan > li and khan > otooley:
        winner = "Khan"
    elif correy > khan and correy > li and correy > otooley:
        winner = "Correy"
    elif li > khan and li > correy and li > otooley:
        winner = "Li"
    elif otooley > khan and otooley > li and otooley > correy:
        winner = "O'Tooley"

#Printing in terminal.

print("----------------------------------------------------------")
print("Election Results")
print("----------------------------------------------------------")
print(f"Total Votes: {number_of_votes:,}")
print("----------------------------------------------------------")
print(f"Khan: {khan_percentage:00.2%} ({khan:,})")
print(f"Correy: {correy_percentage:00.2%} ({correy:,})")
print(f"Li: {li_percentage:00.2%} ({li:,})")
print(f"O'Tooley {otooley_percentage:00.2%} ({otooley:,})")
print("----------------------------------------------------------")
print(f"Winner: {winner}")
print("----------------------------------------------------------")

#Specifying the file to write to
output_path = os.path.join("Resources", "election_data.txt")

#Opening the file using write mode and writing to a text.
#Writing text method obtained from stackoverflow.
#Link to stackoverflow: https://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file
with open(output_path, 'w') as text_file:
    text_file.write("----------------------------------------------------------\n")
    text_file.write("Election Results\n")
    text_file.write("----------------------------------------------------------\n")
    text_file.write(f"Total Votes: {number_of_votes:,}\n")
    text_file.write("----------------------------------------------------------\n")
    text_file.write(f"Khan: {khan_percentage:00.2%} ({khan:,})\n")
    text_file.write(f"Correy: {correy_percentage:00.2%} ({correy:,})\n")
    text_file.write(f"Li: {li_percentage:00.2%} ({li:,})\n")
    text_file.write(f"O'Tooley {otooley_percentage:00.2%} ({otooley:,})\n")
    text_file.write("----------------------------------------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("----------------------------------------------------------\n")
