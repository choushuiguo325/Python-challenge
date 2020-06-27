import csv

total = 0
total_vote = []
individual_vote = 0
candidate_name = []
candidate_percent = []
candidate_vote = []

path2 = "election_data.csv"
with open(path2) as csvfile2: 
    csvreader2 = csv.reader(csvfile2,delimiter=",")
    csv_header = next(csvfile2)
    
    # calculate the total vote: 
    for row in csvreader2: 
        total = total + 1
        total_vote.append(row[2])
        # proceed only if the candidate is not in the existing candidate list: 
        if row[2] not in candidate_name:
            # add name
            candidate_name.append(row[2])

    for candidate in candidate_name: 
        for name in total_vote:
            # if candidate's name in two list are the same: 
            if candidate == name:
                individual_vote = individual_vote + 1
        # add vote amount
        candidate_vote.append(individual_vote)
        individual_vote = 0

    candidate_percent = ["{:.3%}".format(i/total) for i in candidate_vote]
    a = len(candidate_name)
    b = candidate_vote.index(max(candidate_vote))

    # output in the terminal
   
    print("Election Results")
    print("-----------------------")
    print(f"Total Votes = {len(total_vote)}")
    print("-----------------------")
    for i in range(a-1):
        print(f"{candidate_name[i]}:{candidate_percent[i]} ({candidate_vote[i]})")
    print("-----------------------")
    print(f"Winner:{candidate_name[b]}")
    print("-----------------------")

    # write the output to the text file: 

    print("Election Results",file= open("PyPoll Analysis.txt", "a"))
    print("-----------------------",file= open("PyPoll Analysis.txt", "a"))
    print(f"Total Votes = {len(total_vote)}",file= open("PyPoll Analysis.txt", "a"))
    print("-----------------------",file= open("PyPoll Analysis.txt", "a"))
    a = len(candidate_name)
    for i in range(a-1):
        print(f"{candidate_name[i]}:{candidate_percent[i]} ({candidate_vote[i]})",file= open("PyPoll Analysis.txt", "a"))
    print("-----------------------",file= open("PyPoll Analysis.txt", "a"))
    b = candidate_vote.index(max(candidate_vote))
    print(f"Winner:{candidate_name[b]}",file= open("PyPoll Analysis.txt", "a"))
    print("-----------------------",file= open("PyPoll Analysis.txt", "a"))




        
