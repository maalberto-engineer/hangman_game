import random
import os

def play_game():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    words_file = os.path.join(script_dir, 'words.txt')
    
    try:
        with open(words_file, 'r') as file:
            content = file.read()
            words = content.split()
    except FileNotFoundError:
        print("Error: words.txt not found")
        return False
    
    secret_word = random.choice(words).strip().lower()
    letters_guessed = []
    wrong_letters = []
    mistakes_made = 0
    max_guesses = 6
    
    while mistakes_made < max_guesses:
        # Display word with blanks
        display_word = ''
        for letter in secret_word:
            if letter in letters_guessed:
                display_word += letter + ' '
            else:
                display_word += '_ '
        print(display_word.strip())
        
        # Check win condition
        if all(letter in letters_guessed for letter in secret_word):
            print(f"Congrats, {secret_word} was correct!")
            return True
            
        print(f"lives = {max_guesses - mistakes_made}")
        if wrong_letters:
            print(f"Wrong letters: {wrong_letters}")
        
        # Get guess
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter")
            continue
            
        if guess in letters_guessed or guess in wrong_letters:
            print("Already guessed that letter")
            continue
        
        if guess in secret_word:
            letters_guessed.append(guess)
        else:
            wrong_letters.append(guess)
            mistakes_made += 1
            print("Wrong!")
    
    print(f"You lost! The word was: {secret_word}")
    return False

def main():
    while True:
        result = play_game()
        
        if result:
            print("You won!")
        else:
            print("Better luck next time!")
        
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()
