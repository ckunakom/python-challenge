# Import modules for reading CSV file
import os
import csv

# Path to collect data from the Resources folder
pybankpath = os.path.join('Resources', 'budget_data.csv')

# Define a list for counting month and adding profit/loss variables
months = []
# Define a list to store individual change in profit/loss
change = []

# My starting profit/loss
profitloss = 0
# Start for calculating the change it profit/loss
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
        profitloss = profitloss + int(row[1])

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
    # Total month with all the changes in profit/loss (-1 b/c no change in first date)
    monthschange = total_months - 1 
    # Setting up to find the greatest increase/decrease over entire period
    great_inc = 0
    great_dec = 0

    # Start looping through the change list to...
   
    for x in change:
        
        # Sum up all the changes in profit/loss one by one
        total_change = total_change + x

        # Getting the max and min profit        
        if  x > great_inc:
            great_inc = x
        #
        elif x < great_dec:
            great_dec = x

    # The average of the changes in "Profit/Losses" over the entire period
    average_change = total_change/monthschange

    # Find the index of the greatest increase date in profit/loss
    inc_index = change.index(great_inc)
    # Get the index to call for the date with the greatest increase 
    inc_date = inc_index + 1
    # The greatest increase in profits (date and amount) over the entire period
    maxdate = months[inc_date]

    # Find the index of the greatest decrease in profit/loss
    dec_index = change.index(great_dec)
        # Get the index to call for the date with greatest decrease
    dec_date = dec_index + 1
    # The greatest decrease in losses (date and amount) over the entire period
    mindate = months[dec_date]

# print the analysis to the terminal and export a text file with the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${profitloss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {maxdate} (${great_inc})")
print(f"Greatest Decrease in Profits: {mindate} (${great_dec})")

# Specify path to the file to write to
pybanktxt = os.path.join('analysis', 'pybank.txt')

# Write in txt file
with open(pybanktxt, "w") as text_file:

    text_file.write(f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${profitloss}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {maxdate} (${great_inc})
Greatest Decrease in Profits: {mindate} (${great_dec})""")

    text_file.close()