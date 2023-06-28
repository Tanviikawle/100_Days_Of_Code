class QuizBrain:
    def __init__(self,q_bank):
        self.score=0
        self.question_number=0
        self.question_list=q_bank

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("You got it right!")
        else:
            print("You got it wrong.")
        print(f"The correct answer is :{correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")

    def next_question(self):
        que=self.question_list[self.question_number]
        current_que=self.question_number+1
        user_ans=input(f"Q.{current_que}: {que.text} (True/False): ")
        self.question_number+=1
        self.check_answer(user_ans,que.answer)

    def still_has_questions(self):
        return self.question_number<len(self.question_list)
    



            
