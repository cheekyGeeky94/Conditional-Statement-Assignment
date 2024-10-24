'''Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. 
Your code should then identify and print out the largest number among the three.'''

enter_number = int(input("Enter the first number "))
enter_number2 = int(input("Enter the second number "))
enter_number3 = int(input("Enter the final number "))

if enter_number >= enter_number2 and enter_number >= enter_number3:        #created variations of conditions
    print ("The largest number is ", enter_number)                          #use of AND statement with >= in case of
elif enter_number2 >= enter_number and enter_number2 >= enter_number3:      #equal numbers
    print ("The largest number is ", enter_number2)
elif enter_number3 >= enter_number and enter_number3 >= enter_number2:
    print ("The largest number is ", enter_number3)


'''Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest
 number among the three and print it out.'''

if enter_number <= enter_number2 and enter_number <= enter_number3:        #created variations of conditions
    print ("The smallest number is ", enter_number)                          #use of AND statement with <= in case of
elif enter_number2 <= enter_number and enter_number2 <= enter_number3:      #equal numbers
    print ("The smallest number is ", enter_number2)
elif enter_number3 <= enter_number and enter_number3 <= enter_number2:
    print ("The smallest number is ", enter_number3)