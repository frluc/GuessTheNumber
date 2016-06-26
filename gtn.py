#Guess the Number

import random

#variables initialization

rangel = 1 #low boundary
rangeh = 20 #high boundary
thenumber = random.randint(rangel,rangeh)
guess = 0
tries = 0

#guessing loop

print("Try to guess a number between " + str(rangel) + " and " + str(rangeh))

while guess != thenumber:
	print("Type your guess:")
	guess = input()
	if guess.isdigit():
		guess = int(guess)
		if guess < rangel or guess > rangeh :
			print("Can you count properly?")
		else:
			tries += 1
			if guess > thenumber:
				print("too high")
			elif guess < thenumber:
				print("too low")
			elif guess == thenumber:
				print ("you win in " + str(tries) + " tries!")
	else:
		print("You know what integers are?")
