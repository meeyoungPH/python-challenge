# CSV Data Analysis with Python

This project demonstrates data summarization using Python for two different datasets with financial data and poll data respectively.

## Libraries
* os
* csv

## Poll Data (PyPoll)
Python is used to tally votes based on poll data from a small, rural town to help determine the winner.

### Data
This dataset contains three columns in a file called [election_data.csv](PyPoll/Resources/election_data.csv).
* BallotID
* County
* Candidate

#### Excerpt
![poll_data_excerpt](PyPoll/Resources/poll_data_excerpt.PNG)

### Analysis
The following calculations are conducted using this poll data:
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.

### Approach
#### Data Preparation
* The data are read in using the csv and os libraries.
* The header is stored and excepted from calculations using the next function.
* The poll data is stored to a list for ease of iteration.
#### Calculations
* Total Votes: The number of total votes is determined by using the len function to find the length of the list storing the poll data (minus the header row).
* Unique Candidates: A set is created to store the unique list of candidates. A for loop iterates through the list containing the poll data to compare the candidate's name to any stored in the set. If the name is missing, it is added to the set.
* Vote Counts per Candidate: Once the set of unique candidates is complete, another for loop iterates through each candidate. A nested for loop matches names in the poll data and increments the vote count accordingly.
* Winner: After the nested loop completes, if the count for the candidate is greater than the stored value of maximum votes for a candidate (initially set to 0), then the candidate and their number of votes is stored as the potential winner. The ultimate winner is decided after all for loops have completed their runs.
* Vote Percentage: Once the votes have been tallied for the candidate, the vote percentage is calculated by dividing the vote count by the total number of votes, multiplied by 0 and rounded to 3 decimal points.
#### Printing
* Printing to the terminal and to the csv file is handled by two separate functions.
* The first function, create_csv(), appends new lines to a csv file in the analysis folder under the name [poll_results.csv](PyPoll/analysis/poll_results.csv).
* The second function, print_all(), prints data, text, and formatting generated in the script to the terminal using the print function and the csv file by calling the create_csv() function. Formatted statements with data is passed to this function in a list as values are calculated.

