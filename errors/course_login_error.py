from user_input.register import reg
def login_error(course_name, name, password, Reg, Course):
    if name not in Reg.accounts: # Проверка на существование аккаунта
        print("Такого аккаунта не существует! \n-------------------")
        
    elif course_name not in Course.courses: # Проверка на существование курса
        print("Такого курса не существует! \n-------------------")
        
    elif name in Course.courses[course_name]: # Проверка на существование аккаунта в курсе
        print("Такой аккаунт уже в курсе! \n-------------------")
         
    elif password != Reg.accounts[name]["Пароль"]: # Проверка на правильность пароля
        print("Неправильный пароль! \n-------------------")
    else:
        return True 
    return False