
#part 2 
#taking user weight and height
weight = float(input("Enter your weight is kg: "))
height = float(input("Enter your heigt in feet: "))

#calutating users' BMI and taking decission based on the BMI
def isGoing_gym(weight, height):
    height_in_meter = height*0.3048
    bmi = weight/(height_in_meter**2)
    if bmi>18:
        print("I will go to a gym")
    else:
        print("I am totally a healthy person")

w = 70
h = 6

isGoing_gym(weight,height) #This call will take weight and height as input from user
isGoing_gym(60,5.6) #This will pass 60 as weight and 5.6 as height to the parameter 
isGoing_gym(w,h) # This call will pass w and h variable's value to the parameter

"""
output  
Enter your weight is kg: 56 // if the user input 56 as weight
Enter your heigt in feet: 5.6 // if the usesr input 5.6 as height
I will go to a gym // first result from users' input
I will go to a gym // second result from the given vlaues 60 and 5.6
I will go to a gym // third result from w and h

"""

""" 
explanations
This function will take weight and height as parameters and calculate BMI based on the weight and height and give a dicission if I have to go gym or not. 

"""