class university:
    def __init__(student, name, number_of_grade, grade1, grade2, grade3):
        student.name = name
        student.number_of_grade = number_of_grade
        student.grade1 = grade1
        student.grade2 = grade2
        student.grade3 = grade3

    def get_name(student):
        print("Student name is %s" % student.name)
        
    def get_grades(student):
        total_grade = student.grade1+student.grade2+student.grade3
        average = total_grade/student.number_of_grade
        print ("The Average is %i" % average)

Information = university("Hossein",3,16,12,18)
Information.get_name()
Information.get_grades()