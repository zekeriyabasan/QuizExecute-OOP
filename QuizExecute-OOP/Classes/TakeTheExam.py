from Classes import AnswerQuestion,TakeTheExam,ExaminationPaper

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
