#print("Disctionaries")

student = {"Name": "Akrima", "Father_Name": "Abdul Ghaffar", "age": 42}
#print(student["Name"])
#print("F Name" in student)

student["No of students"] = 5
#print(student)

my_key = "Contact No."
student[my_key] = "03462665606"
#print(student)

#print(student.keys())
#print(student.values())
#print(student.items())

for key in student.keys():  #for values student.values & for item student.items
    print(key)

for k,v  in student.items():
    print(k, v)

tpl = (2, 4, 6)
a ,b, c = tpl
print(a, b, c)

del student["Contact No."]