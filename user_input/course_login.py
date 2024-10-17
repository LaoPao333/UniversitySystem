from errors.course_login_error import login_error
from user_input.course_create import course


def course_login(ui, Reg, Course):
    if ui == "2": # Проверка на выбор действия
        course_name = input("Введите название курса: ")
        name = input("Введите ваше имя: ")
        password = input("Введите ваш пароль: ")
        if course_name == "" or name == "" or password == "":
            return
        next = login_error(course_name, name, password, Reg, Course) # Вызов функции, для обработки ошибок
        if next == True:
            Course.courses[course_name]["Students"].append(name)
            Course.courses[course_name]["Оценки"][name] = []
            print(f"Вы успешно вошли в курс {course_name} \n {Course.courses} \n----------------------")

            