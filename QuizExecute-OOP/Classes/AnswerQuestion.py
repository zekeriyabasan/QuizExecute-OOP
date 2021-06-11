class AnswerQuestion:
    answerQuestionList = list() 

    def __init__(self,answer,question):
        self.answer = answer
        self.question = question
        answerQuestionList = self.answerQuestionList.append({answer:question})
        
    def __del__(self):
        return self.answerQuestionList
