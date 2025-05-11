"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
import typing

class Quiz:
    def __init__(self, path : str, mode : str) -> None:
        self.path = path
        self.mode = mode

    @property
    def read_file(self) -> typing.List:
        file = open(self.path, self.mode)
        quiz_data = file.readlines()
        file.close()
        return quiz_data

    @staticmethod
    def list_questions(quiz_data: typing.List) -> typing.List:
        questions = [question.strip() for question in quiz_data]
        return questions

    @staticmethod
    def quiz(questions : typing.List) -> int:
        correct = 0
        for question in questions:
            index = question.index("=")
            ques = question[:index]
            print(ques)
            ans = question[index+1:]
            prompt = "Enter your answer : "
            response = input(prompt)
            if response == ans:
                correct += 1
        print(f"Number of correct answer is {correct}, your score is {correct/4}")
        return correct

quiz_obj = Quiz('./question.txt','r')

lines = quiz_obj.read_file

ques = quiz_obj.list_questions(lines)

quiz = quiz_obj.quiz(ques)