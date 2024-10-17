from user_input.course_create import course

def teacher_error(teacher_name, course_name, Course):
    if not teacher_name.isalpha(): # Проверка на буквы
        print("Имя преподавателя может состоять только из букв \n-------------------")
        
    elif course_name not in Course.courses: # Проверка на существование курса
        print("Такого курса не существует \n-------------------")
        
    elif teacher_name in Course.courses[course_name]: # Проверка на существование преподавателя в курсе
        print("Такой преподаватель уже в курсе \n-------------------")
    else:
        return True