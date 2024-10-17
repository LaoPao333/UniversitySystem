from user_input.course_create import course
from errors.view_teachers_error import view_teacher_error
def view_teachers_on_course(ui, Course):
    if ui == "8":
        course_name = input("Введите название курса: ")
        if course_name == "":
            return
        next = view_teacher_error(course_name, Course)
        if next == True:
            print(f"Преподаватели на курсе > {Course.courses[course_name]['Преподаватели']} \n----------------------")