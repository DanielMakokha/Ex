# Initialize a variable to store the sum of scores
score_sum = 0

# Initialize a variable to store the highest and lowest scores
highest_score = -1
lowest_score = 101

# Initialize a variable to store the second highest score
second_highest_score = -1

# Initialize a variable to store if a score over 100 was entered
over_100_entered = False

# Prompt the user to enter 10 test scores
for i in range(10):
    score = int(input("Enter test score: "))
    score_sum += score
    if score > highest_score:
        highest_score = score
    if score < lowest_score:
        lowest_score = score
    if score > 100:
        over_100_entered = True
    if score > second_highest_score and score < highest_score:
        second_highest_score = score

# Print the highest and lowest scores
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)

# Print the average of the scores
average = score_sum/10
print("Average of the scores:", average)

# Print the second largest score
print("Second highest score:", second_highest_score)

# Print a warning message if a score over 100 was entered
if over_100_entered:
    print("Warning: A score over 100 was entered.")

# sort the score and drop the lowest two scores
scores_sorted = sorted(scores)
scores_sorted = scores_sorted[2:]

# calculate the average of the remaining scores
average_remaining = sum(scores_sorted)/(10-2)

# Print the average of the remaining scores
print("Average of the remaining scores:", average_remaining)
