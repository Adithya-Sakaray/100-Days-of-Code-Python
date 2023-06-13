from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    question_bank.append(Question(question_text,question_ans))

quizManager = QuizBrain(question_bank)

while (quizManager.still_has_questions()):
    quizManager.next_question()
    





