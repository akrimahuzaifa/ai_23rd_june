# for i in range(10):
#     if i % 2 == 0:
#         continue #or can be break
#     print(i)

students = []

while True:
    print ('Press 1 to Add Student')
    print ('Press 2 to Delete Student')
    print ('Press 3 to Search Student')
    print ('Press 4 to Edit Student')
    print ('Press 5 to  Print All Students')
    print ('Press 6 to  Exit')

    option = input("Enter 1 - 6: ")
    if option == '6':
        break
    elif option == "1":
        student = {}
        student["Name"] = input ("Enter Student Name: ")
        student["Age"] = input ("Enter Student Age: ")
        student["Father Name"] = input ("Enter Student Father Name: ")
        student["Address"] = input ("Enter Student Adress: ")
        students.append(student)
        
    elif option == "5":
        print(students)

    elif option == "2":
        name = input("Enter Student Name To delete: ")
        ind = 0
        for student in students:
            if student["Name"] == name:
                del students[ind]
                break
                

