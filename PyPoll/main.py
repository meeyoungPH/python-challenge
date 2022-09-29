# dependencies
import os
import csv

# set path to file
poll_csv = os.path.join('Resources','election_data.csv')

with open(poll_csv, newline='') as f:
  reader = csv.reader(f, delimiter=',')

  # read in headers and exclude from results
  poll_header = next(reader)
  
  # save data to list
  poll = list(reader)
  #print(poll[:5])
  
  # count number of votes
  votes = len(poll)
  print('Election Results')
  print('---------------------------------')
  print(f'Total Votes: {votes}')
  print('---------------------------------')
  
  # identify unique candidates
  candidates = set()
  
  for row in poll:
    if row[2] not in candidates:
      candidates.add(row[2])
  
  # set values for starting variables to help identify winning candidate
  max_votes = 0
  winner = ''
  
  # iterate through list of candidates
  for each in candidates:
    
    # set subtotal of votes for each candidate to 0
    subtotal = 0
    
    # tally each vote for the candidate
    for row in poll:
      if each == row[2]:
        subtotal += 1
    
    # if the subtotal of votes for the candidate is greater than the stored value of max_votes
    # identify as the current winning candidate and update the max_vote value
    if subtotal > max_votes:
      max_votes = subtotal
      winner = each
    
    # calculate the percentage of votes for the candidate
    vote_percent = round(subtotal / votes * 100, 3)
    
    # print candidate's results
    print(f'{each}: {vote_percent}% ({subtotal})' )
  
  # print overall winner
  print('---------------------------------')
  print(f'Winner: {winner}')
  print('---------------------------------')