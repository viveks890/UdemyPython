class Student:
    def __init__(self, name, school) -> None:
        self.name = name
        self.school = school
        self.marks = []

    def __repr__(self) -> str:
        return f"Student('{self.name}','{self.school}')"
    
    def __str__(self):
        return f"Student Object with name : '{self.name}' and school as '{self.school}'"

    @property
    def __len__(self):
        return len(self.marks)
    
    def __getitem__(self, i):
        return self.marks[i]
    
    def append_marks(self, mark):
        return self.marks.append(mark)

    @property
    def average(self):
        return sum(self.marks)/len(self.marks)
    
class WorkingStudent(Student):
    def __init__(self, name, school, wages) -> None:
        super().__init__(name, school)
        self.wages = wages

    @property
    def weekly_salary(self):
        return self.wages * 35
    

anna = Student('Anna', 'MIT')
rolf = WorkingStudent('Rolf', 'MIT', 12)

import random

i = 0

while i <= 4:
    anna.append_marks(random.randint(33,100))
    rolf.append_marks(random.randint(33,100))
    i += 1

for i in anna:
    print(i)

print(f"Anna's avg marks :{anna.average}")

for i in rolf:
    print(i)

print(f"Rolf's avg marks :{rolf.average}")

print(rolf.weekly_salary)