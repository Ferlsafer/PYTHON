'''
working with classes (_init_ function)
The _init_ is used to initialize the fields of the class, it is used as a constructor
'''

class Staff:
    def __init__(self, name, department, id):
        self.name = name
        self.department = department
        self.id = id

staff1 = Staff('Dickson fredy', 'IT', 112)

print(staff1.department)
print(staff1.name)
print(staff1.id)

'''
the use of _str_ function
'''

class Students:
    def __init__(self, name, course, Id):
        self.name = name
        self.course = course
        self.Id = Id

    def __str__(self):
        return f"{self.name}, {self.course}, {self.Id}"
    
student1 = Students('John Axon', 'Computer Science', 16)
print(student1)

'''
The key difference between the above two classes is the use of _str_ function and without _str_ function
-when using str function you give Python a power to print result(string) in human readable format
-without using str the Python will return the memory addres which may confuse us
-the way we acces is different, I have printed each value different, when I did not use str and print all value of student when using str
'''

'''
Methods - are functions which belongs to the specific object
'''
class Addition():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def DisplayResult(self):
        result = self.num1 + self.num2
        print(f"The result is {result}")

addNumber = Addition(40, 30)
addNumber.DisplayResult()


