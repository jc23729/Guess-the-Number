from random import randint
#Part of step 4 set these two constants that are Global
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# 3 Function to check if user's guess against actual answer
def check_answer(guess, answer):
  if guess > answer:
    print("Too high")
  elif guess < answer:
    print("Too Low")
  else:
    print(f"You got it! The answer was {answer}.")

#Step 1 Choosing a random number between 1 and 100


print("Welcome to the guessing Game!")
print ("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)
print(f"Pssst the correct answer is {answer}")

#4. Make a function to set difficulty changed order because should have the difficulty level choice first

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS



#2. Let the user guess a number
guess = int(input("Make a guess:"))
turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess a number")



# Track the number of turns and reduce by 1 if they get it wrong 



#Repeat the guessing functionality if they get it wrong


