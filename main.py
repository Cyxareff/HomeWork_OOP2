class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in lecturer.courses_attached \
                and course in self.courses_in_progress \
                and grade <= 10:
            lecturer.grades += [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        sum_hw = 0
        count = 0
        for grades in self.grades.values():
            sum_hw += sum(grades)
            count += len(grades)
        return round(sum_hw / count, 2)

    def __str__(self):
        res = f'Студент \n' \
              f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за ДЗ: {self.get_avg_grade()} \n' \
              f'Курс в процессе изучения: {",".join(self.courses_in_progress)} \n' \
              f'Завершенные курсы: {",".join(self.finished_courses)} \n'
        return res

    def __lf__(self, other_student):
        if not isinstance(other_student, Student):
            print('Такого студента нет')
            return
        else:
            if self.get_avg_grade() < other_student.get_avg_grade():
                print(f'{self.name} {self.surname} учиться хуже чем {other_student.name} {other_student.surname}')
            else:
                print(f'{self.name} {self.surname} учиться лучше чем {other_student.name} {other_student.surname}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress \
                and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Проверяющий \n' \
              f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        res = f'Лектор \n' \
              f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за лекции: {sum(self.grades) / len(self.grades): .2f} \n'
        return res

    def __lf__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Такого лектора нет')
            return
        if sum(self.grades) / len(self.grades) > sum(other_lecturer.grades) / len(other_lecturer.grades):
            print(f'{self.name} {self.surname} преподает лучше чем {other_lecturer.name} {other_lecturer.surname}')
        else:
            print(f'{self.name} {self.surname} преподает хуже чем {other_lecturer.name} {other_lecturer.surname} ')


best_student = Student('Ivan', 'Ivanov', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в програмирование']
next_student = Student('Boris', 'Petrov', 'male')
next_student.courses_in_progress += ['Python']
next_student.courses_in_progress += ['Git']
next_student.finished_courses += ['Изучения языка C++']

cool_reviewer = Reviewer('Alex', 'Smirnoff')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
next_reviewer = Reviewer('Sebastian', 'Fish')
next_reviewer.courses_attached += ['Python']
next_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Git', 6)
cool_reviewer.rate_hw(best_student, 'Git', 7)
cool_reviewer.rate_hw(best_student, 'Git', 4)

next_reviewer.rate_hw(best_student, 'Python', 7)
next_reviewer.rate_hw(best_student, 'Python', 3)
next_reviewer.rate_hw(best_student, 'Python', 4)
next_reviewer.rate_hw(best_student, 'Git', 5)
next_reviewer.rate_hw(best_student, 'Git', 2)
next_reviewer.rate_hw(best_student, 'Git', 4)

cool_reviewer.rate_hw(next_student, 'Python', 2)
cool_reviewer.rate_hw(next_student, 'Python', 4)
cool_reviewer.rate_hw(next_student, 'Python', 3)
cool_reviewer.rate_hw(next_student, 'Git', 4)
cool_reviewer.rate_hw(next_student, 'Git', 6)
cool_reviewer.rate_hw(next_student, 'Git', 2)

next_reviewer.rate_hw(next_student, 'Python', 6)
next_reviewer.rate_hw(next_student, 'Python', 7)
next_reviewer.rate_hw(next_student, 'Python', 3)
next_reviewer.rate_hw(next_student, 'Git', 5)
next_reviewer.rate_hw(next_student, 'Git', 4)
next_reviewer.rate_hw(next_student, 'Git', 6)

# print(best_student.grades)
# print(next_student.grades)

cool_lecturer = Lecturer('Jhon', 'Smit')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
next_lecturer = Lecturer('Samanta', 'Fox')
next_lecturer.courses_attached += ['Python']
next_lecturer.courses_attached += ['Git']

best_student.rate_lecturer(cool_lecturer, 'Python', 6)
best_student.rate_lecturer(cool_lecturer, 'Git', 7)
best_student.rate_lecturer(next_lecturer, 'Python', 5)
best_student.rate_lecturer(next_lecturer, 'Git', 6)
next_student.rate_lecturer(cool_lecturer, 'Python', 8)
next_student.rate_lecturer(cool_lecturer, 'Git', 9)
next_student.rate_lecturer(next_lecturer, 'Python', 5)
next_student.rate_lecturer(next_lecturer, 'Git', 5)

print(cool_lecturer, end='')
print(cool_lecturer.__lf__(next_lecturer))
print()
print(next_lecturer, end='')
print(next_lecturer.__lf__(cool_lecturer))
print()
print(cool_reviewer)
print(next_reviewer)
print()
print(best_student, end='')
print(best_student.__lf__(next_student))
print()
print(next_student, end='')
print(next_student.__lf__(best_student))
print()


def get_avg_hw_grade(student_list, course):
    total_sum = 0
    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                total_sum += sum(grades) / len(grades)
            return round(total_sum / len(student_list), 1)


print(
    f'Средняя оценка на курсе: {"Python"}, за ДЗ по всем студентам:'
    f' {get_avg_hw_grade([best_student, next_student], "Python")}')


def get_avg_lecturer_grade(lecturer_list, course):
    total_sum = 0
    for lecturer in lecturer_list:
        total_sum += sum(lecturer.grades) / len(lecturer.grades)
    return round(total_sum / len(lecturer_list), 1)


print(
    f'Средняя оценка на курсе: {"Python"}, за лекции по всем лекторам:'
    f' {get_avg_lecturer_grade([cool_lecturer, next_lecturer], "Python")}')
