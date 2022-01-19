import os
import csv
import pathlib

csv_path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'Resources', "election_data.csv")

Election_Analysis = []
voters = []
candidates = []
candidate_list = []
Khan = 0
Correy = 0
Li = 0
OTooley = 0

with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader, None)
    for row in csv_reader:
        voters.append(row[0])
        candidates.append(row[2])
        total_votes = len(voters)
    for i in candidates:
        if i not in candidate_list:
            candidate_list.append(i)
        elif i == "Khan":
            Khan = Khan + 1
        elif i == "Correy":
            Correy = Correy + 1
        elif i == "Li":
            Li = Li + 1
        elif i == "O'Tooley":
            OTooley = OTooley + 1
    Khan_percentage = Khan/total_votes
    Correy_percentage = Correy/total_votes
    Li_percentage = Li/total_votes
    OTooley_percentage = OTooley/total_votes

Election_Analysis = [Khan, Correy, Li, OTooley]
Election_Percentage = [Khan_percentage, Correy_percentage, Li_percentage, OTooley_percentage]
Winner = max(Election_Analysis)


Election_Results = os.path.join("Election_Results.txt")
with open(Election_Results, 'w', newline="") as datafile:
    csvWriter = csv.writer(datafile)
    csvWriter.writerow(["Election Results"])
    csvWriter.writerow(["----------------------------"])
    csvWriter.writerow(["Total Votes: " + str(total_votes)])
    csvWriter.writerow(["----------------------------"])
    csvWriter.writerow(["Khan: " + str(round(Khan_percentage*100, 0)) + "%" + " (" + str(Khan) + ")"])
    csvWriter.writerow(["Correy: " + str(round(Correy_percentage*100, 0)) + "%" + " (" +  str(Correy) + ")"])
    csvWriter.writerow(["Li: " + str(round(Li_percentage*100, 0)) + "%" + " (" + str(Li) + ")"])
    csvWriter.writerow(["O'Tooley: " + str(round(OTooley_percentage*100, 0)) + "%" + " (" + str(OTooley) + ")"])
    csvWriter.writerow(["----------------------------"])
    csvWriter.writerow(["Winner: " + str(candidate_list[Election_Analysis.index(max(Election_Analysis))])])
    csvWriter.writerow(["----------------------------"])

Election_Analysis = [Khan_percentage, Correy_percentage, Li_percentage, OTooley_percentage]
Winner = max(Election_Analysis)

print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------")
print("Khan: " + str(round(Khan_percentage*100, 0)) + "% " + "(" + str(Khan) + ")")
print("Correy: " + str(round(Correy_percentage*100, 0)) + "% " + "(" + str(Correy) + ")")
print("Li: " + str(round(Li_percentage*100, 0)) + "% " + "(" + str(Li) + ")")
print("O'Tooley: " + str(round(OTooley_percentage*100, 0)) + "% " + " (" + str(OTooley) + ")")
print("----------------------------")
print("Winner: " + str(candidate_list[Election_Analysis.index(max(Election_Analysis))]))
print("----------------------------")
