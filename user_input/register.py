from errors.add_student_error import student_error

class reg:
    def __init__(self):
        self.accounts = {}
        
    def add_student(self, ui):
        if ui == "1": # Проверка на выбор действия
            name = input("Ваше имя: ")
            password = input("Создайте ваш пароль, не менее шести символов: ")
            if name == "" or password == "":
                return
            next = student_error(name, password) # Вызов функции, для обработки ошибок
            if next == True:
                self.accounts[name] = {"Пароль": password}
                print(f"Аккаунт создан! {name}\n---------------------")
                print(self.accounts)
                           