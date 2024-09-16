import random

def choose_word():
   
    
    words = ["python", "hangman", "programming", "openai", "artificial", "intelligence"]
    return random.choice(words)

def display_word(word, guessed_letters):
    
  
    return ''.join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = set()
    attempts = 6 

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nCurrent word: " + display_word(word, guessed_letters))
        print(f"Wrong guesses: {', '.join(wrong_guesses) if wrong_guesses else 'None'}")
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters or guess in wrong_guesses:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue
        
        if guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses.add(guess)
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nGame over! You've run out of attempts. The word was:", word)


hangman()

