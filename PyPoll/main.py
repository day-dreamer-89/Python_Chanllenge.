import csv

def calculate_election_results(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  

        total_votes = 0
        candidates = {}

        for row in reader:
            total_votes += 1

            candidate = row[2]

            if candidate in candidates:
                candidates[candidate] += 1
            else:
                candidates[candidate] = 1

        results = {}
        for candidate, votes in candidates.items():
            percentage = (votes / total_votes) * 100
            results[candidate] = (percentage, votes)

        winner = max(results, key=lambda x: results[x][1])

        print("Election Results")
        print("-------------------------")
        print(f"Total Votes: {total_votes}")
        print("-------------------------")
        for candidate, (percentage, votes) in results.items():
            print(f"{candidate}: {percentage:.3f}% ({votes})")
        print("-------------------------")
        print(f"Winner: {winner}")
        print("-------------------------")

# Example usage
csv_file_path = 'Resources/election_data.csv'
calculate_election_results(csv_file_path)
