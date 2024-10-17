def view_student_error(course_name, Course):
    if course_name not in Course.courses: # Проверка на существование курса
        print("Такого курса не существует! \n-------------------")
        
    elif Course.courses[course_name]["Students"] == []: # Проверка на пустоту курса
        print("В курсе нет преподавателей! \n-------------------")
    else:
        return True
    return False