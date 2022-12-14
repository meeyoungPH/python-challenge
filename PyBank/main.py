# dependencies
import os
import csv
import statistics

# function to append data to file
def create_csv(line):
  # specify location and file name to write data
  output_path = os.path.join('analysis','budget_analysis.csv')
  
  # open file to append data
  with open(output_path, 'a', newline='') as f:
    
    # initialize csv.writer
    writer = csv.writer(f, delimiter=',')
    
    # write line to CSV
    writer.writerow(line)
    
# function to print to terminal and CSV synchronously
def print_all(line):
  print(line[0])
  create_csv(line)

# summarize financial data from budget_data.csv
# set path to file
budget_csv = os.path.join('Resources','budget_data.csv')

# open file using read mode and specify variable to store object
with open(budget_csv, newline='') as f:
  
  # initialize reader
  reader = csv.reader(f, delimiter=',')
  
  # read in headers and exclude from results
  header = next(reader)
  # print(header) # ['Date', 'Profit/Losses']

  # save data to list
  budget = list(reader)
  
# calculate months
months = len(budget)
  
# print total number of months
print_all(['Financial Analysis'])
print_all(['-------------------------------------'])
print_all([f'Total Months: {months}'])
  
# initialize variables for calculations
balance = 0
change_amounts = []
month_max_increase = ''
month_max_decrease = ''
max_increase = 0
max_decrease = 0

# iterate through budget data to calculate the change from month-to-month and maximum increases and decreases of that change
for i in range(len(budget)):

  # for loop to skip first row    
  if i > 0:
    
    # save previous and current profit/loss values and month
    previous = int(budget[i-1][1])
    current = int(budget[i][1])
    month = budget[i][0]
    
    # calculate change between current and previous profit/loss values and add to the change_amounts list
    change = current - previous
    change_amounts.append(change)
    
    # compare value of change to stored values for max_increase and max_decrease
    # update stored values for max_increase and max_decrease as well as the months if conditional criteria are met
    if change > max_increase:
      month_max_increase = month
      max_increase = change
    elif change < max_decrease:
      month_max_decrease = month
      max_decrease = change 
    
  # add profit/loss value to total budget after converting to integer
  balance += int(budget[i][1])

# print sum of the profit/losses column
print_all([f'Total: ${balance}'])

# calculate the average change from month-to-month
avg_change = round(statistics.mean(change_amounts),2)

# print the average change, month and value of greatest increase in profits and decrease in profits
print_all([f'Average Change: ${avg_change}'])
print_all([f'Greatest Increase in Profits: {month_max_increase} (${max_increase})'])
print_all([f'Greatest Decrease in Profits: {month_max_decrease} (${max_decrease})'])