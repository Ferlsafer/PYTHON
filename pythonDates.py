from datetime import datetime
'''I imported the datetime module and use its methods
1. strptime is used to format the date to the format I want
2. datetime.now() is used to provide the current date and hour that the information was provided
'''
start_date = datetime.strptime(input("Enter your start date: "), "%d-%m-%Y")
today_date = start_date
start_date = datetime.now()
print(start_date)
