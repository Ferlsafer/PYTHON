'''
working with classes (_init_ function)
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