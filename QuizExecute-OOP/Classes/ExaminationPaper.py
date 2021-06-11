class ExaminationPaper(AnswerQuestion):

    a = ""
    def __init__(self,score=0):
        true = 0
        false = 0
        self.score = score
        
        questionScore = 100/len(self.answerQuestionList)
        for index,question in enumerate(self.answerQuestionList):
            print(f"****************SORU-{index + 1}-********************")
            print(f"{index + 1}.soru:\t{list(question.values())[0]}\n----------------------------------------")
            
            showOptions = creatOptions(self.answerQuestionList,list(question.keys())[0])
            optionsList=["A","B","C","D","E"]
            
            
            
            
            
            for option in optionsList:
                
                print(f"{option}) {showOptions[option]}")
                
                if list(question.keys())[0] == showOptions[option]:
                    global a
                    a = option
                    
                
                    
            response = str(input("cevabınız?:"))  
                    
                
            if response.upper() == str(a) or response ==str(list(question.keys())[0]):     
                self.score =self.score + 100/questionScore
                print("TRUE")
            else:
                print("FALSE!")    
                                            
                
            
            
            

        
        if not self.score == 0:
            
            true = self.score/questionScore
            false = (100-self.score)/questionScore
            
        elif score == 0:
            true = 0
            false = questionScore
            
        
        print(f"****************SONUÇLAR::{int(true+false)}/{int(true)}::********************")    
        print(f"{int(true)} doğru {int(false)} yanlış!\nPuanınız:{self.score}")
                
    

