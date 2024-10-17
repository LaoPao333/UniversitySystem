from errors.transfer_error import transfer_of_students_error
def transfer_students(ui, Course):
    if ui == "6":
        course_name = input("Введите название курса: ")
        name = input("Введите имя студента: ")
        another_course_name = input("Введите название другого курса: ")
        if course_name == "" or name == "" or another_course_name == "":
            return
        next = transfer_of_students_error(course_name, name, another_course_name, Course)
        if next == True:
            Course.courses[course_name]["Students"].remove(name)
            Course.courses[another_course_name]["Students"].append(name)
            print(f"Студент {name} переведен на курс {another_course_name} \n {Course.courses} \n-----------------------")
            