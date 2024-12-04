def average(grades): #среднее
    summa = 0
    sbj_amount = 0
    for sbj in grades:
        summa += sum(grades[sbj])
        sbj_amount += len(grades[sbj])

    return summa / sbj_amount

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []            #завершенные курсы
        self.courses_in_progress = []         # курсы в процессе изучения
        self.grades = {}    #оценки #словарь
        self.average = 0


    def rate_lecturer(self, lecturer, rate, sbj):
        if sbj in self.courses_in_progress and sbj in lecturer.rating and sbj in lecturer.courses_attached:
            lecturer.rating[sbj] += [rate]

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)} \n'

class Mentor:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.courses_attached = []      #закрепленные курсы за ментором


class Lecturer(Mentor):
    def __init__(self, firstName, lastName,grade):
        super().__init__(firstName, lastName)
        self.grade = grade
        self.rating = {
            'Введение в программирование': [10, 10, 10, 10, 10],
            'Git': [10, 10, 10, 10, 10],
            'Python': [10, 10]
        }  # оценки #словарь


    def __str__(self):
        return f'Имя: {self.firstName} \nФамилия: {self.lastName} \nСредняя оценка за лекции:  {self.grade} \n'


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


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.finished_courses += ['Введение в программирование']
some_student.courses_in_progress += ['Git']
some_student.courses_in_progress += ['Python']
some_student.grades['Введение в программирование'] = [10, 10, 10, 10, 10]
some_student.grades['Git'] = [10, 10, 10, 10, 10]
some_student.grades['Python'] = [10, 10]

print(some_student.__str__())

some_lecturer = Lecturer('Some', 'Buddy', 9)

print(some_lecturer.__str__())

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_checked += ['Введение в программирование']
some_reviewer.rate_hw(some_student, 'Python', 10)
print(some_reviewer.__str__())
