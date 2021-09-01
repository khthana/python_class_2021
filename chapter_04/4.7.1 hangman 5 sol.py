import random

#TODO-1: - เปลี่ยนจาก word list ในไฟล์เป็น 'word_list' จากไฟล์ hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import logo จากไฟล์ hangman_art.py และพิมพ์ในตอนเริ่มเกม
from hangman_art import logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for i in range(word_length):
    display.append('_')


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - ถ้าผู้ใช้ป้อนตัวอักษรที่เคยเดาไปแล้ว แสดงข้อความ
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        #TODO-5: - ถ้าตัวอักษรไม่ได้อยู่ใน chosen_word พิมพ์อักษร ให้บอก user ว่าผิด
        print(f"You guessed {guess}, that's not in the word. You lose a life.")        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

     #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if ('_' not in display):
        end_of_game=True
        print("you win.")

    #TODO-2: - Import จากไฟล์ hangman_art.py และแสดงผล
    from hangman_art import stages
    print(stages[lives])