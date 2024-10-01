class Student:
    def __init__(self, name, school) -> None:
        self.name = name
        self.school = school
        self.marks = []

    def __repr__(self) -> str:
        return f"Student('{self.name}','{self.school}')"
    
    def __str__(self):
        return f"Student Object with name : '{self.name}' and school as '{self.school}'"

    def __len__(self):
        return len(self.marks)
    
    def __getitem__(self, i):
        return self.marks[i]
    
    def append_marks(self, mark):
        return self.marks.append(mark)

    def average(self):
        return sum(self.marks)/len(self.marks)
    
class WorkingStudent(Student):
    def __init__(self, name, school, wages) -> None:
        super().__init__(name, school)
        self.wages = wages

    def weekly_salary(self):
        return self.wages * 35
    

anna = Student('Anna', 'MIT')

print(anna)
