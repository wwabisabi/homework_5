class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # почему не возвращает ошибку, если я хочу поставить оценку курсу, которого нет в courses_attached?
    def rate_lecture(self, lector, course, grade):
        if isinstance(lector, Lector) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Почему средняя оценка считается только из оценок последнего курса, а не перебирает все курсы?
    def count_average_grade(self):
        for item in self.grades.values():
            average = sum(item) / len(item)
        return average

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}' \
               f'\nСредняя оценка за домашние задания: {self.count_average_grade()}' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
               f'\nЗавершенные курсы:{", ".join(self.finished_courses)}'

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (Lector, float)):
            raise TypeError
        return other

    def __eq__(self, other):
        gr = self.__verify_data(other)
        return self.count_average_grade() == gr

    def __lt__(self, other):
        gr = self.__verify_data(other)
        return self.count_average_grade() > gr

    def __le__(self, other):
        gr = self.__verify_data(other)
        return self.count_average_grade() >= gr

    def __gt__(self, other):
        gr = self.__verify_data(other)
        return self.count_average_grade() < gr

    def __ge__(self, other):
        gr = self.__verify_data(other)
        return self.count_average_grade() <= gr


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_grade = {}


class Lector(Mentor):
    grades = {}

    # как сделать, чтобы функция считала оценки всех лекций?
    def count_average_grade(self):
        for item in self.grades.values():
            average = sum(item) / len(item)
        return average

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.count_average_grade()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


lector_1 = Lector('Александр', 'Иванов')
lector_2 = Lector('Сергей', 'Петров')
reviewer_1 = Reviewer('Анна', 'Николаевна')
reviewer_2 = Reviewer('Михаил', 'Игорев')
student_1 = Student('Мария', 'Смирнова', 'жен')
student_2 = Student('Алексей', 'Попов', 'муж')

student_1.courses_in_progress = ['Python']
student_2.courses_in_progress = ['Python', 'C++']
reviewer_1.courses_attached = ['Python']
reviewer_2.courses_attached = ['C++']
lector_1.courses_attached = ['Python']
lector_2.courses_attached = ['C++']

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'C++', 5)

student_1.rate_lecture(lector_1, 'Python', 9)
student_2.rate_lecture(lector_1, 'Python', 7)
student_2.rate_lecture(lector_2, 'C++', 8)

list_st = [student_1, student_2]
list_lect = [lector_1, lector_2]


def avg_rate_st(course, list=list_st):
    sum_ = 0
    len_ = 0
    for s in list:
        sum_ += sum(s.grades[course])
        len_ += len(s.grades[course])
    avg_rate = sum_ / len_
    return f'Средняя оценка за курс {course} среди студентов: {avg_rate}'


def avg_rate_lect(course, list=list_lect):
    sum_ = 0
    len_ = 0
    for s in list:
        sum_ += sum(s.grades[course])
        len_ += len(s.grades[course])
    avg_rate = sum_ / len_
    return f'Средняя оценка за курс {course} среди лекторов: {avg_rate}'


print('Лектор №1:')
print(lector_1)
print('Лектор №2:')
print(lector_2)
print('Проверяющий №1:')
print(reviewer_1)
print('Проверяющий №2:')
print(reviewer_2)
print('Студент №1:')
print(student_1)
print('Студент №2:')
print(student_2)


print(avg_rate_st('Python'))
print(avg_rate_lect('Python'))