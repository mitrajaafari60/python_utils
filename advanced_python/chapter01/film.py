genres = ['Horror', 'Romance', 'Comedy', 'History', 'Adventure', 'Action']
votes = {}

# Initialize vote counts for each genre
for genre in genres:
    votes[genre] = 0

# Read the number of people
num_people = int(input())

# Read the names and genres of each person
for _ in range(num_people):
    person = input().split()
    name = person[0]
    person_genres = person[1:]

    # Update vote counts for each genre
    for genre in person_genres:
        if genre in votes:
            votes[genre] += 1

# Sort and print the genres based on vote counts
sorted_genres = sorted(votes.items(), key=lambda x: (-x[1], x[0]))

for genre, count in sorted_genres:
    print(f"{genre} : {count}")
