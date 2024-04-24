import random

def printWord(word_):
    print(''.join(word_))


def check(letter, word, word_):
    found = False
    for i in range(len(word)):
        if letter == word[i]:
            word_[i] = letter
            found = True
    return found


def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'watermelon']
    return random.choice(words)


def checkWin(word, word_):
    if "_" not in word_:
        print("\nCongratulations! You guessed the word:", word)
        return True
    return False


def main():
    word = choose_word()
    print("Try to guess the word.")
    word_ = ["_"] * len(word)
    printWord(word_)
    fail = 0
    while fail != 7:
        letter = input("Guess a letter: ")
        found = check(letter, word, word_)
        if not found:
            fail += 1
            print("\nIncorrect guess. You have \n", 7 - fail, "guesses left.")
        printWord(word_)
        if checkWin(word, word_):
            break
    else:
        print("\nSorry, you've run out of guesses. The word was:", word)


if __name__ == "__main__":
    main()
