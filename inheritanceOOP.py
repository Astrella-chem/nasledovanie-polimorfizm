
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
        return self.grade_avg < other_student.grade_avg

    def __eq__(self, other_student):
        if not isinstance(other_student, Student):
            print('Не студент')
        return self.grade_avg == other_student.grade_avg

    def __ne__(self, other_student):
        if not isinstance(other_student, Student):
            print('Не студент')
        return self.grade_avg != other_student.grade_avg

    def __le__(self, other_student):
        if not isinstance(other_student, Student):
            print('Не студент')
        return self.grade_avg <= other_student.grade_avg

    def __gt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Не студент')
        return self.grade_avg > other_student.grade_avg

    def __ge__(self, other_student):
        if not isinstance(other_student, Student):
            print('Не студент')
        return self.grade_avg >= other_student.grade_avg

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
        if not isinstance(other_lecturer, Lecturer):
            print('Не лектор')
        return self.average() == other_lecturer.average()

    def __ne__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Не лектор')
        return self.average() != other_lecturer.average()

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Не лектор')
        return self.average() < other_lecturer.average()

    def __le__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Не лектор')
        return self.average() <= other_lecturer.average()

    def __gt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Не лектор')
        return self.average() > other_lecturer.average()

    def __ge__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Не лектор')
        return self.average() >= other_lecturer.average()

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

#4
student_1 = Student('Вовочка', 'Петров', 'мужской')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Design']

student_2 = Student('Светочка', 'Козлова', 'женский')
student_2.courses_in_progress += ['Design']
student_2.finished_courses += ['Python']

lecturer_1 = Lecturer('Никола', 'Тесла')
lecturer_2 = Lecturer('Мария', 'Кюри')
lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Design']

student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Design', 8)

reviewer_1 = Reviewer('Дмитрий', 'Менделеев')
reviewer_2 = Reviewer('Альберт', 'Эйнштейн')
reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Design']

reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_2.rate_hw(student_2, 'Design', 7)

print(student_1)
print(student_2)

print(reviewer_1)
print(reviewer_2)

print(lecturer_1)
print(lecturer_2)

print("___\n")#среднее
print(f'Средняя оценка студентов: {(student_1.grade_avg + student_2.grade_avg) / 2}')
print(f'Средняя оценка лекторов: {(lecturer_1.average() + lecturer_2.average()) / 2}')

print("___\n")#сравнение
print(student_2.__lt__(student_1))
print(lecturer_2.__lt__(lecturer_1))

print("___\n")#средняя оценка
stud_list = [student_1, student_2]

def medium_grade_student(stud_list, course):
    sum_grade = 0
    count_grade = 0
    for student in stud_list:
        if course in student.grades:
            sum_grade += sum(student.grades[course])
            count_grade += len(student.grades[course])
    return sum_grade / count_grade

print(medium_grade_student(stud_list, 'Python'))

lect_list = [lecturer_1, lecturer_2]

def medium_grade_lecturer(lect_list, course):
    sum_grade = 0
    count_grade = 0
    for lecturer in lect_list:
        if course in lecturer.rating:
            sum_grade += sum(lecturer.rating[course])
            count_grade += len(lecturer.rating[course])
    return sum_grade / count_grade

print(medium_grade_lecturer(lect_list, 'Design'))