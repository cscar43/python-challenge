#importing the fuctions to running the analysis
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Open the CSV file
with open(budget_csv, 'r') as csvfile:

    # Use the CSV reader to read the file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(csvreader) 
    
    # Initialize variables to store the data we're interested in
    num_months = 0
    total_profit_loss = 0
    previous_profit_loss = None
    profit_loss_changes = []
    max_increase_date = None
    max_increase_amount = 0
    max_decrease_date = None
    max_decrease_amount = 0
    
    # Loop through each row of the CSV file
    for row in csvreader:
        
        # Increment the number of months
        num_months += 1
        
        # Add the profit/loss to the total
        total_profit_loss += int(row[1])
        
        # Calculate the change in profit/loss from the previous month
        if previous_profit_loss is not None:
            change = int(row[1]) - previous_profit_loss
            profit_loss_changes.append(change)
            
            
            # Update the maximum increase and decrease values
            if change > max_increase_amount:
                max_increase_amount = change
                max_increase_date = row[0]
            elif change < max_decrease_amount:
                max_decrease_amount = change
                max_decrease_date = row[0]
        
        # Set the previous profit/loss to the current value
        previous_profit_loss = int(row[1])
     
    # Calculate the average change in profit/loss   
    avg_profit_loss_change = sum(profit_loss_changes)/len(profit_loss_changes)
    
    # Specify the path to the output file inside the 'analysis' folder
    output_path = os.path.join('analysis', 'budget_analysis.txt')
    
    # Write the results to a txt file
    with open(output_path, 'w') as output_file:
        output_file.write(f"Total Months: {num_months}\n")
        output_file.write(f"Total Profit/Loss: {total_profit_loss}\n")
        output_file.write(f"Average Change in Profit/Loss: {round(avg_profit_loss_change, 2)}\n")
        output_file.write(f"Greatest Increase in Profits: {max_increase_date} ({max_increase_amount})\n")
        output_file.write(f"Greatest Decrease in Profits: {max_decrease_date} ({max_decrease_amount}\n")
    
    #Prints out in Terminal when the code is ran
    print(f"Total Months: {num_months}")
    print(f"Total Profit/Loss: {total_profit_loss}")
    print(f"Average Change in Profit/Loss: {round(avg_profit_loss_change, 2)}")
    print(f"Greatest Increase in Profits: {max_increase_date} ({max_increase_amount})")
    print(f"Greatest Decrease in Profits: {max_decrease_date} ({max_decrease_amount})")