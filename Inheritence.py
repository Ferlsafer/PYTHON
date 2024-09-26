'''
Inheritence provides a feature whereby a class can use the properties of another class
a class that inherit features is called child class or derived class
a class that has the foundation features is called parent class or base class
'''
'''base class or parent class'''
class Doctors:
    def __init__(self, name, specialization, ID):
        self.name = name
        self.specialization = specialization
        self.ID = ID

    def Details(self):
        print(f"Doctor Name: {self.name}, Specialization: {self.specialization}, ID: {self.ID}")
    
# Create an instance of the Doctors class
Doc1 = Doctors('Christian Mapunda', 'Surgeon', 111)
Doc1.Details()  # Print details for the doctor

'''Child class (Nurse) derived from Doctors'''
class Nurse(Doctors):
    def __init__(self, name, specialization, ID, color):
        super().__init__(name, specialization, ID)
        self.uniform = color  # New attribute specific to Nurse
        
    def Details(self):
        # Change the output to reflect it's for a nurse
        print(f"Nurse Name: {self.name}, Specialization: {self.specialization}, ID: {self.ID}, Uniform Color: {self.uniform}")

# Create an instance of the Nurse class
Nurse1 = Nurse('Anna Komba', 'Attendant', 1212, 'blue')
Nurse1.Details()  # Print details for the nurse

