import random
words = [
    "apple", "banana", "cherry", "grape", "orange", "peach", "pear", "plum", "mango", "kiwi",
    "strawberry", "blueberry", "raspberry", "watermelon", "pineapple", "coconut", "papaya",
    "apricot", "fig", "pomegranate",

    "dog", "cat", "horse", "tiger", "lion", "zebra", "giraffe", "elephant", "monkey", "gorilla",
    "kangaroo", "panda", "koala", "leopard", "cheetah", "wolf", "bear", "fox", "rabbit", "squirrel",

    "house", "school", "church", "castle", "palace", "mansion", "cottage", "apartment", "village",
    "garden", "forest", "desert", "mountain", "valley", "river", "ocean", "island", "beach", "cave",

    "computer", "keyboard", "mouse", "screen", "monitor", "printer", "scanner", "laptop", "tablet",
    "phone", "internet", "website", "server", "network", "software", "hardware", "database", 
    "program", "algorithm",

    "football", "basketball", "tennis", "cricket", "rugby", "hockey", "baseball", "golf", 
    "swimming", "running", "cycling", "skiing", "boxing", "wrestling", "karate", "judo", "chess",
    "badminton", "volleyball",

    "happy", "sad", "angry", "tired", "sleepy", "excited", "bored", "scared", "proud", "brave",
    "funny", "serious", "clever", "kind", "gentle", "strong", "weak", "fast", "slow", "quiet",

    "universe", "galaxy", "planet", "asteroid", "meteor", "comet", "satellite", "spaceship",
    "rocket", "astronaut", "gravity", "telescope", "microscope", "quantum", "physics", "chemistry",
    "biology", "geology", "history", "philosophy",

    "python", "java", "ruby", "swift", "kotlin", "javascript", "typescript", "rust", "go", "perl",
    "haskell", "fortran", "matlab", "scheme", "scala", "elixir", "cobol", "assembly", "bash", "linux"
]

word = random.choice(words)
blanks = list("_" * len(word))

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

chances = len(HANGMANPICS)
print(f"You have {chances} chances to guess every letter in the word")
check = 0
chances = len(HANGMANPICS)
guesses = []
for _ in range(len(HANGMANPICS)):
    guess = input("Enter your guess: ")
    print(f"You have {chances} left")
    
    indexes = []
    start = 0
    if guess in word:
        while True:
            pos = word.find(guess, start)
            if pos == -1:
                break
            indexes.append(pos)
            start = pos + 1 
        for i in indexes:
            blanks[i] = word[i]
    else:
        check += 1
        print(HANGMANPICS[check])
        chances -= 1
    if guess in guesses:
        print("You guessed this already")
    guesses.append(guess)
    if "_" not in " ".join(blanks):
        print("YOU WIN!!!!!!!!")
        break

collated = " ".join(blanks)
if "_" not in collated:
	print("You win")
else:
    print(HANGMANPICS[-1])
    print("LOOSER!!!!!!!!!")
    print(f"The correct word was {word}")		



