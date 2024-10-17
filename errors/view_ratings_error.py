from user_input.course_create import course
def view_error(course_name, name, Course):
    if course_name not in Course.courses: # Проверка на существование курса
        print("Такого курса нет! \n-------------------")
        
    elif name not in Course.courses[course_name]["Students"]: # Проверка на существование ученика
        print("Такого ученика нет! \n-------------------")
        
    elif Course.courses[course_name]["Оценки"][name] == []: # Проверка , пуст ли список оценок
        print("Оценок нет! \n-------------------")
    else:
        return True
    return False
        