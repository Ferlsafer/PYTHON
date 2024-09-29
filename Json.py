import json
'''
====>JSON is a syntax for storing and exchanging data.
====>JSON is text, written with JavaScript object notation.
'''

#json.load() is a method for converting Json to Python
car = '{ "year": 2009, "brand": "Toyota", "Model": "Hardtop"}'

#converting to Python
car_convertedto_python = json.loads(car)
print(type(car_convertedto_python)) #I used 'type' to check the type of data and verify if it has been converted to python dict

#json.dump() is used to convert Python to Json format

studentDetails = {
    "name": "dixon fredy",
    "age": 20,
    "course": "Computer Science"
}
to_jason_format = json.dumps(studentDetails)
print(to_jason_format) #when converted it will print out type str 