import random
HANGMAN_PICS = ['''
  +---+
  |   |  
      |
      |
      |
     ===''', '''
  +---+
  |   |
  O   |
      |
      |
     ===''', '''
  +---+
  |   |
  O   |
  |   |
      |
     ===''', '''
  +---+
  |   |
  O   |
 /|   |
      |
     ===''', '''
  +---+
  |   | 
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  |   | 
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
  |   | 
 (O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
  |   |
 (O)  |
 /|\  |
 / \  |
     ===''']
words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapazoid chevron pentagon hexagon septagon octogon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalope mango strawberry tomato'.split(),
'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split(),
'Sports': 'baseball basketball soccer football lacrosse tennis golf running volleyball badminton swimming boxing skiing cricket rugby pool darts bowling hockey surfing cycling archery fishing gymnastics'.split(),
'First Twenty Elements': 'hydrogen helium lithium beryllium boron carbon nitrogen oxygen fluorine neon sodium magnesium aluminium silicon phospohorus sulfur chlorine argon potassium calcium'.split()}

def getRandomWord(wordDict):
    # This function returns a random string from the passed dictionary of lists of strings, and the key also.
    # First, randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if guess == secretWord: #this allows the player to guess the word in its entirity and not just letter by letter - Noah
            print('You have guessed the correct word!!!')
            if playAgain():
                missedLetters = ''    
                correctLetters = ''
                gameIsDone = False  #this will loop this the code if the player wishes to play again - Noah

            else:
                break #if the user does not want to play again, this stops the code - Noah
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')

difficulty = 'X'
while difficulty not in 'EMHP':
  print('Enter difficulty: E - Easy, M - Medium, H - Hard, P - Pendar ')
  difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]
if difficulty == 'P':
    #you have one life, if you guess an incorrect letter, you lose.
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[6]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[4]
    del HANGMAN_PICS[3]
    del HANGMAN_PICS[2]
    del HANGMAN_PICS[1]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('CONGRATS! YOU HAVE GUESSED THE CORRECT WORD: "' + secretWord +'')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
##asher is very cute
#I added the sports and first tewenty elements categories and changed some of the outputs - Noah
