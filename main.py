from user_input.course_create import course
from user_input.register import reg
from user_input.course_login import course_login
from user_input.add_teacher import add_teacher
from user_input.add_rate import rate_add
from user_input.view_ratings import view
from user_input.transfer_of_students import transfer_students
from user_input.view_students import view_students_on_course
from user_input.view_teachers import view_teachers_on_course

opened_or_closed = True

Reg = reg()

Course = course()

while opened_or_closed == True:
    ui = input("Система: Выберите действие \n1:Зарегистрироватся \n2:Войти в курс \n3:Создать курс \n4:Назначить преподователя \n5:Вывод оценок\n"
               "6:Перевод студентов на другой курс \n7:Просмотр истории оценок \n8:Просмотр списка студентов на курсе"
               "\n9:Просмотр списка преподавателей на курсе \n0:Добавить оценку"
               "\n    --->>")
    if ui != "0" and ui != "1" and ui != "2" and ui != "3" and ui != "4" and ui != "5" and ui != "6" and ui != "7" and ui != "8" and ui != "9":
        break
    Reg.add_student(ui) # Функция регистрации 1
    course_login(ui, Reg, Course) # Функция авторизации в курс 2
    Course.add_course(ui, Course) # Функция создания курса 3 
    add_teacher(ui, Course) # Функция назначения преподователя 4
    view(ui, Course) # Функция вывода оценок 5
    transfer_students(ui, Course) # Функция перевода студентов на другой курс 6
    view_students_on_course(ui, Course) # Функция просмотра списка студентов на курсе 7
    view_teachers_on_course(ui, Course) # Функция просмотра списка преподавателей на курсе 8
    rate_add(ui, Course) # Функция добавления оценок 9


    # Далее идёт вызов функций, где в каждой функции стоит условие, если ui == числу , то выполняется код. else: пропуск.
    
 