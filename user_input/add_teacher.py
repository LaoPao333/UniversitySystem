from errors.add_teacher_error import teacher_error
from user_input.course_create import course
def add_teacher(ui, Course): # Функция записи учителя на курс
    if ui == "4":
        teacher_name = input("Введите имя преподавателя:")
        course_name = input("Введите название курса:")
        if teacher_name == "" or course_name == "":
            return
        next = teacher_error(teacher_name, course_name, Course)
        if next == True:
            Course.courses[course_name]["Преподаватели"].append(teacher_name)
            print(f"Преподаватель успешно добавлен! {teacher_name} \n {Course.courses} \n-----------------------")
            