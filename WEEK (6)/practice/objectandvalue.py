#Objectes represent pythons' data on the other hand values are those data represented by objects

my_first_name = "Amdadul"
his_first_name = "Amdadul"
print(my_first_name is his_first_name)
#Output: True
# Here my_first_name and his_first_name are identical because they come from the same object

my_marks = [90, 84, 95]
his_marks = [90, 84, 95]
print(my_marks is his_marks)
#Output: False
# Here my_marks and his_marks are equavalent not identical.Though both of them have the same list, they didn't referes from the same object. That's why they are not identical but equavalent. 


my_name = "Amdadul"
student_name = my_name
print(student_name)
#Everything in python is saved in memory as an object. We give the object a name so that we can find the object from memory easily. Here the name we give to an object is a reference for that object. In simple, we can find an object from memory by reference. But when an object have more then one reference we call it aliasing. I hope we can understand now how objects, references, and aliasing are related to each other. In the avove "Amdadul" is a str object and I gave a reference(my_name) to this object and putted it inside another reference. That means the object now is aliased and have two different reference

def calculate_average_marks(marks):
    
    # marks = marks.append(3,5,5)
    mark_for_attendence = [100]
    mark_for_assignments = [90]
    extra_marks = mark_for_attendence + mark_for_assignments
    marks = marks + extra_marks
    # print(marks)
    total = 0
    for mark in marks:
        total = total+mark
    average = total/len(marks)
    print("Your average mark is: "+ str(average))

marks = [84,87,90,96]
calculate_average_marks(marks) 

#Here I've set a referece(marks) for the list and passed it as a argument the parameter recieved the argument which is a list. Then I used the parameter as another reference to modify the previous one.  