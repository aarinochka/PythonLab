import random

class Faculty:
    name: str
    departments: dict
    disciplines: dict
    specialties: list
    students: dict

    def __init__(self, name):
        self.name = name
        self.departments = {}
        self.disciplines = {}
        self.specialties = []
        self.students = {}

    def find_student_po_id(self, id):
        if id in self.students:
            return self.students[id]
        else:
            raise Exception(f"cтудент с id {id} не найден")

    def add_specialty(self, name):
        if name not in self.specialties:
            self.specialties.append(name)

    def add_student_na_specialty(self, id, name, specialty, semester):
        if id in self.students:
            raise Exception(f"уже есть студент с id {id} - {self.students[id].name}")
        if semester > 8 or semester < 1:
            raise Exception(f"нет семестра {semester}")
        if specialty in self.specialties:
            new_student = Student(id, name, specialty, self, semester)
            print(
                f"Студент {new_student.name} ({new_student.id}) зачислен на специальность {new_student.specialty}"
            )
            self.students[id] = new_student
        else:
            raise Exception(f"на факультете {self.name} нет специальности {specialty}")

    def remove_student(self, id):
        removed_student = self.find_student_po_id(id)
        removed_student.new_disciplines.clear()
        removed_student.old_disciplines.clear()
        del self.students[id]
        print(f"Студент {removed_student.name} ({removed_student.id}) отчислен")

    def add_discipline(self, id, name_discipline):
        student = self.find_student_po_id(id)
        discipline_find = False
        discipline_find_specialty = False
        for department in self.departments.values():
            for discipline in department.disciplines.values():
                if name_discipline == discipline.name:
                    discipline_find = True
                    
                    if (student.specialty in discipline.specialties_semester 
                        and student.semester in discipline.specialties_semester[student.specialty]):
                        key = (discipline, student.semester)
                        if key not in student.new_disciplines:
                            student.new_disciplines[key] = 0
                            discipline_find_specialty = True
                            print(f"{student.name} ({student.id}) зачислен на дисциплину {discipline.name} на кафедре {department.name}")
                            return
                        else:
                            raise Exception(f"{student.name} ({student.id}) уже изучает дисциплину {discipline.name}")
                            
        if not discipline_find:
            raise Exception(f"дисциплина {name_discipline} не найдена")
        elif not discipline_find_specialty:
            raise Exception(f"дисциплина {name_discipline} не читается для специальности {student.specialty} в {student.semester} семестре")
      
             
      

    def remove_student_dicsipline(self, id, name_discipline):
        student = self.find_student_po_id(id)
        student.remove_discipline(name_discipline)

    def set_student_mark(self, id, name_discipline, mark):
        student = self.find_student_po_id(id)
        student.discipline_mark(name_discipline, mark)

    def perevod_student(self, id):
        student = self.find_student_po_id(id)
        student.perevod()

    def vvod_marks(self, student):
        
        print(f"Введите оценки для {student.name} ({student.specialty}, {student.semester}):")
        student_disciplines = []
        for department in self.departments.values():
            for discipline in department.disciplines.values():
                if student.specialty in discipline.specialties_semester:
                    for discipline_sem in discipline.specialties_semester[student.specialty]:
                        if discipline_sem <= student.semester:
                            student_disciplines.append((discipline_sem, discipline))

        if not student_disciplines:
            print("Для этого студента пока нет доступных дисциплин.")
            return
        student_disciplines.sort(key=lambda x: x[0])
        for semester, discipline in student_disciplines:
            mark = 0
            key = (discipline, semester)
            if key in student.new_disciplines:
                mark = student.new_disciplines[key]
            elif key in student.old_disciplines:
                mark = student.old_disciplines[key]
            if not(mark == 0):
                if semester == student.semester:
                    print(f"По {discipline.name} ({semester}) уже стоит {mark}")
                continue
            else:
                if semester == student.semester:
                    while True:
                        mark = input(f"{discipline.name} ({semester}): ") 
                        if not (mark == '') :
                            mark = int(mark)
                        else:
                            mark = 0
                        if not (0 <= mark <= 10):
                            raise Exception("Оценка должна быть от 0 до 10")                            
                        student.new_disciplines[key] = mark
                        break
                elif semester < student.semester:
                    student.old_disciplines[key] = random.randint(4,10)


    def vedomoct_studenta(self, id):
        student = self.find_student_po_id(id)
        self.vvod_marks(student)
        with open(f"lab_2.txt", "w", encoding="utf-8") as f:
            f.write(f"Ведомость {student.name} ({student.id})\n")
            f.write(f"Специальность: {student.specialty}\n")
            f.write(f"Семестр: {student.semester}\n")
            summa = 0
            count = 0
            for key, mark in student.old_disciplines.items():
                discipline = key[0]
                semester = key[1]
                f.write(f"{discipline.name} ({discipline.department.name}, {semester}): {mark}\n")
                summa += mark
                count += 1
            for key, mark in student.new_disciplines.items():
                discipline = key[0]
                semester = key[1]
                f.write(f"{discipline.name} ({discipline.department.name}, {semester}): {mark}\n")
                if not (mark == 0): 
                    summa += mark
                    count += 1
            if not (summa == 0) and not (count ==0):
                f.write(f"Средний балл: {(summa/count):.2f}\n")
            else:
                f.write(f"Средний балл: 0.00\n")

    def vedomost_discipline(self, name_discipline):
        find_discipline = None
        for department in self.departments.values():
            if name_discipline in department.disciplines:
                find_discipline = department.disciplines[name_discipline]
                break
                
        if not find_discipline:
            raise Exception(f"Дисциплина '{name_discipline}' не найдена на факультете.") 
        for student in self.students.values():
            if student.specialty in find_discipline.specialties_semester:
                for discipline_sem in find_discipline.specialties_semester[student.specialty]:
                    if discipline_sem < student.semester:
                        key = (find_discipline, discipline_sem)
                        if key not in student.old_disciplines and key not in student.new_disciplines:
                            student.old_disciplines[key] = random.randint(4, 10)
        students_data = [] 
        summa = 0
        count = 0
        for student in self.students.values():
            for key, mark in student.old_disciplines.items():
                discipline, sem = key
                if discipline == find_discipline:
                    students_data.append((student, mark, sem))
                    summa += mark
                    count += 1
            for key, mark in student.new_disciplines.items():
                discipline, sem = key
                if discipline == find_discipline:
                    students_data.append((student, mark, sem))
                    if mark != 0:
                        summa += mark
                        count += 1
        with open("lab_2.txt", "w", encoding="utf-8") as f:
            f.write(f"Ведомость {name_discipline}:\n")
            f.write(f"Читающая кафедра: {find_discipline.department.name}\n")
            if not(count == 0) and not (summa ==0):
                f.write(f"Средний балл: {(summa/count):.2f}\n")
            else:
                f.write("Средний балл: 0.00\n")
            f.write("Список студентов:\n")
            if not students_data:
                f.write("  Нет студентов, изучающих/изучивших данную дисциплину.\n")
            else:
                for student, mark, sem in students_data:
                    f.write(f"{student.name} ({student.id}) ({student.specialty}, {student.semester}): {mark}\n")


class Department:
    name: str
    faculty: Faculty
    disciplines: dict

    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty
        self.disciplines = {}
        self.faculty.departments[self.name] = self


class Discipline:
    name: str
    department: Department
    specialties_semester: dict

    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.specialties_semester = {}
        self.department.disciplines[self.name] = self

    def set_specialty_semester(self, specialty, semester):
        if specialty not in self.specialties_semester:
            self.specialties_semester[specialty] = []
        if semester not in self.specialties_semester[specialty]:
            self.specialties_semester[specialty].append(semester)


class Student:
    id : str
    name : str
    specialty : str
    faculty : Faculty
    semester : int
    new_disciplines : dict
    old_disciplines : dict

    def __init__(self, id, name, specialty, faculty, semester):
        self.id = id
        self.name = name
        self.specialty = specialty
        self.faculty = faculty
        self.semester = semester
        self.new_disciplines = {}
        self.old_disciplines = {}
        self.faculty.students[self.id] = self

    def remove_discipline(self, name_discipline):
        removed_key = None
        for key in self.new_disciplines.keys():
            discipline = key[0]
            if discipline.name == name_discipline:
                removed_key = key
                break
        if removed_key:
            del self.new_disciplines[removed_key]
            print(
                f"Студент {self.name} ({self.id}) удален из списка изучающих дисциплину {name_discipline}"
            )
        else:
            raise Exception(
                f"студент {self.name} ({self.id}) не изучет дисциплину {name_discipline}"
            )

    def discipline_mark(self, name_discipline, mark):
        discipline_find = False
        if mark > 10 or mark < 1:
            raise Exception(f"оценки {mark} не существует")
        for key in self.new_disciplines:
            discipline = key[0]
            if name_discipline == discipline.name:
                self.new_disciplines[key] = mark
                discipline_find = True
                print(
                    f"Студенту {self.name} ({self.id}) выставлена оценка {mark} по дисциплине {name_discipline}"
                )
                break
        if not discipline_find:
            raise Exception(
                f"студент {self.name} ({self.id}) не изучет дисциплину {name_discipline}"
            )

    def perevod(self):
        for mark in self.new_disciplines.values():
            if mark is None:
                raise Exception(f"студент {self.name} ({self.id}) не сдал все предметы")
            if mark < 4:
                raise Exception(f"студент {self.name} ({self.id}) имеет {mark}")

        self.old_disciplines.update(self.new_disciplines)
        self.new_disciplines.clear()
        if self.semester != 8:
            self.semester += 1
            print(f"Студент {self.name} ({self.id}) переведен на {self.semester}")
        else:
            print(f"Студент {self.name} ({self.id}) окончил университет")

        



    


fac = Faculty("РФиКТ")

dep_ics = Department("Кафедра информатики и компьютерных систем", fac)
dep_is = Department("Кафедра интеллектуальных систем", fac)
dep_tit = Department("Кафедра телекоммуникаций и ИТ", fac)
dep_phys = Department("Кафедра физики и аэрокосмических технологий", fac)
dep_math = Department("Кафедра высшей математики", fac)
dep_hum = Department("Кафедра гуманитарных наук", fac)
dep_lang = Department("Кафедра иностранных языков", fac)
dep_diploma = Department("Кафедра дипломного проектирования", fac)

fac.add_specialty("ПИ")
fac.add_specialty("КБ")
fac.add_specialty("РФ")

disciplines_map = {
    dep_math: [
        ("Аналитическая геометрия и линейная алгебра", "РФ", 1),
        ("Математический анализ", "КБ", 1),
        ("Дискретная математика", "КБ", 1),
        ("Дискретная математика", "ПИ", 1),
        ("Математический анализ", "ПИ", 1),
        ("Математический анализ", "РФ", 2),
        ("Аналитическая геометрия и линейная алгебра", "КБ", 2),
        ("Аналитическая геометрия и линейная алгебра", "ПИ", 2),
        ("Дифференциальные уравнения", "РФ", 3),
        ("Дифференциальные уравнения", "КБ", 3),
        ("Теория вероятностей и математическая статистика", "КБ", 3),
        ("Теория вероятностей и математическая статистика", "ПИ", 3),
        ("Численные методы", "РФ", 4),
        ("Теория колебаний и волн", "РФ", 5),
    ],
    dep_ics: [
        ("C++", "РФ", 2),
        ("C++", "КБ", 2),
        ("C++", "ПИ", 2),
        ("Python", "РФ", 3),
        ("Java", "КБ", 3),
        ("Python", "ПИ", 3),
        ("Java", "ПИ", 3),
        ("Программирование микроконтроллеров", "РФ", 5),
        ("Архитектура компьютера", "РФ", 5),
        ("Микропроцессоры", "КБ", 5),
        ("Микропроцессоры", "ПИ", 5),
        ("Параллельные вычисления и программирование", "КБ", 7),
    ],
    dep_is: [
        ("Искусственный интеллект и методы машинного обучения", "КБ", 4),
        ("Искусственный интеллект и методы машинного обучения", "ПИ", 4),
        ("Методы оптимизации и исследование операций", "КБ", 6),
        ("Методы оптимизации и исследование операций", "ПИ", 6),
        ("Биоинформатика", "ПИ", 6),
        ("Обработка данных в киберфизических и интеллектуальных системах", "ПИ", 6),
    ],
    dep_tit: [
        ("Компьютерные сети", "КБ", 5),
        ("Компьютерные сети", "ПИ", 5),
        ("Операционные системы", "КБ", 5),
        ("Безопасность информационных систем", "КБ", 6),
        ("Системы мобильной связи", "РФ", 7),
        ("Технические средства и методы защиты информации", "ПИ", 7),
        ("Цифровая обработка сигналов", "ПИ", 7),
    ],
    dep_phys: [
        ("Механика", "РФ", 1),
        ("Механика", "КБ", 1),
        ("Электричество и магнетизм", "КБ", 2),
        ("Квантовая физика", "РФ", 4),
        ("Интегральная электроника", "КБ", 4),
        ("Интегральная электроника", "ПИ", 4),
        ("Термодинамика и статистическая физика", "ПИ", 5),
        ("Прикладная электродинамика", "РФ", 6),
        ("Прикладная электродинамика", "КБ", 6),
        ("Теория колебаний и волн", "РФ", 6),
        ("Статистическая радиофизика и теория информации", "РФ", 6),
        ("Квантовая радиофизика", "РФ", 7),
        ("Статистическая радиофизика", "КБ", 7),
        ("Статистическая радиофизика", "ПИ", 7),
    ],
    dep_hum: [
        ("История белорусской государственности", "РФ", 1),
        ("История белорусской государственности", "ПИ", 1),
        ("Современная политэкономия", "РФ", 3),
        ("Философия", "РФ", 4),
        ("Философия", "КБ", 4),
    ],
    dep_lang: [
        ("Английский язык", "РФ", 2),
        ("Английский язык", "ПИ", 2),
        ("Английский язык", "ПИ", 4),
    ],
    dep_diploma: [
        ("Преддипломная практика", "РФ", 8),
        ("Подготовка дипломной работы", "РФ", 8),
        ("Защита дипломной работы", "РФ", 8),
        ("Преддипломная практика", "КБ", 8),
        ("Подготовка дипломной работы", "КБ", 8),
        ("Защита дипломной работы", "КБ", 8),
        ("Преддипломная практика", "ПИ", 8),
        ("Подготовка дипломной работы", "ПИ", 8),
        ("Защита дипломной работы", "ПИ", 8),
    ],
}


for department, subjects_list in disciplines_map.items():
    for disc_name, specialty, semester in subjects_list:
        
        if disc_name in department.disciplines:
            existing_disc = department.disciplines[disc_name]
            existing_disc.set_specialty_semester(specialty, semester)
        else:
            new_disc = Discipline(disc_name, department)
            new_disc.set_specialty_semester(specialty, semester)

students = [
    "Азарчик",
    "Аптыкаева",
    "Банчук",
    "Бардышев",
    "Глебко",
    "Гурский",
    "Есеневиич",
    "Кивель",
    "Комалов",
    "Коровайко",
    "Лопухов",
    "Макуркин",
    "Мадаховский",
    "Маляревич",
    "Марко",
    "Мацкевич",
    "Мирчук",
    "Мурков",
    "Пахомов",
    "Радьков",
    "Станчик",
    "Тихонова",
    "Ясюк",
    "Байрамов",
]
for i in range(1, len(students) + 1):
    if i < 9:
        new_student = Student(str(i), students[i - 1], "ПИ", fac, i)
    elif i < 17:
        new_student = Student(str(i), students[i - 1], "КБ", fac, i % 8 + 1)
    else:
        new_student = Student(str(i), students[i - 1], "РФ", fac, i % 8 + 1)


while True:
    metod = input("""1. Зачисление студента на специальность
2. Отчисление студента
3. Добавление на изучение дисциплины
4. Удаление из списка дисциплин
5. Выставление отметки
6. Перевод в следующий семестр
7. Сформировать ведомость студента 
8. Сформировать ведомость по дисциплине
(Нажмите Enter для выхода)
Введите номер метода: """)

    if metod == "":
        print("Выход из программы.")
        break
    try:
        if metod == "1":
            id = input("Введите id студента: ")
            name = input("Введите имя студента: ")
            print(f"Специальности: {fac.specialties}")
            specialty = input("Введите название специальности: ")
            semester = int(input("Введите семестр: "))
            fac.add_student_na_specialty(id, name, specialty, semester)

        elif metod == "2":
            id = input("Введите id студента: ")
            fac.remove_student(id)

        elif metod == "3":
            id = input("Введите id студента: ")
            name_discipline = input("Введите название дисциплины: ")
            fac.add_discipline(id, name_discipline)

        elif metod == "4":
            id = input("Введите id студента: ")
            name_discipline = input("Введите название дисциплины: ")
            fac.remove_student_dicsipline(id, name_discipline)

        elif metod == "5":
            id = input("Введите id студента: ")
            name_discipline = input("Введите название дисциплины: ")
            mark = int(input("Введите оценку: "))
            fac.set_student_mark(id, name_discipline, mark)

        elif metod == "6":
            id = input("Введите id студента: ")
            fac.perevod_student(id)

        elif metod == "7":
            id = input("Введите id студента: ")
            fac.vedomoct_studenta(id)

        elif metod == "8":
            name_discipline = input("Введите название дисциплины: ")
            fac.vedomost_discipline(name_discipline)

        else:
            print(f"Метода {metod} нет. Попробуйте снова.")

    except Exception as e:
        print(f"Ошибка: {e}")
