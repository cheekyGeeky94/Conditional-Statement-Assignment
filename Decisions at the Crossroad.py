'''Task 1: Code Correction You are provided with a Python script that uses conditional statements to tell
 if a number is positive, negative, or zero, but it has some errors. Identify and fix them.'''

number = int(input("Enter a number: "))      #variable type must be an integer for the code to work, corrected

if number > 0:
    print("The number is positive.")
elif number == 0:                        #Syntax error. Use of one "=" and not the "==". Corrected
    print("The number is zero.")
elif number < 0:                        #Syntax error. Use of else statement instead of elif
    print("The number is negative.")