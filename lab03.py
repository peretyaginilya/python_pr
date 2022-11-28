class Employer:  # Создание класса "Сотрудник"
    def __init__(self,  name, jobtitle, specialization,work):
        self.name = name
        self.jobtitle = jobtitle
        self.specialization = specialization
        self.work = work

    def setname(self, name):  # Функция, предназначеная для присвоения данных объекту
        self.name = name
        print('Присвоено ФИО сотруднику:', name)

    def setjobtitle(self, jobtitle):
        self.jobtitle = jobtitle
        print('Присвоена должность сотруднику:', jobtitle)

    def setspecialization (self, specialization):
        self.specialization = specialization
        print('Специализация:', specialization)

    def setwork(self, work):
        self.work = work
        print('Присвоение вып. заданий:', work)

    def __repr__(self): # Может возращать как строки, так и словари
        return {'ФИО': self.name, 'Должность': self.jobtitle, 'Специализация:' : self.specialization,
                'Количество вып. заданий:' : self.work}

    def __str__(self): # Возвращает строки
        return 'Employer(ФИО:' + self.name + ', Должность' + self.jobtitle + ', Специализация:' + self.specialization+\
               ', Количество вып. заданий:' + self.work + ')'

class id_employer:  # Инциализация счетчика
    def __init__(self):
        self.id_employer = 0

    def __call__(self, *args, **kwargs):
        self.id_employer +=1
        return self.id_employer


def view(self):  # Создание функции, визуализирующей информацию об объектах
    print('Информация о сотруднике:', self.name, self.jobtitle, self.specialization, self.work)


example = Employer('Петров Иван Иванович', 'Инженер-конструктор', 'Администратор автоматизированных систем', '0')
example.setjobtitle('Главный инженер')  # Изменение данных объекта
view(example)

print(type(example.__str__()))
print(type(example.__repr__()))

id = id_employer()
print(id())
