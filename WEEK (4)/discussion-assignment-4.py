""" 
Note: I've used the same function for each of the possibilities to keep the explanation simple and easy to understand. 
I've created a function that can take a number and show the multiplication table of that number. At the end of the file, I included the actual function which doesn't throw any error. 

"""


"""
Three possibilities to consider if a function is not working.
I. There is something wrong with the arguments the function is getting; a precondition is violated.	
Precondition: 
Conditions that are applied before executing a function are called preconditions.											  
My Explanation: 
It can happen when we do not send arguments when we have to.
"""

# My Code: 
def multi_table(n,t):
    if n == 11:
        return
    else:
        print(str(n) + " X " + str(t) + " = " + str(n*t))
        return multi_table(n+1,t)

t = int(input("Enter a number: "))
multi_table(1) # here I missed 1 argument

""" 
Output: 
Enter a number: 5
Traceback (most recent call last):
  File "c:\Users\Amdadullah Raihan\Desktop\CS 1101\ASSIGNMENTS\WEEK (4)\discussion-assignment-4.py", line 17, in <module>
    multi_table(1)
TypeError: multi_table() missing 1 required positional argument: 't'
PS C:\Users\Amdadullah Raihan\Desktop\CS 1101\ASSIGNMENTS> 


"""

""" 
II. There is something wrong with the function; a postcondition is violated.
Postcondition: 
Conditions that are applied after executing a function are called preconditions.
My Explanation: 
It can happen if I send a different type of argument violating functions' expectation type  

"""

# My Code: 
def multi_table(n,t):
    if n == 11:
        return
    else:
        print(n + " X " + str(t) + " = " + str(n*t)) #Here I am not converting "n" to a string
        return multi_table(n+1,t)

t = int(input("Enter a number: "))
multi_table(1,t)

""" 
    Enter a number: 2
    Traceback (most recent call last):
    File "c:\Users\Amdadullah Raihan\Desktop\CS 1101\ASSIGNMENTS\WEEK (4)\test.py", line 9, in <module>   
        multi_table(1,t)
    File "c:\Users\Amdadullah Raihan\Desktop\CS 1101\ASSIGNMENTS\WEEK (4)\test.py", line 5, in multi_table
        print(n + " X " + str(t) + " = " + str(n*t)) #Here I am not converting "n" to a string
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

"""



""" 
III. There is something wrong with the return value or the way it is being used.
My Explanation: 

"""
# My Code: 
def multi_table(n,t):
    if n == 11:
        return
    else:
        print(str(n) + " X " + str(t) + " = " + str(n*t))
        return multi_table(n+1) #here I missed 1 argument

t = int(input("Enter a number: "))
multi_table(1,t)

""" 
Output: 
Enter a number: 5
1 X 5 = 5
Traceback (most recent call last):
  File "c:\Users\Amdadullah Raihan\Desktop\CS 1101\ASSIGNMENTS\WEEK (4)\test.py", line 9, in <module>
    multi_table(1,t)
  File "c:\Users\Amdadullah Raihan\Desktop\CS 1101\ASSIGNMENTS\WEEK (4)\test.py", line 6, in multi_table
    return multi_table(n+1) #here I missed 1 argument
TypeError: multi_table() missing 1 required positional argument: 't' 

"""

"""
Reference 
Downey, A. (2015). Think Python: How to think like a computer scientist. This book is licensed under Creative Commons Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0) 
"""