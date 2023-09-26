import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')
analysis = os.path.join("analysis", "poll_analysis_result.txt")
election_results = {}
candidate = []


with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        candidate_name = row[2]
        if candidate_name not in candidate:
            candidate.append(candidate_name)
            election_results[candidate_name] = 0
        election_results[candidate_name] += 1


vote_totals = sum(election_results[item] for item in election_results)
vote_list = [*election_results.values()]
ccs = (vote_list[0]) / vote_totals * 100
dd = (vote_list[1]) / vote_totals * 100
rad = (vote_list[2]) / vote_totals * 100
winner = max(ccs, dd, rad)

if winner == ccs:
    winner = candidate[0]
if winner == dd:
    winner = candidate[1]
if winner == rad:
    winner = candidate[2]
output =(
f"Election Results\n"
f"-------------------------\n"
f"Total Votes: {vote_totals}\n"
f"-------------------------\n"
f"{candidate[0]}: {ccs:.3f}% ({vote_list[0]})\n"
f"{candidate[1]}: {dd:.3f}% ({vote_list[1]})\n"
f"{candidate[2]}: {rad:.3f}% ({vote_list[2]})\n"
f"-------------------------\n"
f"Winner: {winner}\n"
f"-------------------------"
)
print(output)

with open(analysis, "w") as resultsEnd:
    resultsEnd.write(output)






