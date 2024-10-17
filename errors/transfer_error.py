from user_input.course_create import course
def transfer_of_students_error(course_name, name, another_course_name, Course):    
    if course_name not in Course.courses: # Проверка на существование курса
        print("Такого курса нет! \n-------------------")
        
    elif name not in Course.courses[course_name]["Students"]: # Проверка на существование ученика
        print("Такого ученика нет! \n-------------------")
        
    elif another_course_name not in Course.courses: # Проверка на существование второго курса на который будет переведён
        print("Курса на который вы хотите перевести учеников нет! \n-----------------")
        
    elif name in Course.courses[another_course_name]["Students"]: # Проверка на перевод ученика на тот же курс
        print("Вы пытаетесь перевести ученика на тот же курс! \n-----------------")
    else:
        return True
    return False