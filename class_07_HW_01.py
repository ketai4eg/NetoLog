class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grade:
                lecturer.grade[course]+=[grade]
            else:
                lecturer.grade[course]=[grade]

    def __str__(self):
        average=(sum(list(self.grades.values())[0]))/len(list(self.grades.values())[0])
        return f"""     ---Студент---
Имя: {self.name}
Фамилия:{self.surname}
Средняя оценка за ДЗ: {average:.3}
Курсы в процессе: {self.courses_in_progress}
Курсы окончены: {self.finished_courses}"""


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"""Prof {self.name} {self.surname}, attached to {self.courses_attached}"""


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade={}

    def __str__(self):
        average=(sum(list(self.grade.values())[0]))/len(list(self.grade.values())[0])
        return f"""     ---Лектор---
Имя: {self.name}
Фамилия:{self.surname}
{self.grade}
Средняя оценка:  {average:.3}"""

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f"""     ---Ревьювер---
Имя: {self.name}
Фамилия:{self.surname}"""

s1=Student("Ivan", "Ivanov", "Male")
s1.finished_courses.append("Python")
s1.courses_in_progress.append("Java")

s2=Student("Nik", "Serov", "Male")
s2.finished_courses.append("Java")
s2.finished_courses.append("Pascal")
s2.courses_in_progress.append("Python")

l1=Lecturer("Paca", "Vaca")
l1.courses_attached.append("Java")
l1.courses_attached.append("C++")
l1.courses_attached.append("C#")

l2=Lecturer("Alfa", "Centavra")
l2.courses_attached.append("Java")
l2.courses_attached.append("Python")
l2.courses_attached.append("Pascal")

r1=Reviewer("Bubble", "Gum")
r1.courses_attached.append("Java")
r1.courses_attached.append("Python")
r1.courses_attached.append("Pascal")

r2=Reviewer("Senhor", "Pomidor")
r2.courses_attached.append("Java")
r2.courses_attached.append("Python")
r2.courses_attached.append("PHP")

r1.rate_hw(s1, "Java", 4)
r1.rate_hw(s1, "Java", 8)
r1.rate_hw(s1, "Java", 10)

r2.rate_hw(s2, "Python", 4)
r2.rate_hw(s2, "Python", 8)
r2.rate_hw(s2, "Python", 8)

s1.rate_lect(l1,"Java", 9)
s1.rate_lect(l1,"Java", 5)
s1.rate_lect(l1,"Java", 6)

s2.rate_lect(l2,"Python", 4)
s2.rate_lect(l2,"Python", 5)
s2.rate_lect(l2,"Python", 6)

print(s1)
print(s2)
print(l1)
print(l2)
print(r1)
print(r2)

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)