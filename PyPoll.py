#Import os module
import os

#Module for reading CSV file
import csv

#path to csv file in directory
csvpath = os.path.join('/Users/mary/anaconda3/envs/tuesday_pandas/python-challenge/PyPoll/election_data.csv')

#The total number of votes cast
with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler,delimiter = ",")
    data = list(reader)
    row_count = len(data)-1
    print("Total Votes: ", row_count)

#A complete list of candidates who received votes
with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler,delimiter = ",")
    data = list(reader)
candidates = list(set(i[2] for i in data[1:]))
print ("Candidates: ", candidates)

#The total number of votes each candidate won
with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler,delimiter = ",")
    data = list(reader)
from collections import Counter
tally = Counter([vote[2] for vote in data[1:]])
print("Counts: ", tally)

#The percentage of votes each candidate won
with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler,delimiter = ",")
    data = list(reader)
Khan_percentage = float(tally['Khan'])/sum(tally.values())
print("Khan Percentage: ", Khan_percentage*100)

Correy_percentage = float(tally['Correy'])/sum(tally.values())
print("Correy Percentage: ", Correy_percentage*100)

with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler,delimiter = ",")
    data = list(reader)
Li_percentage = float(tally['Li'])/sum(tally.values())
print("Li Percentage: ", Li_percentage*100)

with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler,delimiter = ",")
    data = list(reader)
Tooley_percentage = float(tally["O'Tooley"])/sum(tally.values())
print("O'Tooley Percentage: ", Tooley_percentage*100)


#The winner of the election based on popular vote.
with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler,delimiter = ",")
    data = list(reader)
    from collections import Counter
    tally = Counter([vote[2] for vote in data[1:]])
    current_max_number = list[1]
    for number in list:
        if number>current_max_number:
            current_max_number = number

print("Winner: ", current_max_number)