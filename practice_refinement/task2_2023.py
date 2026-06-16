# A 2-player game is being programmed.
# The following program allows each player, in turn, to enter the names of 5 animals. 
# It converts the name of each animal to lower case. 
# Each animal entered by player 2 is their guess for the animal entered by player1.
	
# num_of_animals = 5
# for x in range(num_of_animals):
# 	p1_animal = input("Player 1, please enter an animal: ")
# 	p1_animal = p1_animal.lower()
# 	p2_guess = input("Player 2, please enter your guess: ")
# 	p2_guess = p2_guess.lower()
	
# Open the fie ANIMALGAME.py
# Save the file as ANIMAL_2023_<your name>_<centre number>_<index number>.py

#============================================================
# 1.	Edit the program to allow player 1 to keep entering animals until that player does not want to enter any more. 
# All animals entered by player 1 must be stored in a list. 

# Once all animals have been entered by player 1, player 2 will enter a single guess. 
# All inputs and outputs must have suitable messages. 
# Save your program.  [4 marks]
# -----------------------------------------------------------


# num_of_animals = 5
# for x in range(num_of_animals):
# 	p1_animal = input("Player 1, please enter an animal: ")
# 	p1_animal = p1_animal.lower()
# 	p2_guess = input("Player 2, please enter your guess: ")
# 	p2_guess = p2_guess.lower()
# p1_list = []
# while True:

#     p1_animal = input("Player 1 , please enter an animal: ")
#     p1_animal = p1_animal.lower()
    
#     p1_list.append(p1_animal)

#     proceed = input("Would you like to continue? ")
#     proceed = proceed.lower()
#     if proceed != "y":
#         break
# print(p1_list)




#============================================================
# 2.	Save your program as ANIMAL2_2023_<your name>_<centre number>_<index number>.py 

# Edit your program to search the list of animals to find the guess entered by player 2. 
# Player 2 has a score that starts at 0. If the guess entered by player 2 is found in the list:
# •	the animal is removed from the list
# •	the score for player 2 is incremented by 1
# Save your program. [3 marks]
# -----------------------------------------------------------

# p1_list = []
# while True:

#     p1_animal = input("Player 1 , please enter an animal: ")
#     p1_animal = p1_animal.lower()
    
#     p1_list.append(p1_animal)

#     proceed = input("Would you like to continue? ")
#     proceed = proceed.lower()
#     if proceed != "y":
#         break
# print(p1_list)

# #task 1.2
# p2_guess = input("Player 2, please enter your guess: ")
# p2_guess = p2_guess.lower()
# p2_score = 0

# if p2_guess in p1_list:
#     p2_score += 1
#     p1_list.remove(p2_guess)






#============================================================
# 3.	Save your program as ANIMAL3_2023_<your name>_<centre number>_<index number>.py

# Edit your program to allow player 2 to keep entering guesses until they enter 
# an animal that is not found in the list, or until the list is empty. 
# When player 2 enters an animal that is not found in the list:
# •	the game ends and informs player 2 the game is over 
# •	a message is displayed showing: 
# o	player 2 their score “
# o	the animals that are still in the list.
# All inputs and outputs must have suitable messages. Save your program. [3 marks]
# -----------------------------------------------------------
p1_list = []
while True:

    p1_animal = input("Player 1 , please enter an animal: ")
    p1_animal = p1_animal.lower()
    
    p1_list.append(p1_animal)

    proceed = input("Would you like to continue? ")
    proceed = proceed.lower()
    if proceed != "y":
        break
print(p1_list)

#task 1.2
while True:
    p2_guess = input("Player 2, please enter your guess: ")
    p2_guess = p2_guess.lower()
    p2_score = 0

    if p2_guess in p1_list:
        p2_score += 1
        p1_list.remove(p2_guess)
    elif p2_guess not in p1_list:
        print("Game Over")
        print(f"Your score is {p2_score}")
        print(f"The remaining animals in the list that you did not guess are {p1_list}")
        break
    elif p1_list == "":
        print("Congratulations, you have managed to find every animal ! ")
        print(f"Your score is {p2_score}")
        break