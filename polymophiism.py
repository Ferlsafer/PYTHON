'''
In coding polymophism shows how methods, functions or class can different form but share some certain characteristics.
'''

class Teachers:
    def __init__(self, name, department, subject, ID):
        self.name = name
        self.department = department
        self.subject = subject
        self.ID = ID

    def ShowInfo(self):
        print(f"{self.name} teaches {self.subject} in the {self.department} department with ID {self.ID}")

# Create a Teacher object
teacher1 = Teachers('Huruma Ngongi', 'CS', 'Data Structure', 1212)
teacher1.ShowInfo()

class Librarian(Teachers):
    def __init__(self, name, department, subject, ID):
        super().__init__(name, department, subject, ID)
    
    # Overriding the ShowInfo method to represent a Librarian's behavior
    def ShowInfo(self):
        print(f"{self.name} manages the library with ID {self.ID}")

# Create a Librarian object
librarian1 = Librarian('Sara Mwangi', 'Library', 'Library Management', 3434)
librarian1.ShowInfo()

# Polymorphism in action
for staff in (teacher1, librarian1):
    staff.ShowInfo()
