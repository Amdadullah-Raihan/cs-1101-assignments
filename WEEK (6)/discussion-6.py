#Objectes represent pythons' data. On the other hand, values are those data represented by objects
#part-1
my_first_name = "Amdadul"
his_first_name = "Amdadul"
print(my_first_name is his_first_name)
#Output: True
# Here my_first_name and his_first_name are identical because they refer to the same object


my_marks = [90, 84, 95]
his_marks = [90, 84, 95]
print(my_marks is his_marks)
#Output: False
""" Here, my_marks and his_marks are equivalent, not identical. Though both of them have the same list, they didn't refer to the same object. That's why they are not identical but equivalent.  """

#part-2
my_name = "Amdadul"
student_name = my_name
print(student_name)
""" Everything in python is saved in memory as an object. We give the object a name so that we can find the object from memory easily. Here the name we give to an object is a reference for that object. In simple, we can find an object from memory by reference. But when an object has more than one reference, we call it aliasing. I hope we can understand now how objects, references, and aliasing are related to each other. In the above, "Amdadul" is an str object, and I gave a reference(my_name) to this object and put it inside another reference. That means the object, now is aliased and have two different references """

def calculate_average_marks(marks):
    
    
    mark_for_attendence = [100]
    mark_for_assignments = [90]
    extra_marks = mark_for_attendence + mark_for_assignments
    marks = marks + extra_marks #modifying the list by adding more integer values
    # print(marks)
    total = 0
    for mark in marks:
        total = total+mark
    average = total/len(marks)
    print("Your average mark is: "+ str(average))

marks = [84,87,90,96]
calculate_average_marks(marks) 
#Output: Your average mark is: 91.16666666666667

""" Here, I've set a reference(marks) for the list object and passed it as an argument, and the parameter received the argument, which is a list. Then I used the parameter as another reference to modify the previous one(list).  At first, the function takes the argument and sets it as a parameter. Then the function creates two more references for two more list-objects. After that, the function adds those two references and creates a new reference to make a new list that contains the values from both of the previous references. Then the function calls the reference(parameter) for the original list, which I've passed as an argument, and adds new values to it. After that, the function calculates the sum of each value from the list."""