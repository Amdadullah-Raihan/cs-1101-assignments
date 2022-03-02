# 1

def any_lowercase1(s):
     for c in s:
        #   print(c)
          if c.islower():
            #    print(c)
               return True
          else:
               return False
print(any_lowercase1("Hello")) #This will result false because the first letter of the argument is a upper case
print(any_lowercase1("hello")) #This will result True because the first letter of the argument is a lower case 
""" 
Output:
False
True
"""
#The function checks only the first letter of the parameter. How did I know? I included a print statement inside the for loop to see the values of c and I got only the first latter. Then I called the function with two different arguments one of them begins with an upper case and the other begins with a lower case.  
# 2

def any_lowercase2(s):
     for c in s:
          if 'c'.islower():
               return 'True'
          else:
               return 'False'
print(any_lowercase2("HELLO")) # This will print true 
#output: True
# The function is showing True as output, though I passed a parameter with all uppercase. The function is showing true because it checks only "c"(a string) instead of checking the parameters' characters. As string "c" is a lower case the function will always return true, no matter what parameter we pass. 
# 3

def any_lowercase3(s):
     for c in s:
        #   print(c)
          flag = c.islower()
        #   print(flag)
     return flag
print(any_lowercase3("Hello")) #This will print true as the last character of the argument is a lower case.
print(any_lowercase3("HellO")) # This will print False as the last character of the argument is an uppercase. 
#outputs:
# True 
# False
# The function is running a loop into its parameter and storing each character of the parameter in a variable named c. Then there is a variable named flag inside the for a loop which checks if c is a lowercase.  If the stored character in c is a lowercase the value of the flag will be true otherwise false. But here is the twist the loop runs until it covers all of the characters of the string(parameter s). 
#For the first character of the string, it will modify the value of the flag as true or false, then it will go back to loop again and check the second character of the string and reassign the value of flag according to the value of the second character. The loop will continue in that way until it reaches the last character of the string. Once it reaches the last character of the string it will reassign the value of the flag as the last character of the string, then the loop would end. As we returned flag from the same level of the loop it will return what the loop accomplished at last.  As the loop sets the value of flag according to the last character of the string the loop will return flag according to the value of the last string.  
#Long story short the function shows the output according to the last character of the string we passed as an argument. That means if the last character of the argument is lowercase, the function will return true otherwise it will return false. 
# 4

def any_lowercase4(s):
     flag = False
     for c in s:
        #   print(c)
          flag = flag or c.islower()
        #   print(flag)
     return flag
print(any_lowercase4("Amdad"))
print(any_lowercase4("AMDaD"))
print(any_lowercase4("AMDAD"))
# Output:
# True
# True
# False
#This fucntion is working properly and showing true if there is any lower case no matter where it placed. The function is returning Fasle only when there is no lowercase. 
# 5

def any_lowercase5(s):
     for c in s:
          if not c.islower():
            #    print(not c.islower())
               return False
     return True
print(any_lowercase5("raihaN"))
print(any_lowercase5("raihan"))
# output: 
# False
#  True
# This function is checking for uppercase instead of checking for lowercase and returning true if there is no uppercase vise versa false. This function also returns the value according to the last character of the string we passed as an argument. 
