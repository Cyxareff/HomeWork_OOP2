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
        res = f'Имя: {self.name} \n' \
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
            compare = self.get_avg_grade() < other_student.get_avg_grade()
            if compare:
                print(f' {self.name} {self.surname} учиться хуже чем {other_student.name} {other_student.surname}')
            else:
                print(f'{other_student.name} {other_student.surname} учиться хуже чем {self.name} {self.surname}')
        return compare


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
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        res = f'Имя: {self.name} \n' \
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
            print(f'{other_lecturer.name} {other_lecturer.surname} преподает лучше чем {self.name} {self.surname}')


best_student = Student('Ivan', 'Ivanov', 'male')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']

next_student = Student('Boris', 'Petrov', 'male')
next_student.courses_in_progress += ['Python']
next_student.courses_in_progress += ['Git']

cool_reviewer = Reviewer('Alex', 'Smirnoff')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 5)

cool_reviewer.rate_hw(best_student, 'Git', 6)
cool_reviewer.rate_hw(best_student, 'Git', 7)
cool_reviewer.rate_hw(best_student, 'Git', 4)
