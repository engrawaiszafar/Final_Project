from tkinter import *
from Grade_Algorithm import grade_algo
from Store_Grades import *


def clear_fields() -> None:
    """
    * This method clears all the data that user enters in the application
    :return: None
    """
    score_input.delete(0, END)
    score_input.delete(0, END)
    first_name_input.delete(0, END)
    last_name_input.delete(0, END)
    id_input.delete(0, END)


def calc_grade() -> None:
    """
    * This method is used to calculate the student grades by calling grade_algo() method.
    * Stores those grades into grades.csv file by calling add_data() method.
    :return: None
    """
    score = score_input.get()
    first_name = first_name_input.get()
    last_name = last_name_input.get()
    id = id_input.get()
    grade = ''
    if first_name.strip() == '' or last_name.strip() == '' or id.strip() == '' or score.strip() == '':
        show_grade.config(fg="red", text="INVALID INPUT. Please provide all the inputs")
        return
    try:
        # try to convert string to int
        score = float(score)
    except:
        # change show grade to invalid input
        show_grade.config(fg="red", text="INVALID INPUT. Score should only be numbers.")
        score_input.delete(0, END)
        print("Error")

    if grade_algo(score, show_grade) != 'X':
        grade = grade_algo(score, show_grade)
    else:
        show_grade.config(fg="red", text="INVALID INPUT. Scores can be between 0-100")
        print("Error")
        score_input.delete(0, END)
        return

    add_data(id, first_name, last_name, score, grade, show_grade)
    clear_fields()


# setup window
window = Tk()

# setup size
window.geometry("600x600")
# set title
window.title("Grade Calculator")
# false to resize
window.resizable(False, False)

# id label
id_lable = Label(window, text="Enter Student ID:", font=("Courier", 15))
id_lable.pack()
# id input
id_input = Entry(window, width=10, font=("Courier", 15))
id_input.pack(pady=(10, 25))

# First Name label
first_name_lable = Label(window, text="Enter Your First Name:", font=("Courier", 15))
first_name_lable.pack()
# First name input
first_name_input = Entry(window, width=10, font=("Courier", 15))
first_name_input.pack(pady=(10, 25))

# Last Name label
last_name_lable = Label(window, text="Enter Your Last Name:", font=("Courier", 15))
last_name_lable.pack()
# Last name input
last_name_input = Entry(window, width=10, font=("Courier", 15))
last_name_input.pack(pady=(10, 25))

# score lable
score_lable = Label(window, text="Enter Your Score:", font=("Courier", 15))
score_lable.pack()
# score input
score_input = Entry(window, width=10, font=("Courier", 15))
score_input.pack(pady=(10, 25))

# calculate Button
grade_calc = Button(window, text="Add Grade", height=3, width=20, command=calc_grade)
grade_calc.pack(side="bottom", pady=50)

# show grade Frame
grade_frame = Frame(window)
# show grade lable
show_grade = Label(grade_frame, text=" ", font=("Courier", 15))
show_grade.pack(side="bottom")
grade_frame.pack(side="bottom", pady=0)

window.mainloop()
