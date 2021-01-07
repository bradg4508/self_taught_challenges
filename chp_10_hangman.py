import random

def word_guess():
    words = ["ball",
             "hammer",
             "lemonade",
             "football",
             "dog",
             "strong",
             "xylophone"
             ]
    n = random.randint(0,len(words)-1)
    guess = words[n]
    return guess

def hangman(word):
    wrong = 0
    stages = ["",
              "________       ",
              "|       |      ",
              "|       |      ",
              "|       0      ",
              "|      /|\     ",
              "|      / \     ",
              "|              "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        print((" ".join(board)))
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
              print("You win! The word was: {}.".format(word))
              print("".join(board))
              win = True
              break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! The word was: {}.".format(word))

hangman(word_guess())
