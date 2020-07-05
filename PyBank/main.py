# Import modules for reading CSV file
import os
import csv

# Path to collect data from the Resources folder
pybankpath = os.path.join('Resources', 'budget_data.csv')

# Define the function to pring out the anaylsis
def bank_analysis(total_months, profitloss, total_change):

    return "Financial Analysis" +\
        "\n----------------------------" +\
        f"\nTotal Months: {total_months}" +\
        f"\nTotal: ${profitloss}" +\
        f"\nAverage Change: ${average_change:.2f}" +\
        f"\nGreatest Increase in Profits: {maxdate} (${great_inc})" +\
        f"\nGreatest Decrease in Profits: {mindate} (${great_dec})"

# Define a list for counting month and adding profit/loss variables
months = []
# Define a list to store individual change in profit/loss
change = []

# My starting profit/loss
profitloss = 0
# Start for calculating the change in profit/loss
first_date = 0
value = 0

# Read in the CSV file
with open(pybankpath, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        
        # Start adding the month 1 by 1
        months.append(row[0])

        # Start adding all the profit/loss
        # The net total amount of profit/loss over the entire period
        profitloss += int(row[1])

    # There's no change in for the first month in the table, so...
        if first_date == 0:
            
            # Store the value of profit/loss of this first number in a variable
            value = int(row[1])
            
            # Save this first_date to be in the 'value' so the loop never comes to this if-statement again
            first_date = value
            
        else:
            
            # Calculate the the individual change by subtracting the current profit/loss from the previous profit/loss 
            individual_change = int(row[1]) - value 
            # Add this value to the change list
            change.append(individual_change)

            # Reset the variable to be the number of the current profit/loss
            value = int(row[1])
    
    # The total number of months included in the dataset
    total_months = len(months)

    # Setting up to sum up all the change in profit/loss
    total_change = 0
    
    # Setting up to find the greatest increase/decrease over entire period
    great_inc = 0
    great_dec = 0

    # Start looping through the change list to...
    for x in change:
        
        # Sum up all the changes in profit/loss one by one
        total_change += x

        # Getting the max and min profit        
        if  x > great_inc:
            great_inc = x
        #
        elif x < great_dec:
            great_dec = x

    # The average of the changes in "Profit/Losses" over the entire period (minus 1st date as there was no change)
    average_change = total_change/(total_months - 1)

    # Find the index of the greatest increase date in profit/loss, +1 since first date wasn't included in the list
    inc_index = change.index(great_inc) + 1
    # The greatest increase in profits (date and amount) over the entire period
    maxdate = months[inc_index]

    # Find the index of the greatest decrease in profit/loss, +1 since first date wasn't included in the list
    dec_index = change.index(great_dec) + 1
    # The greatest decrease in losses (date and amount) over the entire period
    mindate = months[dec_index]

# Save the result strings into the variable, so...
result_string = bank_analysis(total_months, profitloss, total_change)
print(result_string)

# Specify path to the file to write to
pybanktxt = os.path.join('analysis', 'pybank.txt')

# Write in txt file
with open(pybanktxt, "w") as text_file:

    # Call on the result_string and print to txt file w/o doing the calculations again
    text_file.write(result_string)

    text_file.close()