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
When we use parameters in a function and do not send the arguments while calling the function. The interpreter would throw this error because of expecting arguments as the value of the parameters.  
"""

# My Code 1 
def multi_table(n,t):
    if n == 11:
        return
    else:
        print(str(t) + " X "  + str(n)+ " = " + str(n*t))
        return multi_table(n+1,t)

t = int(input("Enter a number: "))
multi_table(1) # here I missed 1 argument

""" 
Output: 
Enter a number: 4
Traceback (most recent call last):
  File "c:\Users\Amdadullah Raihan\Desktop\CS 1101\ASSIGNMENTS\WEEK (4)\test.py", line 9, in <module>
    multi_table(1) # here I missed 1 argument
TypeError: multi_table() missing 1 required positional argument: 't'

"""

""" 
II. There is something wrong with the function; a postcondition is violated.
Postcondition: 
Conditions that are applied after executing a function are called preconditions.
My Explanation: 
When a function doesn't get any precondition error and starts executing the function and gets errors from the inside statement of the function, then we get this error. It also can happen, if we send a different type of argument violating functions' expectation type. 

"""

# My Code: 2
def multi_table(n,t):
    if n == 11:
        return
    else:
        print(t + " X "  + str(n)+ " = " + str(n*t)) #Here I am not converting "t" to a string
        return multi_table(n+1,t)

t = int(input("Enter a number: "))
multi_table(1,t)

""" 
Enter a number: 5
Traceback (most recent call last):
  File "c:\Users\Amdadullah Raihan\Desktop\CS 1101\ASSIGNMENTS\WEEK (4)\test.py", line 9, in <module>
    multi_table(1,t)
  File "c:\Users\Amdadullah Raihan\Desktop\CS 1101\ASSIGNMENTS\WEEK (4)\test.py", line 5, in multi_table
    print(t + " X "  + str(n)+ " = " + str(n*t)) #Here I am not converting "t" to a string
TypeError: unsupported operand type(s) for +: 'int' and 'str'

"""



""" 
III. There is something wrong with the return value or the way it is being used.
My Explanation: 
The error occurs when the function does not return according to the expectation.
"""
# My Code: 3
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

# This code will work properly without throwing any error
def multi_table(n,t):
    if n == 11:
        return
    else:
        print(str(t) + " X "  + str(n)+ " = " + str(n*t))
        return multi_table(n+1,t)

t = int(input("Enter a number: "))
multi_table(1,t)


"""
Reference 
Downey, A. (2015). Think Python: How to think like a computer scientist. This book is licensed under Creative Commons Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0) 
"""
