
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for i in range(word_length):
    display.append('_')

#TODO-1: - ใช้ while loop เพื่อให้ผู้ใช้เดาตัวอักษรไปเรื่อยๆ โดย loop หยุดเมื่อเดาครบทุกตัวและไม่มี "_"
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)

    if ('_' not in display):
        end_of_game=True
        print("you win.")