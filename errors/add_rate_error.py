from user_input.course_create import course
def rate_error(name, course_rate_name, rate, Course):
    if not rate.isdigit(): # Проверка на цифры
        print("Оценка должна состоять только из цифр \n-------------------")
        
    elif course_rate_name not in Course.courses: # Проверка на существование курса
        print("Такого курса не существует \n-------------------")
        
    elif Course.courses[course_rate_name]["Преподаватели"] == []: # Проверка, пуст ли список преподавателей
        print("Преподавателя нет! \n-------------------")
        
    elif name not in Course.courses[course_rate_name]["Students"]: # Проверка, существует ли ученик
        print("Такого ученика нет! \n-------------------")
    else:
        return True
    return False