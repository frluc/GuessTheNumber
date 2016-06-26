#Guess the Number

import random

print('Try to guess a number between 1 and 20')

#variables initialization

thenumber = random.randint(1,20)
guess = 0
tries = 0

#guessing loop

while guess <> thenumber:
	print('Type your guess:')
	guess = input()
	tries += 1
	if guess > thenumber:
		print('too high')
	elif guess < thenumber:
		print('too low')
	elif guess == thenumber:
		print 'you win in',tries,'tries!'
	else:
		print('WTF?')
