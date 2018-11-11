#Import os module
import os

#Module for reading CSV file
import csv
import numpy as np


#path to csv file in directory
csvpath = os.path.join('/Users/mary/anaconda3/envs/tuesday_pandas/python-challenge/PyBank/budget_data.csv')

# write data to file
f = open("PyBank.text", "w")

#The total number of months included in the dataset
with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler,delimiter = ",")
    data = list(reader)
    row_count = len(data)-1
    print >>f, "Total Months: ", row_count
    print ("Total Months: ", row_count)

#The total net amount of "Profit/Losses" over the entire period
with open(csvpath, 'r') as file_handler:
    headerline = file_handler.next()
    total = 0
    for row in csv.reader(file_handler):
        total += int(row[1])
    print >>f, "Total: $", total
    print ("Total: $", total)

#The average change in "Profit/Losses" between months over the entire period
with open(csvpath, 'r') as file_handler:
    headerline = file_handler.next()
    sum_of_changes = 0
    prev_amount = None
    for row in csv.reader(file_handler):
        if prev_amount is None:
            prev_amount = int(row[1])
            pass
        sum_of_changes += int(row[1]) - prev_amount
        prev_amount = int(row[1])

    print >>f, "Average: $", (sum_of_changes/(row_count-1))
    print ("Average: $", (sum_of_changes/(row_count-1)))

#The greatest increase in profits (date and amount) over the entire period
with open(csvpath, 'r') as file_handler:
    headerline = file_handler.next()
    prev_amount = None
    greatest_increase = 0
    for row in csv.reader(file_handler):
        if prev_amount is None:
            prev_amount = int(row[1])
            pass

        increase = int(row[1]) - prev_amount
        if increase > greatest_increase:
            greatest_increase = increase
            greatest_row = row

        prev_amount = int(row[1])


    print >>f, "Greatest Increase: in Profits ", greatest_row[0], greatest_increase
    print ("Greatest Increase: in Profits ", greatest_row[0], greatest_increase)

#The greatest decrease in losses (date and amount) over the entire period
with open(csvpath, 'r') as file_handler:
    headerline = file_handler.next()
    initial_amount = None
    greatest_decrease = 0
    for row in csv.reader(file_handler):
        if initial_amount is None:
            initial_amount = int(row[1])
            pass

        decrease = int(row[1]) - initial_amount
        if decrease < greatest_decrease:
            greatest_decrease = decrease
            greatest_rows = row

        initial_amount = int(row[1])


    print >>f, "Greatest Decrease in Profits: ", greatest_rows[0], greatest_decrease
    print ("Greatest Decrease in Profits: ", greatest_rows[0], greatest_decrease)

f.close()