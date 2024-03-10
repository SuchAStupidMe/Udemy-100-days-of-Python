class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def make_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(guess, question.answer)

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, guess, answer):
        if guess.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {answer}.")
        print(f"Your current score is {self.score}/{self.question_number}\n")
