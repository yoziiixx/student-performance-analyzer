from data import Data
import numpy as np

data = Data(["Alex", "Sam", "Maya", "Noor"], ["Maths", "Chemistry", "Physics"])

while True:
    print()
    print("1- Enter or update a grade")
    print("2- View student ranking")
    print("3 - View student averages")
    print("4 - View subject averages")
    print("5 - View class average")
    print("6 - View student status")
    print("7 - View highest and lowest student")
    print("8 - View all grades")
    print("9- Exit")
    choice = input("Choice: ")

    if choice == "1":
        name = input("Student's name: ")
        subject = input("Student's subject: ")
        grade_text = input("Student's grade: ")
        try:
            print(data.enterGrade(name, subject, float(grade_text)))
        except ValueError as e:
            print(e)

    elif choice == "2":
        ranked_names, ranked_average = data.studentRanking()
        if ranked_names.size == 0:
            print("No students have complete grades yet.")
        else:
            for name, average in zip(ranked_names, ranked_average):
                print(f"{name} - {average:.2f}%")

    elif choice == "3":
        student_name = data.getNames()
        student_average = data.studentAverage()
        highest = data.studentHighestGrade()
        lowest = data.studentLowestGrade()
        status = data.studentStatus()

        for name, average, highest, lowest, status in zip(student_name, student_average, highest, lowest, status):
            if np.isnan(average):
                print(f"{name} - No grades yet")
            else:
                print(f"{name} | {average:.2f}% | {highest:.2f}% | {lowest:.2f}% | {status}")


    elif choice == "4":
        get_subject = data.getSubjects()
        get_subject_average = data.subjectAverage()

        for subject, average in zip(get_subject, get_subject_average):
            if np.isnan(average):
                print(f"{subject} - No grades yet")
            else:
                print(f"{subject} - {average:.2f}%")
    elif choice == "5":
        class_average = data.classAverage()
        if np.isnan(class_average):
            print(f"No grades yet")
        else:
            print(f"Average : {class_average:.2f}%")
    elif choice == "6":
        student_status = data.studentStatus()
        print("Pass:", student_status.count("Pass"))
        print("Fail:", student_status.count("Fail"))
        print("Incomplete:", student_status.count("Incomplete"))
    elif choice == "7":
        ranked_names,ranked_average = data.studentRanking()

        if ranked_names.size == 0:
            print("No students have complete grades yet.")
        else:
            highest = ranked_average[0]
            lowest = ranked_average[-1]

            top_names = ranked_names[ranked_average == highest]
            bottom_names = ranked_names[ranked_average == lowest]

            print(f"Highest: {', '.join(top_names)} - {highest:.2f}%")
            print(f"Lowest: {', '.join(bottom_names)} - {lowest:.2f}%")
    elif choice == "8":
        print("Student | " + " | ".join(data.getSubjects()))

        names = data.getNames()
        grades = data.getGrades()

        for i in range(len(names)):
            cells = [names[i]]
            for g in grades[i]:
                if np.isnan(g):
                    cells.append("—")
                else:
                    cells.append(f"{g:g}")
            print(" | ".join(cells))

    elif choice == "9":
        break
    else:
        print("Invalid choice")




