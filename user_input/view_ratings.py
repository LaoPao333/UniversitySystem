from errors.view_ratings_error import view_error
def view(ui, Course):
    if ui == "5":
        course_name = input("Введите название курса: ")
        name = input("Введите имя: ")
        if course_name == "" or name == "":
            return
        next = view_error(course_name, name, Course)
        if next == True:
            for i, char in enumerate(Course.courses[course_name]["Оценки"][name]):
                print(f"{i+1} - {char}")
        