def student_error(name, password):
    if not name.isalpha():
        print("Имя должно состоять только из букв! \n--------------") # Проверка на только буквы
        
    elif not password.isdigit():
        print("Пароль должен состоять только из цифр! \n------------") # Проверка на только цифры
        
    elif len(password) < 6:
        print("Пароль должен содержать не менее 6 символов! \n----------") # Проверка на минимальное содержание в 6 символов
    else:
        return True
    return False
        