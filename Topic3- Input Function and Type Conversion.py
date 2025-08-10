'''
-> Input() Function: Input() function is used to get a value from end user, It always read values in string
                     from only.
Syntax: Variable_name = input()/ input('Your Message')
Ex: Read Empname then print empname
    ename  = input('Enter your name')
    print(ename)
'''

# Problem1: Write a program to read firstname, lastname then find fullname.
# sol: fname = input('Enter your first name')
#      lname = input('Enter your Last name')
#      fullname = fname + lname
#      print(fullname)

'''
a. To read integer value: 
   variable = int(input('your message'))

b. To read Floating value:
   variable = float(input('your message'))
   
c. To read int\Float value:
   variable = eval(input('your message'))

d. If user enter then it will convert into integer

e. If user enter float value then it will convert into float. 
'''

# Problem2: Write a program to read two integer number, then find the sum and print sum.
# sol: a =int(input('Enter value 1:'))
#      b =int(input('Enter value 2:'))
#      sum = a + b
#      print('the sum is:',sum)


# Problem3: Consider pizza cost is 350.0, now read Quantity from the user then find BillAmount.
# sol:  Pcost = 350.0
#       Ordered = int(input('Enter the amount of quantity of pizza:'))
#       bill_Amount = Pcost * Ordered
#       print('The total bill Amount is', bill_Amount')

'''
-> Type Conversion:- Converting a value from one type to another type.
                  It is also known as Type Conversion/ Type casting
syntax: variable = Datatype (value - int/Float/char/eval)
'''

# 1. Convert from string value to Integer:
# sol.   a = '5'      |  a = 'venkat'
#        b = int(a)   |  b = int(a)
#        print(b)     |  print(b)
#        Output: '5'  |  Output: error

# 2. Convert from string value to float:
# sol. a = '2.5'
#      b = float(a)
#      print(b)
# Output: 2.5

'''
Type of Type Conversions: 
a. int() - convert an Integer number from an integer Literals a string or a float literal.
Eg: variable = int(input('Enter any String:'))
b. Float() - constructs a float number from an integer literals, a float literals or a string Literal.
Eg: variable = Float(input('Enter the Statement'))
c. str() - Construct a string from a wide variety of data type, including string, integer literals and float literals
Eg: Variable = str(input('Enter any Statement'))
    Variable = str(value)
'''