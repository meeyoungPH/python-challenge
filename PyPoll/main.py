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
  #poll_summary = []
  candidates = set()
  
  for row in poll:
    if row[2] not in candidates:
      candidates.add(row[2])
  
  max_votes = 0
  winner = ''
  
  for each in candidates:
    subtotal = 0
    
    for row in poll:
      if each == row[2]:
        subtotal += 1
    
    if subtotal > max_votes:
      max_votes = subtotal
      winner = each
    
    vote_percent = round(subtotal / votes * 100, 3)
    print(f'{each}: {vote_percent}% ({subtotal})' )
  
  print('---------------------------------')
  print(f'Winner: {winner}')
  print('---------------------------------')
    
    
    
  
  
  
#def tally_candidate_votes():
  
  
# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# Your analysis should look similar to the following:

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.