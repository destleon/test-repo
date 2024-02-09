import additionop,multi,substraction

#using for loop to repeat my code 10 times

for number_of_times in range(1,11):


    first_number = int(input("enter the first number "))
    second_number =int(input("enter the second number "))
    type_of_operation =input("choose the  operation do you want to perform  +,-,* ")

    if type_of_operation =="+":
        print(additionop(first_number,second_number))

    elif type_of_operation =="-":
        print(substraction(first_number,second_number))

    elif type_of_operation =="*":
        print(multi(first_number,second_number))

    else:
        print("no operation selected")