# Import modules for reading CSV file
import os
import csv

# Path to collect data from the Resources folder
pybankpath = os.path.join('Resources', 'budget_data.csv')

# Define a list for counting month and adding profit/loss variables
months = []
monthpfl = [] # - pfloss change
proflos = 0

# still figuring out changes - pfloss change
x = 0


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
        # Store the values of profit/loss in each month in a list - pfloss change
        monthpfl.append(row[1])

        # Start adding all the profit/loss
        # The net total amount of profit/loss over the entire period
        proflos = proflos + int(row[1])

        # Calculate the changes between each row - pfloss change
        
        x = int(row[1]) - x
      

    print(monthpfl)    
    # The total number of months included in the dataset
    total_months = len(months)
    # lastmonth_ind = total_months - 1
    # average_change = changes/total_months

    # print(average_change)



# # The average of the changes in "Profit/Losses" over the entire period - pfloss
#     first_pl = int(monthpfl[0])

#     last_pl = int(monthpfl[lastmonth_ind])
#     change = last_pl - first_pl
#     avg_change = change/total_months 
#     print(avg_change)

# The greatest increase in profits (date and amount) over the entire period
    # if 

# The greatest decrease in losses (date and amount) over the entire period




# print the analysis to the terminal and export a text file with the results

# outputpath = os.path.join('analysis', 'pybank_analysis.txt)

# with open(outputpath,"w") as text:  
#     # This stores a reference to a file stream
#     print(text)

#     # Store all of the text inside a variable called "lines"
#     lines = text.write()

#     # Print the contents of the text file
#     print(lines)


# print("Financial Analysis")
# print("----------------------------")
# print(f"Total Months: {total_months}")
# print(f"Total: ${proflos}")
# print(f"Average Change: ${avg_change}")
# print("Greatest Increase in Profits: {} (${}")
# print("Greatest Decrease in Profits: {} (${}")

