# Problem Set 2, hangman.py
# Name: leonel cerda
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
BOLD = '\033[1m'
END = '\033[0m'

def load_words():
   
    print("Loading word list from file...")
    # inFile: file
    inFile = open("words.txt", 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded...")
    return wordlist

wordlist = load_words()


def choose_word(wordlist):
   
    return random.choice(wordlist)




def is_word_guessed(secret_word, letters_guessed):
  
   
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    
    
    guessed_word = ""

    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word = guessed_word + letter 
        else:
            guessed_word = guessed_word + " _ "
    return guessed_word





def get_available_letters(letters_guessed):
    available_letters = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters += letter + " "
    return available_letters


def get_unique_letters(secrect_word):
    letters = []
    for letter in secret_word:
        if letter not in letters:
            letters.append(letter)
            
    return len(letters)
    


def hangman(secret_word):
    runs = 0
    
    guesses_left = 6
    warnings = 3

    message = " "
    

    letters_guessed = []

    
    print("\n" + "Welcome to the game Hangman!")
    print("\n" + "I am thinking of a word that is" , len(secret_word), "letters long.")
    print("\n"+ "You have", warnings, "warnings left.")

    def win():
      print("\n" + "Congratulations, you won!")
      score =  get_unique_letters(secret_word) * guesses_left
      print("\n" + "Your total score for this game is:", score ) 
      quit()

    def lose():
      print("\n" + f"Sorry, you ran out of guesses. The word was {BOLD}{secret_word.upper()}{END}." )
      quit()


    while guesses_left > 0 and not is_word_guessed(secret_word, letters_guessed):
        
        runs += 1
        
        print("\n" + "-" * 13, "-" * 13, "-" * 13) 
        print("\n"+ "You have", guesses_left, "guesses left.")
        print("\n" + "Available letters:" , get_available_letters(letters_guessed))

        guess = input("\n" + "Please guess a letter: ")
       

        if not guess.isalpha():
            

            if warnings > 0:
                warnings -= 1
                message = f"Oops! That is not a valid letter. You have {warnings} warnings left."

            else:
                guesses_left -= 1
                message = "Oops! That is not a valid letter. You have no warnings left so you lose one guess."
            print("\n" + message, get_guessed_word(secret_word, letters_guessed))
            continue
       
        else:
            guess = guess.lower()
            
            if guess in letters_guessed:
                
                
                if warnings > 0:
                  warnings -= 1
                  message = f"Oops! You've already guessed that letter. You now have {warnings} warnings left. "

                else:
                 guesses_left -= 1
                 message = "Oops! You've already guessed that letter. You have no warnings left so you lose one guess: "
            else:
                
                letters_guessed.append(guess)

                if guess in secret_word:
                    message = "Good guess: "
                
                else:

                  if guess in 'aeiou':
                     guesses_left -= 2
                     message = "Oops! That vowel is not in my word, so you lose 2 guesses: "
                  else:
                     guesses_left -= 1
                     message = f"Oops! {BOLD}{guess.upper()}{END} is not in my word: "
            print()
            print(message, get_guessed_word(secret_word, letters_guessed))
            print()
            
        
            if runs > 1 and guesses_left > 0 and message == "Good guess: ":
                yes_or_no = input("Would you like to guess the word? (Y)es or (N)o: ").lower()
                yes_or_no = yes_or_no.lower()
                print()
                if yes_or_no == "y" :
                   print()
                   final_guess = input("Please input your final guess if you have one: ")
                   print()
                   if final_guess == secret_word:
                       win()
                   else: 
                       print()
                       print(f"{BOLD}{final_guess.upper()}{END} was not my word!")
                       lose()
                while yes_or_no not in ("y", "n"):
                   print()
                   print("That is not a valid answer. Please try again.")
                   print()
                   yes_or_no = input("Would you like to guess the word? (Y)es or (N)o: ").lower()
                   print()
                   
            
         
      
    if is_word_guessed(secret_word, letters_guessed):
      
      win()
    else:
      lose()
        
    

        




       

          
            



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

    my_word = my_word.replace(" ", "")
    #  where my_word is  _  _  _  _  _  
   
    # if not same len -> false
    if len(my_word) != len(other_word):
        return False
    
    # search guessed word and see if same letters
    for i in range(len(my_word)):
        # search the whole word
        # grab each letter and check if in the wrong letters section
            # if it is update knowledge and remove word
        
        
        if my_word[i] in 
    return True
    


    





def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matching_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matching_words.append(word)

    if len(matching_words)  > 0:
        for word in matching_words:
            print(word + " ")
    else: 
        print("\n" + "No matches found")


    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    
    guesses_left = 6
    warnings = 3

    message = " "

    letters_guessed = []

    print("\n" + "Welcome to the game Hangman!")
    print("\n" + "I am thinking of a word that is" , len(secret_word), "letters long.")
    print("\n"+ "You have", warnings, "warnings left.")

    def win():
      print("\n" + "Congratulations, you won!")
      score =  get_unique_letters(secret_word) * guesses_left
      print("\n" + "Your total score for this game is:", score, "\n") 
      quit()

    def lose():
      print("\n" + f"Sorry, you ran out of guesses. The word was {BOLD}{secret_word.upper()}{END}." + "\n" )
      quit()


    while guesses_left > 0 and not is_word_guessed(secret_word, letters_guessed):
        
        print("\n" + "-" * 13, "-" * 13, "-" * 13) 
        print("\n"+ "You have", guesses_left, "guesses left.")
        print("\n" + "Available letters:" , get_available_letters(letters_guessed))

        guess = input("\n" + "Please guess a letter: ")
        
        if guess == "*":
            print("\n" + "Possible matches are: " + "\n" )
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))

        elif not guess.isalpha():
            if warnings > 0:
                warnings -= 1
                message = f"Oops! That is not a valid letter. You have {warnings} warnings left."

            else:
                guesses_left -= 1
                message = "Oops! That is not a valid letter. You have no warnings left so you lose one guess."
            
            print("\n" + message, get_guessed_word(secret_word, letters_guessed))
            continue
       
        else:
            guess = guess.lower()
            
            if guess in letters_guessed:
                
                
                if warnings > 0:
                  warnings -= 1
                  message = f"Oops! You've already guessed that letter. You now have {warnings} warnings left. "

                else:
                    guesses_left -= 1
                    message = "Oops! You've already guessed that letter. You have no warnings left so you lose one guess: "
            else:
                
                letters_guessed.append(guess)

                if guess in secret_word:
                    message = "Good guess: "
                
                else:

                  if guess in 'aeiou':
                     guesses_left -= 2
                     message = "Oops! That vowel is not in my word, so you lose 2 guesses: "
                  else:
                     guesses_left -= 1
                     message = f"Oops! {BOLD}{guess.upper()}{END} is not in my word: "
            
            print("\n" + message, get_guessed_word(secret_word, letters_guessed))
            
            
        
            if guesses_left != 0 and message == "Good guess: " and len(letters_guessed) > 2 and not is_word_guessed(secret_word, letters_guessed):
                yes_or_no = input("\n" + "Would you like to guess the word? (Y)es or (N)o: ").lower()

                if yes_or_no == "y" :   
                   final_guess = input("\n" + "Please input your final guess if you have one: ")
                   
                   if final_guess == secret_word:
                       win()
                   else:   
                       print("\n" + f"{BOLD}{final_guess.upper()}{END} was not my word!")
                       lose()
                
                while yes_or_no not in ("y", "n"):
                   print("\n" + "That is not a valid answer. Please try again.")
                   yes_or_no = input("\n" + "Would you like to guess the word? (Y)es or (N)o: ").lower()
                
                   
            
         
      
    if is_word_guessed(secret_word, letters_guessed):
      
      win()
    else:
      lose()

    


if __name__ == "__main__":
    #secret_word = random.choice(wordlist)
    secret_word = "house"
    hangman_with_hints(secret_word)
