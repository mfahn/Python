import time
name=input("What is your name?")
print(f"Hello, {name}. Time to play hangman!")
time.sleep(1)
print("Start guessing...")
time.sleep(0.5)
word="CybHer"
guesses=''
turns =10
while turns>0:
	failed=0
	for char in word:
		if char in guesses:
			print(char)
		else:
			print("_")
			failed +=1
	if failed==0:
		print("you won")
		break
	guess=input("Guess a character: ")
	guesses += guess

	if guess not in word:
		turns -=1
		print("Wrong guess")
		print("You have {turns} more guesses remaining")
		if turns == 0:
			print("You lose")
