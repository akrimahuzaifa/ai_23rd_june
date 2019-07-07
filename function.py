# def arithematic_operations():
#     print("Hello I am inside a function") #2

# print("Hello Iam outside") #1
# arithematic_operations()


def arithematic_operations(operand1, operand2 = 0, operator="+"): #assignment argument does not need 1 to 1 mapping when calling (line15)
    if operator == "+":
        print(operand1 + operand2)

    if operator == "-":
        print(operand1 - operand2)

arithematic_operations(2, operator="-", operand2 = 4)

def fun_with_var_args(*all_paramtr):
    print(all_paramtr)

fun_with_var_args(1)
fun_with_var_args(2,3)


def fun_with_var_args(**all_paramtr):
    print(all_paramtr)

fun_with_var_args(Name = "Akrima")
fun_with_var_args(Name = "Akrima", FName = "Abdul")
fun_with_var_args(Name = "Akrima", FName = "Abdul", age = 43)

