class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].question} "
                            f"(True/False)?: ").capitalize()
        self.question_number += 1
        self.check_answer(user_answer)

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        elif self.question_number < len(self.question_list):
            return True

    def check_answer(self, user_answer):
        if user_answer == self.question_list[self.question_number-1].answer:
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {self.question_list[self.question_number-1].answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")



