# Create a program that selects a random word and then allows the user to guess it in a game of hangman.
# Like the real game, there should be blank spots for each letter in the word, and a part of the body should be added each time the user guesses a letter than is not in the answer.
# You may choose how many wrong turns the user can make until the game ends.
# Subgoals:
# If the user loses, print out the word at the end of the game.
# Create a "give up" option.

import random

#List of words
list_of_words=["poppy", "polliop", "polipo", "pio"]
answer= random.choice(list_of_words)

blankword=print(len(answer)*(" _ "))

guess=" "
guesslist= list(guess)

for i in range(3):
	guess=input("your guess: ")
	

	if (any(elem in letras for elem in guess))== True:
		guesslist.append(guess)
		print(guesslist)
	else:
		print(guess + "is not in the word")


for i in range(lines):
	print(guesslist)
	guess= input("your guess: ")
	# Cambiar las letras por la rayita. 
	for n, i in enumerate(pick):
		if i not in guesslist:
			pick[n]= " _ "
	print(answer)

	if (any(elem in answer for elem in guess))== True:
	 	guesslist.append(guess)
	



	# print(answer)		
	# for i in range(3):
	# 	guess=input("your guess: ")
			
	# 	for n, i in enumerate(answer):
	# 		if i == guess:
	# 			answer[n]=" _ "
	# 	print(answer)






		# if (any(elem in answer for elem in guess))== True:
		# 	guesslist.append(guess)
		# 	print([x for x in guesslist])
		# else:
		# 	print(guess + "is not in the word")
