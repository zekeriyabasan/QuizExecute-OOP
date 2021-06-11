
from random import randint

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