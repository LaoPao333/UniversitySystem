from errors.add_rate_error import rate_error
from user_input.course_create import course
def rate_add(ui, Course):
    if ui == "9":
        name = input("Введите имя студента: ")
        course_rate_name = input("Введите название курса: ")
        rate = input("Введите оценку: ")
        if name == "" or course_rate_name == "" or rate == "":
            return
        next = rate_error(name, course_rate_name, rate, Course)
        if next == True:
            Course.courses[course_rate_name]["Оценки"][name].append(rate)
            print(f"Оценка успешно добавлена! {name} \n {Course.courses} \n-----------------------") 
              
        
            
