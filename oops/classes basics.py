class Students:
    def __init__(self, student_name, student_score) -> None: ## DunDer Method
        self.name = student_name
        self.score = student_score
    
    def avg_marks(self):
        avg_marks = sum(self.score)/len(self.score)
        return avg_marks
    
stud_a = Students('Rolf',[10,20,40,67])
stud_b = Students('Jose', [50,60,30,299,76])

print(stud_a.avg_marks())
print(stud_b.avg_marks())

