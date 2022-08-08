import csv
from os.path import exists


def file_exist(file_path) -> None:
    """
    This method checks if the file exist or not
    :param file_path: Path of the file
    :return: None
    """
    file_exists = exists(file_path)
    return file_exists


def is_duplicate(student_id) -> bool:
    """
    * This method is used to check the duplicate records in the file grades.csv.
    * It returns True if the record is duplicate
    :param student_id: Student ID that user wants to check for duplication
    :return: Boolean
    """
    duplicate = False
    if file_exist('grades.csv'):
        with open('grades.csv', 'r') as csvfile:
            dupsreader = csv.reader(csvfile, delimiter=',')
            datalist = list(dupsreader)
            n = len(list(datalist))
            print(f"{n} records")
            x = 0
            while x < n:
                if student_id == datalist[x][0]:  # duplicate?
                    duplicate = True
                    break
                x += 1
    return duplicate


def add_data(student_id, first_name, last_name, score, grades, show_grade) -> None:
    """
    * This method adds the below data into grades.csv file.
    * Student ID
    * First Name
    * Last Name
    * Score
    * Grades
    :param student_id: Student ID
    :param first_name: First Name
    :param last_name: Last Name
    :param score: Score (0-100)
    :param grades: Grades (A, B, C, D, F)
    :param show_grade: Used to configure the output on the application.
    :return: None
    """
    if is_duplicate(student_id):
        show_grade.config(fg='red', text=f'DUPLICATE RECORD. ID \'{student_id}\' already exists')
    else:
        with open('grades.csv', 'a', newline='') as csvfile:
            content = csv.writer(csvfile)
            content.writerow([student_id, first_name, last_name, score, grades])
            show_grade.config(fg="green", text="Record Successfully added into the csv file..")
