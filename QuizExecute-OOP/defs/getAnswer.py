def getAnswer(liste):
    optionList = list()
    for index,question in enumerate(liste):
        optionList.append(list(question.keys())[0])
    
    return optionList
