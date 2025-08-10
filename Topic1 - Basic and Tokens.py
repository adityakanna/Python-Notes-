'''
-> what is python ?
   Python is a general Purpose programming language (or) Single Programming Language which area
   but involves multiple area such as:
   1. Desktop App
   2. Web App
   3. Data Analysis
   4. Machine Learning
   5. Data Sciences
   6. Amazon Web Services
   7. Devops
   8. Testing
   9. Research And Development
-> Father of Python is Guido Van Rassum
-> And it was introduced in the year.
'''

'''
-> Tokens:-
   The elements which is used to develop programming is called Tokens
   They are 5 types of tokens:
   1. Literals
   2. Constants
   3. Operators 
   4. Keywords
   5. Identifiers
'''

'''
1. Literals: The values in a program is called as Literals (or) The values which are changed is called as literals
   They are 4 types of Literals :
'''

# a. Integer Literals : Any number without decimals is known as Integers Literals
age = 22
token_no = 5
Emp_Id = 171

# b. Float Literals : Any number with decimals is known as float Literals
height = 5.7
weight = 65.5
Pcost = 122.71

# c. String Literals : Anything which is enclosed in double or single Quates is called string Literals
Name = "Aditya kanna"
Date_of_joinging = "10-sep-2022"
Experince = "10 yrs"

# d. Boolean Literals : True or False is called as Boolean Literals.
# (At the time of the condition we had to use boolean expression)

'''
2. Constants : The value which fixed is called as constants.
'''
# Months_in_a_year = 12
# Pi Value = 3.14
# hours_is_a_days = 24 hrs

'''
3. Operations : Anything which performs an operation is called as Operators.
'''
('a = 5 + 3') # -> '+' is an operator and 5, 3 is an operands.
('b = a < c') # -> '<' is an operator and a, b is an operands.
('a $ b') # -> '$' is not an operators and a, b is an operands.

# Arithmatic Operators:
# Operator            Name              Example
#   +               Addition           7+3  = 10
#   -               Subtraction        7-3  = 4
#   *               Multiplication     7*3  = 21
#   /               Division           7/3  = 3.5
#   //              Floor Division     7//2 = 3
#   %               Modulus            7%2  = 1
#   **              Exponent/Power     7**2 = 49

# Note :- 1. Write strings we can add only string value.
#         2. If you are trying to add other type of value are will get Error.
#         3. Adding string is also known as append.
#         4. Between string we always use '+' operator.
#         5. Except '+' if you use other operator than you will get error

# Operator Priority Lists:
# 1. ( )        ->  First Priority
# 2. **         ->  Second Priority
# 3. \,*,//,%   ->  Third Priority
# 4. +,-        ->  Fourth Priority

# Ex1: 5 + 3 * 2 = 11, Ex2: (5 + 3) * 2 = 16

# Note: 1. If you have more than one operator then follow operator Priority.
#       2. Same priority more than one operator you will calculate from Left to right.
#       3. If you have same operator (Exponent) after and other value. Then, we have to go from right to left.
# Ex: 2**2**2 = 16

'''
4. KeyWord: Keyword are the pre-define words and Every Keyword performs some operations.
   Types of Keyword:
   1. None, False, True, and, as, assert, await, break, class, continue, def, del, elif, else, except, finally,
      for, from, global, if, import, ':', in, is, lambda, non local, not, or, pass, raise, return,try, while, with
      yield.
   2. False, True, None are the value, they never do any operation.
'''

'''
5. Identifiers: 
   a. Identifiers are the User-Defined Words.
   b. Identifiers are the name given to the variable, Function, method, object, class, etc are called as Identify.
   Ex: Class CancelTkt:                   Class BookTkt: 
            Statement 1                        Statement 2
            ...........                        ...........
'''
# Note: 1. An Identifier given to the class is called as classname.
#       2. An Identifier given to the function is called as functioname.
#       3. An Identifier given to the Methods is called as methodname.
#       4. For Identifier we can give as name, but we need to follow 4 rule:
#          a. Rule 1: No Space
#             Ex: Book Ticket -> (Not Accepted), Book_Ticket -> (Accepted)
#          b. Rule 2: No Special Symbol Except Underscore (_).
#             Ex: Book@Ticket -> (Not Accepted), Book_Ticket -> (Accepted)
#          c. Rule 3: No keyword
#             Ex: and -> (Not Accepted, Because it is a Keyword)
#          d. Rule 4: First Character should be either alphabet or underscore (_)
# Ex: 2grade -> (Not accepted, Because the first character is not alphabet or Underscore)