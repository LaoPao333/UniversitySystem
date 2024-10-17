from errors.add_course_error import course_error

class course:
    def __init__(self):
        self.courses = {}
    def add_course(self, ui, Course): # Функция добавления курса
        if ui == "3":
            course_name = input("Введите название курса : ")
            if course_name == "":
                return
            next = course_error(course_name, Course)
            if next == True:
                self.courses[course_name] = {"Students": [], "Преподаватели": [], "Оценки": {}}
                print("Курс успешно создан! \n----------------------")
                print(self.courses) 
