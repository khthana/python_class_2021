#-----------------------------------------
#* Game of Rock Paper Scissors
#-----------------------------------------

import random

user_action = input("Enter a choice (rock, paper, scissors): ")

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

#TODO-1: เขียนโปรแกรม เพื่อตัดสินผู้ชนะ โดยมีหลักการดังนี้
#|       ถ้าเลือกเหมือนกันให้แสดง Both players selected [ตัวเลือก]. It's a tie!
#|       ถ้าผู้ใช้เลือก rock และ คอมพิวเตอร์เลือก scissors ให้แสดง Rock smashes scissors! You win!
#|       ถ้าผู้ใช้เลือก rock และ คอมพิวเตอร์ไม่เลือก scissors ให้แสดง Paper covers rock! You lose.
#|       ให้เขียนโปรแกรมลักษณะนี้ กับ กรณีที่เหลือ 
#|

#TODO-2: เมื่อจบเกมให้ถามผู้ใช้ว่า "Play again? (y/n): ถ้าผู้ใช้ตอบ y ก็ให้กลับไปเล่นใหม่ 






