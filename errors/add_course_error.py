def course_error(course_name, Course):
    if not course_name.isalpha(): # Проверка на буквы
        print("В курсе должны быть только БУКВЫ! \n-------------------")
    elif course_name in Course.courses: # Проверка на уникальность курсов
        print("Такой курс уже существует! \n-------------------")
    else:
        return True
    return False