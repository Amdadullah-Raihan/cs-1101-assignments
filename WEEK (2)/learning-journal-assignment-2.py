#part 1

#assigned value to pi
pi = 3.141592653589793


#taking input for radius from the user


#calculating volume of the sphere
def print_volume (r):
    volum = (4/3)*pi*r**3
    print("The volum of sphere is: " + str(volum))


#calling the funciton with three different value.
print_volume(5)
print_volume(5.5)
print_volume(3.00)

#an extra call for getting the result from user input
print_volume(float(input("Input radius of the sphere: ")))

""" 
output 
The volum of sphere is: 523.5987755982989 // This result is for input 5
The volum of sphere is: 696.9099703213358 // This reult is for input 5.5
The volum of sphere is: 113.09733552923254 // This result is for input 3.00
Input radius of the sphere: 2 // Taking input(radius) from the user
The volum of sphere is: 33.510321638291124 // This result is based on users' input

"""


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
