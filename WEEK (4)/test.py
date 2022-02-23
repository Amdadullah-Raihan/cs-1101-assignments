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