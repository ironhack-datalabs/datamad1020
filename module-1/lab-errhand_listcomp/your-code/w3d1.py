class Student:
    def__init__(self,name,course):
        self.name = name
        self.course = course
    def salute(self):
        return f"Hello, my name is {self.name, and I study{self.course}"
    def attend(self,seminar):
        if self.course in seminar.keywords:
            return f"Sending mail to student with inviation for {self.theme} event on {self.date}"
        else:
            return f"{self.name} shall no attend"


class Seminar:
    def__init__(self, theme, presenter, data, *keywords):
        self.theme = theme
        self.presenter = presenter
        self.keywords = keywords