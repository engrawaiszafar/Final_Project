def grade_algo(score, show_grade) -> str:
    """
    This method is used to return the student grades based on the scores.
    :param score: int type. Student's score (0-100).
    :param show_grade: Used to configure the output on the application.
    :return: str type output. It returns the Student's grades (A, B, C, D, F or X for invalid input)
    """
    if score > 100 or score < 0:
        return "X"

    elif score >= 90 and score <= 100:
        show_grade.config(fg='black', text="Student's Grade is: A")
        return "A"

    elif score >= 80 and score < 90:
        show_grade.config(fg='black', text="Student's Grade is: B")
        return "B"

    elif score >= 70 and score < 80:
        show_grade.config(fg='black', text="Student's Grade is: C")
        return "C"

    elif score >= 60 and score < 70:
        show_grade.config(fg='black', text="Student's Grade is: D")
        return "D"

    else:
        show_grade.config(fg='black', text="Student's Grade is: F")
        return "F"
