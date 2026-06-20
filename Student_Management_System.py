# STUDENT MANAGEMENT SYSTEM - USING PYTHON FUNDAMENTALS (OOPS)

class Student:
    def __init__(self,roll,name,age,course):
        self.roll = roll
        self.name = name
        self.age = age
        self.course = course
       

    def display(self):
        print("\n")
        print(f"Roll: {self.roll} ")
        print(f"Name: {self.name} ")
        print(f"Age: {self.age} ")
        print(f"Course: {self.course} ")
        print("\n")
    

Students=[]

# add student 
def add_students():
    roll = int(input("Enter the roll no: "))
    for student in Students:
        if student.roll == roll:
            print("Roll Number Already Exists!")
            return
    name = input("Enter the name of student: ")
    age = int(input("Enter the age of student: "))
    course = input("Enter the course of student: ")

    student = Student(roll,name,age,course)
    Students.append(student)
    print("Student Added Successfully...!!")

# search for student
def search_student():
    roll = int(input("Enter the roll no to search: "))
    for student in Students:
        if student.roll == roll:
            print("Student Found")
            student.display()
            return
    print("Student Not Found")

# view total student
def view_students():
    if len(Students) == 0:
        print("No Records Found")
    else:
        for i in Students:
            i.display()
    
# Update student details
def update_student():
    roll = int(input("Enter roll number to update: "))
    
    for student in Students:
        if student.roll == roll:
            student.name = input("Enter new name: ")
            student.age = int(input("Enter new age: "))
            student.course = input("Enter new course: ")
            print("Student data updated successfully...!")
            return
    print("Student Not Found")


# delete student data
def delete_student():
    roll = int(input("Enter a roll number to delete: "))
    for student in Students:
        if student.roll == roll:
            Students.remove(student)
            print("Data deleted successfully..!")
            return
       
    print("No Records Found")


    


# Menu 
while True:
    
    ch = int(input("""----------STUDENT MANAGEMENT SYSTEM----------
        Choose Option to Proceed:
        1. ADD STUDENT
        2. VIEW STUDNETS
        3. SEARCH STUDENT 
        4. UPDATE STUDENT
        5. DELETE STUDENT
        PRESS ANY TO EXIT: \n"""))
    
    if ch == 1:
        add_students()
    elif ch == 2:
        view_students()
    elif ch ==3:
        search_student()
    elif ch ==4:
        update_student()
    elif ch ==5:
        delete_student()
    else:
       print("Thank You! Exiting Student Management System...")
       break


