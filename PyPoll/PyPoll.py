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

#EIEELN HELP: (below code didn't work) A complete list of candidates who received votes
def unique(list1):
    with open(csvpath, 'r') as file_handler:
         headerline = file_handler.next()
    candidates = x
    for x in csv.reader(file_handler):
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print ("Candidates: ", candidates)

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.

