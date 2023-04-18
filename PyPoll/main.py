import csv

# Open the CSV file and create a CSV reader
with open('election_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    next(reader)

    # Initialize variables to store the votes and total votes
    votes = []
    total_votes = 0

    # Loop through the rows in the CSV file
    for row in reader:
        # Extract the voter ID and candidate name from the row
        voter_id = int(row[0])
        candidate = row[2]

        # Add the vote to the list of votes
        votes.append({"voter_id": voter_id, "candidate": candidate})

        # Increment the total vote count
        total_votes += 1

    # Create a dictionary to keep track of the total number of votes each candidate won
    votes_per_candidate = {}

    # Loop through the list of votes
    for vote in votes:
        candidate = vote["candidate"]
        # Check if the candidate is already in the dictionary
        if candidate in votes_per_candidate:
            # If the candidate is already in the dictionary, increment their vote count
            votes_per_candidate[candidate] += 1
        else:
            # If the candidate is not yet in the dictionary, add them with an initial vote count of 1
            votes_per_candidate[candidate] = 1

    # Create a list of all the candidates who received votes
    candidates = list(votes_per_candidate.keys())

    # Create a dictionary to keep track of the percentage of votes each candidate won
    vote_percentages = {}

    # Loop through the list of candidates and calculate their vote percentage
    for candidate in candidates:
        vote_percentage = (votes_per_candidate[candidate] / total_votes) * 100
        vote_percentages[candidate] = vote_percentage

    # Find the candidate with the most votes (i.e., the winner of the election)
    winner = max(votes_per_candidate, key=votes_per_candidate.get)

    # Print the results
with open("elections.txt", "a") as f:
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print(f"Total Votes: {total_votes}", file=f)
    print("-------------------------", file=f)
    for candidate in candidates:
        print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({votes_per_candidate[candidate]})", file=f)
    print("-------------------------", file=f)
    print(f"Winner: {winner}", file=f)
    print("-------------------------", file=f)
