from errors.view_students_error import view_student_error
def view_students_on_course(ui, Course):
    if ui == "7":
        course_name = input("Введите название курса: ")
        if course_name == "":
            return
        next = view_student_error(course_name, Course)
        if next == True:
            print(f"Студенты на курсе на курсе > {Course.courses[course_name]['Students']} \n---------------------")