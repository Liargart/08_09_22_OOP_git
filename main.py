class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        sum_grades = 0
        quantity_grades = 0
        for grade_results in self.grades.values():
            for each_grade in grade_results:
                sum_grades += int(each_grade)
                quantity_grades += 1
        everage_grades = round(sum_grades / quantity_grades, 2)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {everage_grades}\n' \
              f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {",".join(self.finished_courses)} '
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        else:
            sum_grades = 0
            quantity_grades = 0
            for grade_results in self.grades.values():
                for each_grade in grade_results:
                    sum_grades += int(each_grade)
                    quantity_grades += 1
            self_everage_grades = round(sum_grades / quantity_grades, 2)
            sum_grades = 0
            quantity_grades = 0
            for grade_results in other.grades.values():
                for each_grade in grade_results:
                    sum_grades += int(each_grade)
                    quantity_grades += 1
            other_everage_grades = round(sum_grades / quantity_grades, 2)
        return self_everage_grades < other_everage_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


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
        res = f'Имя = {self.name}\nФамилия = {self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        sum_grades = 0
        quantity_grades = 0
        for grade_results in self.grades.values():
            for each_grade in grade_results:
                sum_grades += int(each_grade)
                quantity_grades += 1
        everage_grades = round(sum_grades / quantity_grades, 2)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {everage_grades}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        else:
            sum_grades = 0
            quantity_grades = 0
            for grade_results in self.grades.values():
                for each_grade in grade_results:
                    sum_grades += int(each_grade)
                    quantity_grades += 1
            self_everage_grades = round(sum_grades / quantity_grades, 2)
            sum_grades = 0
            quantity_grades = 0
            for grade_results in other.grades.values():
                for each_grade in grade_results:
                    sum_grades += int(each_grade)
                    quantity_grades += 1
            other_everage_grades = round(sum_grades / quantity_grades, 2)
        return self_everage_grades < other_everage_grades


# Создание экземпляров классов и применение методов для наполнения их данными
tutor_1 = Lecturer('Петр', 'Учителев')
tutor_1.courses_attached += ['Питон']
tutor_1.courses_attached += ['С++']
tutor_2 = Lecturer('Алексей', 'Преподавателев')
tutor_2.courses_attached += ['Питон']
tutor_2.courses_attached += ['С++']
reviewer_1 = Reviewer('Руслан', 'Ревизоров')
reviewer_2 = Reviewer('Максим', 'Ревизин')
reviewer_1.courses_attached += ['Питон']
reviewer_1.courses_attached += ['С++']
reviewer_2.courses_attached += ['Питон']
reviewer_2.courses_attached += ['С++']
student_1 = Student('Иван', 'Харин', 'мужской')
student_1.courses_in_progress += ['Питон']
student_1.courses_in_progress += ['С++']
student_1.finished_courses += ['Git']
student_1.rate_lecturer(tutor_1, 'Питон', '10')
student_1.rate_lecturer(tutor_2, 'Питон', '8')
student_2 = Student('Андрей', 'Смирнов', 'мужской')
student_2.courses_in_progress += ['Питон']
student_2.courses_in_progress += ['С++']
student_2.rate_lecturer(tutor_1, 'Питон', '9')
student_2.rate_lecturer(tutor_2, 'Питон', '8')
student_3 = Student('Ольга', 'Павлова', 'женский')
student_3.courses_in_progress += ['С++']
student_3.rate_lecturer(tutor_1, 'С++', '8')
student_3.rate_lecturer(tutor_2, 'С++', '7')
reviewer_1.rate_hw(student_1, 'Питон', '7')
reviewer_2.rate_hw(student_1, 'Питон', '8')
reviewer_1.rate_hw(student_1, 'С++', '10')
reviewer_2.rate_hw(student_1, 'С++', '8')
reviewer_1.rate_hw(student_2, 'Питон', '9')
reviewer_2.rate_hw(student_2, 'Питон', '10')
reviewer_2.rate_hw(student_2, 'С++', '7')
students = [student_1, student_2]
tutors = [tutor_1, tutor_2]


# Функция для нахождения средней оценки за домашние задания всех студентов, в зависимости от курса
def average_hw(students_list, course):
    sum_grades = 0
    quantity_grades = 0
    for every_student in students_list:
        for course_name, grade_results in every_student.grades.items():
            if course_name == course:
                for each_grade in grade_results:
                    sum_grades += int(each_grade)
                    quantity_grades += 1
    return round(sum_grades / quantity_grades, 2)


# Функция для нахождения средней оценки за лекции всех лекторов, в зависимости от курса
def average_cg(tutors_list, course):
    sum_grades = 0
    quantity_grades = 0
    for tutor in tutors_list:
        for course_name, grade_results in tutor.grades.items():
            if course_name == course:
                for each_grade in grade_results:
                    sum_grades += int(each_grade)
                    quantity_grades += 1
    return round(sum_grades / quantity_grades, 2)


print(tutor_1)
print('\n')
print(tutor_2)
print('\n')
print(student_1)
print('\n')
print(student_2)
print('\n')
print(f'Средняя оценка за лекции у лектора {tutor_1.surname} меньше, чем у лектора {tutor_2.surname} - '
      f'это {tutor_1 < tutor_2}')
print(f'Средняя оценка за домашние задания у студента {student_1.surname} меньше, чем у студента {student_2.surname} - '
      f'это {student_1 < student_2}')
print(f'Средняя оценка за все домашние задания по всем студентам по курсу Python '
      f'равна {average_hw(students, "Питон")}')
print(f'Средняя оценка за лекции всех лекторов по курсу Python '
      f'равна {average_cg(tutors, "Питон")}')

#  добавим возможность сравнения персонажей
#     def __lt__(self, other):
#         if not isinstance(other, Character):
#             print('Not a Character!')
#             return
#         return self.power < other.power
#
#     def __str__(self):
#         res = f'Сила персонажа = {self.power}'
#         return res
#
#
# peter_parker = SpiderMan('Peter Parker', 80)
# miles_morales = SpiderMan('Miles Morales', 85)

# print(peter_parker < miles_morales)
# и даже "больше" будет работать!
# print(peter_parker > miles_morales)
# print(peter_parker.__lt__(miles_morales))

# print(peter_parker)
# print(miles_morales)

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
