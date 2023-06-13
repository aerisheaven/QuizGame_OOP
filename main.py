from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz_start = QuizBrain(question_bank)
while quiz_start.still_has_questions():
    quiz_start.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz_start.score}/{quiz_start.question_number}")
