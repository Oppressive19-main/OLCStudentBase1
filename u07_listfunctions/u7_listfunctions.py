

# Python List Exercises: Student Names and Scores
#
# Scenario:
# You have 2 separate lists.
# One list stores student names.
# The other list stores the corresponding scores.
#
# The score at each index belongs to the student name at the same index.
#
# Example:
# names[0] matches scores[0]
# names[1] matches scores[1]
#
# Use the sample lists below for the questions.

names = [
    "Aiden", "Bella", "Charlie", "Daphne", "Ethan", "Fiona", "Grace", "Henry",
    "Isaac", "Jasmine", "Kai", "Lydia", "Mason", "Nora", "Owen", "Priya",
    "Quentin", "Rachel", "Samuel", "Tina", "Uma", "Victor", "Wendy", "Xavier",
    "Yvonne", "Zach", "Aaron", "Bianca", "Caleb", "Denise"
]

scores = [
    78, 92, 85, 92, 67, 88, 75, 81,
    90, 73, 84, 95, 69, 87, 58, 91,
    76, 83, 95, 64, 72, 89, 77, 68,
    94, 80, 61, 86, 74, 79
]


# --------------------------------------------------
# PART 1: Basic list access and membership
# --------------------------------------------------

# Q1
# Print the full names list using a for loop.

# Q2
# Print the full scores list using a for loop.

# Q3
# Print the first student name in the list.

# Q4
# Print the last score in the list.

# Q5
# Find out whether "Charlie" exists in the names list.
# Print True or False.

# Q6
# Ask the user to enter a student name.
# Check whether that student exists in the names list.
# Print "Student found" or "Student not found".


# --------------------------------------------------
# PART 2: Finding positions and matching data
# --------------------------------------------------

# Q7
# Find the index position of "Daphne" in the names list.
# Print the index.

# Q8
# Find Charlie's score by first finding Charlie's index in the names list.
# Then use that same index to get the score from the scores list.

# Q9
# Ask the user to enter a student name.
# If the student exists, print that student's score.
# If not, print "Student not found".

# Q10
# Print every student's name together with their score.
# Example output:
# Aiden : 78
# Bella : 92
# Charlie : 85


# --------------------------------------------------
# PART 3: Working with highest and lowest values
# --------------------------------------------------

# Q11
# Find the highest score in the scores list.
# Print the highest score only.

# Q12
# Find the lowest score in the scores list.
# Print the lowest score only.

# Q13
# Find the name of the student who scored the highest mark.
# Assume there is only one highest scorer for now.

# Q14
# Find the name of the student who scored the lowest mark.
# Assume there is only one lowest scorer for now.

# Q15
# Print a sentence like this:
# "Bella scored the highest mark of 92."


# --------------------------------------------------
# PART 4: Handling ties
# --------------------------------------------------

# Q16
# In the current list, there are 2 students with the highest score.
# Find the highest score first.
# Then print all student names who got that highest score.

# Q17
# Print the result in this format:
# "Top scorer(s): Lydia, Samuel with 95 marks."

# Q18
# Find all students who got the lowest score.
# Print their names and the score.

# Q19
# Count how many students got the highest score.
# Print the number.

# Q20
# Count how many students scored above 80.


# --------------------------------------------------
# PART 5: Searching and filtering
# --------------------------------------------------

# Q21
# Create a new list that stores the names of students who scored above 80.
# Print the new list using a for loop.

# Q22
# Create a new list that stores the names of students who failed.
# Assume fail means score below 50.
# Print the new list using a for loop.

# Q23
# Create a new list that stores the scores of students whose names start with the letter "B" or "D".

# Q24
# Ask the user to enter a min_score and a max_score
# Print all student names who are within the range of the min and max score.

# Q25
# Ask the user to enter a student name.
# Print whether the student passed or failed.
# Assume pass mark is 50.
