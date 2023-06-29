class Course:
    def __init__(self, name, teacher_name) -> None:
        self.name = name
        self.teacher_name = teacher_name

    def get_description(self):
        return "{} with {}".format(self.name, self.teacher_name)

class Student:
    def __init__(self, name, grade, courses) -> None:
        self.name = name
        self.grade = grade
        self.courses = courses

    def list_courses(self):
        print("\n".join([v.get_description() for v in self.courses]))


