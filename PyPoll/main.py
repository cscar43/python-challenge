#importing the fuctions to running the analysis
import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

# Open the CSV file
with open(election_csv, 'r') as csvfile:
    
     # Use the CSV reader to read the file
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
     # Initialize variables to store the data we're interested in
    total_votes = 0
    candidates = {}
    winner = ''
    winner_votes = 0
    
    # Loop through each row of the CSV file
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
         # Calculate the change in votes by candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
            
         # Specify the path to the output file inside the 'analysis' folder
        output_file = os.path.join('analysis', 'election_analysis.txt')
    
    # Write the results to a txt file
    with open(output_file, 'w') as output_file:
        output_file.write('Election Results\n')
        output_file.write('-------------------------\n')
        output_file.write(f'Total Votes: {total_votes}\n')
        output_file.write('-------------------------\n')
        
        # Updates the candidate vote count and declares the winner based on who collected the most votes
        for candidate, votes in candidates.items():
            percentage = round((votes / total_votes) * 100, 3)
            output_file.write(f'{candidate}: {percentage}% ({votes})\n')
            if votes > winner_votes:
                winner = candidate
                winner_votes = votes
        output_file.write('-------------------------\n')
        output_file.write(f'Winner: {winner}\n')
        output_file.write('-------------------------\n')  
            
        #Prints out in Terminal when the code is ran
        print('Election Results')
        print('---------------------------')
        print(f'(Total Votes: {total_votes})')
        print('---------------------------')
        
        # Updates the candidate vote count and declares the winner based on who collected the most votes
        for candidate, votes in candidates.items():
            percentage = round((votes/total_votes)*100, 3)
            print(f'{candidate}: {percentage}% ({votes})')
        print('---------------------------')            
        print(f'Winner: {winner}')
        print('---------------------------')