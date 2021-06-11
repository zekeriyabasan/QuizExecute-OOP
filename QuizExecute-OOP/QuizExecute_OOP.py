from random import randint
class AnswerQuestion:
    answerQuestionList = list() 

    def __init__(self,answer,question):
        self.answer = answer
        self.question = question
        answerQuestionList = self.answerQuestionList.append({answer:question})
        
    def __del__(self):
        return self.answerQuestionList

#-------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------------------
class TakeTheExam(ExaminationPaper):
    score = 0
    def __init__(self,name,surName,no):
        self.name = name
        self.surName = surName
        self.no = no
    def startExam(self):
        start = ExaminationPaper()
        self.score = start.score
        return print(f"ADI:{self.name} SOYADI:{self.surName} NUMARASI:{self.no} PUAN:{self.score}")
#-------------------------------------------------------------------------------------------
def creatOptions(liste,trueAnswer):
    
    answerList = getAnswer(liste)
    answerList.remove(trueAnswer)
    
    optionsList=["A","B","C","D","E"]
    
    showOptions = {}

    trueAnswerIndex = randint(0,4)
    showOptions[optionsList[trueAnswerIndex]]=trueAnswer
    
    for index,option in enumerate(optionsList):
        answerIndex = randint(0,len(answerList)-1)
        if index == trueAnswerIndex:
            continue
        
        showOptions[option]=answerList[answerIndex]
        answerList.remove(answerList[answerIndex])      
        
    return showOptions
#-------------------------------------------------------------------------------------------
def getAnswer(liste):
    optionList = list()
    for index,question in enumerate(liste):
        optionList.append(list(question.keys())[0])
    
    return optionList
#-------------------------------------------------------------------------------------------

soru1 = AnswerQuestion("6","2*3")
soru2 = AnswerQuestion("8","2*4")
soru3 = AnswerQuestion("10","2*5")
soru4 = AnswerQuestion("12","2*6")
soru5 = AnswerQuestion("14","2*7")
soru6 = AnswerQuestion("16","2*8")
soru7 = AnswerQuestion("remove","Pythonda liste silme metodu nedir?")
soru8 = AnswerQuestion("Hata","exceptional ne demektir")
soru9 = AnswerQuestion("Düşür","Drop kelime anlamı")
soru10 = AnswerQuestion("1881","M.Kemal Atatürk ün doğum yılı kaçtır")

S1 = TakeTheExam("Zekeriya","BASAN",151101016)
S2 = TakeTheExam("Aslı","Kal",151101016)
S3 = TakeTheExam("Bade","ELMAS",151101016)
S4 = TakeTheExam("ASuman","YALÇIN",151101016)

S1.startExam()