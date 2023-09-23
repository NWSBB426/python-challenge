import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #print(header)
    list_changes=[]
    list_of_months=[]
    greatest_increase=["", 0]
    greatest_decrease=["", 0]
 
    #Total number of Months 
    rowcount = 0
    total_profit_loss = 0
    first_row=next(csvreader)
    rowcount+= 1
    total_profit_loss += int(first_row[1])
    pmonth=int(first_row[1])
    #print(first_row)
    


    # Loop through the data to count the number of months
    for row in csvreader:
        rowcount+= 1
        total_profit_loss += int(row[1])
        change= int(row[1])-pmonth
        list_changes.append(change)
        list_of_months.append(row[0])
        pmonth=int(row[1])
        if change > greatest_increase[1]:
            greatest_increase[0]= row[0]
            greatest_increase[1]= change
       
        if change < greatest_decrease[1]:
            greatest_decrease[0]= row[0]
            greatest_decrease[1]= change
        #print(row)
    print('Financial Analysis')
    print('----------------------------')
    print('Total Months: ', rowcount)
    print('Total: ',"$",total_profit_loss)
    
    avg_change= sum(list_changes)/len(list_changes)
    print('Average Change: ', avg_change)
    print('Greatest Increase in Profits: ', str(greatest_increase))
    print('Greatest Decrease in Profits: ', greatest_decrease)

    


 