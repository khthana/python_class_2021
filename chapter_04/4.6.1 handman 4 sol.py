
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - สร้างตัวแปร 'lives' เพื่อเก็บจำนวนชีวิต
#|Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for i in range(word_length):
    display.append('_')


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    #TODO-2: - ถ้าอักษรที่เดาไม่ใช่อักษรใน chosen_word
    #|         ให้ลดค่า 'lives' ลง 1. 
    #|         ถ้า lives เหลือ 0 จบเกมและแสดง "You lose."            
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

     #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if ('_' not in display):
        end_of_game=True
        print("you win.")

    #TODO-3: - พิมพ์ ASCII art จาก 'stages' ที่สอดคล้องกับ 'lives' ที่เหลืออยู่
    print(stages[lives])