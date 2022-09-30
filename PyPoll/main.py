# dependencies
import os
import csv

# function to append data to file
def create_csv(line):
  # specify location and file name to write data
  output_path = os.path.join('analysis','poll_results.csv')
  
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

# summarize poll data from election_data.csv and find winner
# set path to file
poll_csv = os.path.join('Resources','election_data.csv')

# open file using read mode and specify variable to store object
with open(poll_csv, newline='') as f:
  
  # initialize reader
  reader = csv.reader(f, delimiter=',')

  # read in headers and exclude from results
  poll_header = next(reader)
  
  # save data to list
  poll = list(reader)
  
# count number of votes and print to terminal and file
total_votes = len(poll)
print_all(['Election Results'])
print_all(['---------------------------------'])
print_all([f'Total Votes: {total_votes}'])
print_all(['---------------------------------'])
  
# create set to store unique candidates and save to variable
candidates = set()
  
# iterate through poll data
for row in poll:
    
  # if candidate's name is not in set, add to set
  if row[2] not in candidates:
    candidates.add(row[2])
  
# initialize variables to help identify winning candidate
max_votes = 0
winner = ''
  
# iterate through set of candidates
for candidate in candidates:
    
  # initialize initial count of votes for each candidate to 0
  vote_count = 0
    
  # tally each vote for the candidate
  for row in poll:
    if candidate == row[2]:
      vote_count += 1
    
  # if the votes for the candidate is greater than the stored value of max_votes
  # tag the candidate as the winner (so far) and update the number of max_votes
  if vote_count > max_votes:
    max_votes = vote_count
    winner = candidate
    
  # calculate the percentage of votes for the candidate
  vote_percent = round(vote_count / total_votes * 100, 3)
    
  # print candidate's results and print to terminal and file
  print_all([f'{candidate}: {vote_percent}% ({vote_count})'])
  
# print overall winner to terminal and file
print_all(['---------------------------------'])
print_all([f'Winner: {winner}'])
print_all(['---------------------------------'])