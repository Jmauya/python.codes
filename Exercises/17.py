# A list of numeric scores
scores = [45, 82, 94, 61, 55, 70, 88]

# Create an empty list to store high scores
passing_scores = []

# Loop through each score to filter out anything below 60
for score in scores:
    if score >= 60:
        passing_scores.append(score)

print("Passing Scores:", passing_scores)
# Output: Passing Scores: [82, 94, 61, 70, 88]
