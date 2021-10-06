# -----------------------------------------------------------
# ตัวอย่างนี้ จะเป็นโครงงานเกมตอบคำถาม โดยคำตอบ คือ จริง หรือ ไม่
# -----------------------------------------------------------

# คำถามจะอยู่ใน data.py โดยโครงสร้างจะเป็น list ของ dictionary

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# นำ Question ทั้งหมด มาสร้างเป็น question bank

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")




