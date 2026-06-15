###########################################################
# Part 3. IN-CLASS Practice Exercises For loops
#
# Focus: Python for-loops (range, strings, lists, dicts, indexes)
###########################################################


#------------------------------------------------------------
# Exercise 1: Count Up with range(stop)
# Print the numbers 0 to 9 
# Use: range(10)
# Bonus Challenge: Print on one line, separated by spaces.

# Example: Output = 0 1 2 3 4 5 6 7 8 9
# for i in range(10):
#     print(i)




#------------------------------------------------------------
# Exercise 2: Count Down with range(start, stop, step)
# Print 10 down to 1 
# Bonus Challenge: Print on one line, separated by spaces.
# Example: Output = 10 9 8 7 6 5 4 3 2 1

# range(10, 0, -1)

# for i in range(10,0,-1):
#  print(i)




#------------------------------------------------------------
# Exercise 3: Evens in a Range
# Print all even numbers from 2 to 20.
# Bonus Challenge: Print on one line, separated by spaces.
# Example: Output = 2 4 6 8 10 12 14 16 18 20
for i in range(2,21,2):
    print(i)  




#------------------------------------------------------------
# Exercise 4: Multiples with Steps
# Print the first 6 multiples of 9.
# Use: range(start, stop, step) where step = 9
# Tip: Think about where to stop so you get 6 numbers.
# Example: Output = 9 18 27 36 45 54
for i in range (9,55,9):
    print(i)




#------------------------------------------------------------
# Exercise 5: Running Total (Accumulator)
# Compute the sum of all integers from 1 to 100 (inclusive) and print it.
# Use: range(1, 101)
# Example: Output = 5050
nums = [55, 66, 77, 45,87, 96, 34, 85]
total= sum(nums)

total = 0

for i in nums:

   total = total +1
# print(total)

#find the average of all the numbers in the list
num_items_in_list = len(nums)
average = total / num_items_in_list
#------------------------------------------------------------
# Exercise 6: Sum of Multiples
# Compute the sum of multiples of 3 from 3 to 30 (inclusive).
# Use: range(3, 31, 3)
# Example: Output = 165

total = 0
for i in range(3,31,3):
    total = total + i
print(total)


#------------------------------------------------------------
# Exercise 7: Loop Through a String (characters)
# Count the vowels in the string and print the total.
# Data:
# text = "Computhink Academy"
# Vowels: a, e, i, o, u (case-insensitive)
# Example: Output = 7
text = "Computhink Academy"
vowels = ['a','e','i','o','u']
vcount = 0 

for char in text: # looping through every single character
   
    if char.lower() in vowels:
        vcount += 1
   
# print(vcount)



#------------------------------------------------------------
# Exercise 8: Loop Through a String Using Index
# Print each character with its index in the format: index:char
# Data:
name = "Python"
# Example: 
# 0:P
# 1:y
# 2:t
# 3:h
# 4:o
# 5:n

word_length = len(name) # 6

for i in range(word_length): # 0 1 2 3 4 5

    print(f"{i} : {name[i]}")

for i in range(6):
   
    print(name[k])
    k += 1




#------------------------------------------------------------
# Exercise 9: Every 2nd Character (Index Step)
# Print every 2nd character (positions 0, 2, 4, ...) of the string on one line (no spaces).
# Data:
# s = "abcdefghijkl"
# Example: Output = acegik






#------------------------------------------------------------
# Exercise 10: Loop Through a List (values)
# Print the squares of all numbers in the list on one line, separated by spaces.
# Data:
# nums = [3, 1, 4, 1, 5, 9]
# Example: Output = 9 1 16 1 25 81





#------------------------------------------------------------
# Exercise 11: Loop Through a List Using Index
# Replace every negative number in the list with 0, then print the updated list.
# Data:
# data = [5, -2, 7, -9, 0, 4]
# Expected final list: [5, 0, 7, 0, 0, 4]





#------------------------------------------------------------
# Exercise 12: Manual Max (No max())
# Find and print the largest number in the list without using max().
# Data:
# scores = [42, 67, 23, 88, 55, 88, 12]
# Example: Output = 88
scores = [42, 67, 23, 88, 55, 88, 12]



#------------------------------------------------------------
# Exercise 13: Loop through a List (index + value)
# Print each item with a 1-based index like "1) apple", "2) banana", ...
# Data:
# fruits = ["apple", "banana", "cherry", "durian"]






#------------------------------------------------------------
# Exercise 14: Pair Two Lists 
# Print "Alice: 85", "Ben: 73", etc. by pairing names with marks.
# Data:
# names = ["Alice", "Ben", "Carmen", "Dylan"]
# marks = [85, 73, 91, 66]





#------------------------------------------------------------
# Exercise 15: Nested Loops – Times Table
# Print a 1–5 multiplication table with rows like:
# 1 2 3 4 5
# 2 4 6 8 10
# ...
# Use two for-loops (outer row 1..5, inner col 1..5).





#------------------------------------------------------------
# Exercise 16: Pattern Printing (Right Triangle)
# For n = 5, print:
# *
# **
# ***
# ****
# *****
# Use a for-loop and string multiplication.





#------------------------------------------------------------
# Exercise 17: Dictionary Iteration (keys & values)
# Print "Alice : 72" etc. for each pair in the dict.
# Data:
# grades = {"Alice":72, "Ben":65, "Chloe":88, "Dion":55}





#------------------------------------------------------------
# Exercise 18: Dictionary Aggregation
# Compute and print the average value in the dictionary (to 1 decimal place).
# Data:
# temps = {"Mon":31.2, "Tue":29.8, "Wed":30.5, "Thu":32.0, "Fri":31.0}
# Example: Output = 30.9





#------------------------------------------------------------
# Exercise 19: Filter from a Dictionary
# Print only the students who passed (score >= 50) in "Name (score)" format.
# Data:
# results = {"Amy":49, "Bao":77, "Chin":50, "Deepa":92, "Eun":38}
# Example:
# Bao (77)
# Chin (50)
# Deepa (92)




#------------------------------------------------------------
# Exercise 20: for-else Search
# Search for target in the list; print "Found at index i" or "Not found".
# Use for-else (else runs only if loop completes with no break).
# Data:
# items = ["id-001", "id-007", "id-010", "id-013"]
# target = "id-010"





#------------------------------------------------------------
# Exercise 21: Skip and Stop (continue / break)
# Loop through the string:
#  - Skip vowels (do not print them).
#  - Stop printing entirely if you meet an exclamation mark '!' (break).
# Data:
# msg = "Code smarter, not harder!"
# Expected printed output (no vowels, stop at '!'): Cd smtr, nt hrdr





#------------------------------------------------------------
# Exercise 22: Character Frequency (build a dict)
# Build and print a frequency dictionary {char: count} for letters only (ignore spaces).
# Treat uppercase and lowercase as the same.
# Data:
# line = "Better code, better life"
# Example (order may vary): {'b':2, 'e':6, 't':5, 'r':3, 'c':1, 'o':1, 'd':1, 'l':1, 'i':1, 'f':1}






#------------------------------------------------------------
# Exercise 23: Index Windows (String Slices by Loop)
# Print every 3-letter chunk of the string using indexes (i, i+3).
# Ignore the leftover if length is not a multiple of 3.
# Data:
# dna = "ATGCGATACGCTTGA"
# Example:
# ATG
# CGA
# TAC
# GCT
# TGA





#------------------------------------------------------------
# Exercise 24: Two-List Computation 
# Given costs and quantities, print "Item i: $TOTAL" per line and the grand total.
# Data:
# costs = [1.20, 0.80, 3.50, 2.00]
# qty   = [3,     5,    2,    1   ]
# Example lines:
# Item 1: $3.60
# Item 2: $4.00
# Item 3: $7.00
# Item 4: $2.00
# Grand Total: $16.60





#------------------------------------------------------------
# Exercise 25: Validate with for-loop (All Digits)
# Check if a string consists only of digits (0–9) using a for-loop.
# You cannot use .isdigit()
# Data:
# token = "A12345"
# Print True or False accordingly (no .isdigit()).





#------------------------------------------------------------
# Exercise 26: Build a New List 
# From the list, build a new list containing only the positive even numbers, then print it.
# Data:
# nums = [-3, -2, 0, 1, 2, 3, 4, 11, 12]
# Expected: [2, 4, 12]


#------------------------------------------------------------