
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []            #завершенные курсы
        self.courses_in_progress = []         # курсы в процессе изучения
        self.grades = {}    #оценки #словарь

    # студент выставляет оценку лектору
    def rate_lecturer(self, lecturer, sbj, rate):
        if isinstance(lecturer, Lecturer) and sbj in self.courses_in_progress  and sbj in lecturer.courses_attached:
            if sbj in lecturer.rating:
                lecturer.rating[sbj] += [rate]
            else:
                lecturer.rating[sbj] = [rate]
        else:
            return 'Ошибка'

    @property
    def grade_avg(self):
        grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(grades) / len(grades) if grades else 0

    def __lt__(self, other_student): #операторы сравнения
        if not isinstance(other_student, Student):
            print('Не студент')
        return self.average < other_student.average

    def __eq__(self, other_student):
        if not isinstance(other_student, Student):
            print('Не студент')
        return self.average == other_student.average

    def __ne__(self, other_student):
        if not isinstance(other_student, Student):
            print('Не студент')
        return self.average != other_student.average

    def __le__(self, other_student):
        if not isinstance(other_student, Student):
            print('Не студент')
        return self.average <= other_student.average

    def __gt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Не студент')
        return self.average > other_student.average

    def __ge__(self, other_student):
        if not isinstance(other_student, Student):
            print('Не студент')
        return self.average >= other_student.average

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.grade_avg}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)} \n'

class Mentor:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.courses_attached = []      #закрепленные курсы за ментором

class Lecturer(Mentor):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.rating = {}  # оценки #словарь

    def average(self):
        rating = 0
        lecture_sum = 0
        if not self.rating:
            return 0
        for lect in self.rating:
                lecture_sum += sum(self.rating[lect])
                rating += len(self.rating[lect])
        if rating == 0:
            return 0
        else:
            return lecture_sum / rating

    def __eq__(self, other_lecturer):
        if not isinstance(other_lecturer, Student):
            print('Не лектор')
        return self.average == other_lecturer.average

    def __ne__(self, other_lecturer):
        if not isinstance(other_lecturer, Student):
            print('Не лектор')
        return self.average != other_lecturer.average

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Student):
            print('Не лектор')
        return self.average < other_lecturer.average

    def __le__(self, other_lecturer):
        if not isinstance(other_lecturer, Student):
            print('Не лектор')
        return self.average <= other_lecturer.average

    def __gt__(self, other_lecturer):
        if not isinstance(other_lecturer, Student):
            print('Не лектор')
        return self.average > other_lecturer.average

    def __ge__(self, other_lecturer):
        if not isinstance(other_lecturer, Student):
            print('Не лектор')
        return self.average >= other_lecturer.average

    def __str__(self):
        return f'Имя: {self.firstName} \nФамилия: {self.lastName} \nСредняя оценка за лекции: {some_lecturer.average()} \n'


class Reviewer(Mentor):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.courses_checked = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.firstName}\nФамилия: {self.lastName} \n'


some_student = Student('Some', 'Buddy', "your_gender" )
some_student.courses_in_progress += ['Введение в программирование']
some_student.courses_in_progress += ['Git']
some_student.courses_in_progress += ['Python']
some_student.grades['Введение в программирование'] = [10, 10, 9, 7, 10]
some_student.grades['Git'] = [5, 7, 4, 9, 10]
some_student.grades['Python'] = [4, 9]
print(some_student.__str__())


some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Введение в программирование']
some_lecturer.courses_attached += ['Git']
some_student.rate_lecturer(some_lecturer, "Python", 5)
some_student.rate_lecturer(some_lecturer, "Введение в программирование", 6)
some_student.rate_lecturer(some_lecturer, "Git", 5)
some_student.rate_lecturer(some_lecturer, "Python", 5)
some_student.rate_lecturer(some_lecturer, "Python", 5)
some_student.rate_lecturer(some_lecturer, "Введение в программирование", 5)
print(some_lecturer.__str__())

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_checked += ['Python']
some_reviewer.courses_checked += ['Введение в программирование']
some_reviewer.courses_checked += ['Git']
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Введение в программирование', 5)
some_reviewer.rate_hw(some_student, 'Git', 5)
print(some_reviewer.__str__())
