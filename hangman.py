import random
from time import sleep
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\+
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

words = ("COMPUTER", "BANANA", "DESK", "TESLA", "WINDOW", "UNICORN", "WAFFLES", "PHONE", "TENNIS", "HAIR", "WHITE", "KEYBOARD","GRANOLA", "ONION")
word = random.choice(words)
positive_words = ("Well done!", "Awesome!", "WOW!", "Great!", "Nice!")
max_attempts = len(word) - 1
word_so_far = ("-") * len(word)
letters_used = []
wrong = 1



def intro():
  print("\n\t \t Welcome to My Hangman Game!")
  print("\nThe amount of incorrect guesses you can have is \nequal to that of the amount of letters in the word")
  input("\nPress any key  to start: ")
  return()



def win_greet():
  print("WINNER! Congratulations!")
  print("Run the program again to play again!")
  return()



def lose_greet():
  print("Better luck next time! The word was: ", word)
  return()



def guess_letter_used():
  guess = input("Guess a letter: ").upper()
  sleep(1) # Time delay - allows reading
  print()
  while guess in letters_used:
        print("Try again!  You've already used this letter")
        guess = input("Guess a letter: ").upper()
        sleep(1)
        print()
  letters_used.append(guess)
  return(guess)



def body():

  intro()
  
  word_so_far = ("-") * len(word)
  wrong = 1
  while wrong < max_attempts and word_so_far != word:
    print("\n",HANGMAN[wrong])
    print("Word so far: ", word_so_far)
    print("Letters used: ", letters_used)

    guess = guess_letter_used()

    if guess in word:
        print(random.choice(positive_words))

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess

            else:
                new += word_so_far[i]
        word_so_far = new 

    else:
        print("Not in word! Try again!")
        wrong += 1

  print("\nCalculating result...")
  sleep(1)
  if wrong == max_attempts:
    lose_greet()
  else:
    win_greet()
  return()



body()
