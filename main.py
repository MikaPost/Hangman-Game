"""
This file is for our new theme: Hangman game
Create by: Miqayel Postoyan
Date: 30 April
"""
import random


def print_word(word_):
    """
    Function: print_Word
    Brief: prints an unknown word
    Params: unknown word
    Return:	None
    """
    print(''.join(word_))


def check(letter, word, word_):
    """
    Function: check
    Brief: checks if there is a letter in a word
    Params: letter, word, word_
    Return:	new word
    """
    found = False
    lengt = len(word)
    for i in range(lengt):
        if letter == word[i]:
            word_[i] = letter
            found = True
    return found


def choose_word():
    """
    Function: choose_word
    Brief: chooses random words
    Params:None
    Return:	random word
    """
    words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'watermelon']
    return random.choice(words)


def check_win(word, word_):
    """
    Function: checkWin
    Brief: checks for victory and no
    Params:None
    Return:	True if win and False if no
    """
    if "_" not in word_:
        print("\nCongratulations! You guessed the word:", word)
        return True
    return False


def main():
    """
    Function: main
    Brief: Entry point
    """
    word = choose_word()
    print("Try to guess the word.")
    word_ = ["_"] * len(word)
    print_word(word_)
    fail = 0
    while fail != 7:
        letter = input("Guess a letter: ")
        found = check(letter, word, word_)
        if not found:
            fail += 1
            print("\nIncorrect guess. You have \n", 7 - fail, "guesses left.")
        print_word(word_)
        if check_win(word, word_):
            break
    else:
        print("\nSorry, you've run out of guesses. The word was:", word)


if __name__ == "__main__":
    main()
