import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

election_results = {}
candidate = []
winning_candidate = ""
winning_votes = 0
winning_percentage = 0
total_votes = 0

with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate not in candidate_name:
            candidate.append(candidate_name)
            election_results[candidate_name] = 0
        election_results[candidate_name] += 1





#     # Loop through the data
#     for row in csvreader:
#         vote = row[2] 
#         if vote in election_results.keys(): 
#             election_results[vote]=election_results[vote] +1
        
#         else:
#             election_results[vote]= 1
            

print([election_results])



# ccs = election_results[int('Charles Casper Stockham')]
# print(ccs)

# dd = election_results[int('Diana DeGette')]
# print(dd)

# rad = election_results[int('Raymon Anthony Doane')]
# print(rad)

# print(sum(ccs + dd + rad))



