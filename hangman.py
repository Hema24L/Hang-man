import random

from hangmanart import stages
from hangmanwords import list1
from hangmanart import logo

print(logo)
chosen_word = random.choice(list1)
blank_array = []

for i in chosen_word:
    blank_array += '_'
[print(*a, end=" ") for a in blank_array]

# print(len(chosen_word))

length_of_chosen_word = len(chosen_word)
splited_word = list(chosen_word)

# print(splited_word)

end_of_game = False
count = 0
while not end_of_game:
    guess_letter = input("\nEnter the word you guess\n").lower()
    if guess_letter in blank_array:
        print("You have already guessed the letter")
    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess_letter:
            blank_array[pos] = letter
    if guess_letter not in chosen_word:
        print("Wrong guess")
        count += 1
        if count == 6:
            print('You Lose!')
            end_of_game = True
        print(stages[count])
    if '_' not in blank_array:
        end_of_game = True
        print('\nYou Win!!')
    [print(*a, end=" ") for a in blank_array]