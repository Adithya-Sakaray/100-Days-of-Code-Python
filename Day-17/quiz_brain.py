class QuizBrain:

    def __init__(self,question_bank):
        self.question_bank = question_bank
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        if(self.question_number<10):
            return True
        else:
            print("You have completed this quis!!")
            print(f"Your score is: {self.score}/{self.question_number}")
            return False

    def next_question(self):
        current_question = self.question_bank[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? :")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):

        if (user_answer.lower() == correct_answer.lower()) :
            print("You got it right!!")
            self.score += 1
        else:
            print("It is wrong")
        print(f"The correct answer is:{correct_answer}")
        print(f"Your score is:{self.score}/{self.question_number}")
        print("\n")


        