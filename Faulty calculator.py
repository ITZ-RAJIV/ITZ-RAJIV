print("# THIS IS A PYTHON CODE OF FAULTY CALCULATOR !!!")

print("# IN THIS CALCULATOR EXCEPT SOME CALCULATION ALL THE CALCULATION WAS RIGHT !!!")

print("# SOME FAULTY CALCULATIONS ARE AS FOLLOWS :-")

print("(i) 45 * 3 = 555")

print("(ii) 56 / 9 = 3")

print("(iii) 67-23 = 54")

num1 = int(input("Enter first number :- "))

num2 = int(input("Enter second number :- "))

operator = input("Enter operator out of [ + , - , * ,  ** , / ] :- ")

if num1 == 45 and num2 == 3 and operator =="*" :

	print("Product of these numbers is :- 555")

elif num1 == 56 and num2 == 9 and operator =="/" :

	print("Division of these numbers is :- 3")

elif num1 == 67 and num2 == 23 and operator =="-" :

	print("Difference between both numbers is :- 54")

elif operator == '**' :

	print("Answer of these equation is :- " , num1 ** num2)

elif operator =='+' :

	print("Sum of both numbers is :- " , num1 + num2)

elif operator == '-' :

	print("Difference between both number is :- " , num1 - num2)

elif operator == '*' :

	print("Product of these numbers is :-" , num1 * num2)

elif operator == '/' :

	print("Division of these numbers is :- " , num1 / num2)

else :

	print("Error !!! Please check your input.")
