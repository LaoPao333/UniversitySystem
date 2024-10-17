from user_input.course_create import course
def view_teacher_error(course_name, Course):
    if course_name not in Course.courses: # Проверка на существование курса
        print("Такого курса не существует! \n-------------------")
    else:
        return True
    return False
    