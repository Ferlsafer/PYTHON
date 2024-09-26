from datetime import datetime

class Client:
    def __init__(self, fname, lname, phone, email, createdDate, endDate):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        self.createdDate = createdDate
        self.endDate = endDate

    def ManupulateClient(self):
        # Capture input values and set as instance attributes
        self.fname = input("Enter your first name: ")
        self.lname = input("Enter your last name: ")
        self.phone = input("Enter your phone number: ")
        self.email = input("Enter your email address: ")
        self.createdDate = datetime.strptime(input("Enter the start date (YYYY-MM-DD): "), "%Y-%m-%d")
        self.endDate = datetime.strptime(input("Enter the end date (YYYY-MM-DD): "), "%Y-%m-%d")

        # Display the client details
        print(f"Client Details: {self.fname} {self.lname}, Phone: {self.phone}, Email: {self.email}, "
              f"Start Date: {self.createdDate.strftime('%Y-%m-%d')}, End Date: {self.endDate.strftime('%Y-%m-%d')}")


class ImplementStatus(Client):
    def __init__(self, fname, lname, phone, email, createdDate, endDate):
        super().__init__(fname, lname, phone, email, createdDate, endDate)

        # Calculate days left and print the status
        end_of_day_time = endDate.replace(hour=22, minute=0, second=0, microsecond=0)
        if endDate >= end_of_day_time:
            print("Your stay time is over")
        else:
            days_left = (endDate - createdDate).days
            print(f"You have {days_left} days left")


# Example usage:
# Step 1: Create a `Client` object and get client details
client = Client("", "", "", "", datetime.now(), datetime.now())
client.ManupulateClient()

# Step 2: Use the details from `client` to create `ImplementStatus` object
implement_status = ImplementStatus(client.fname, client.lname, client.phone, client.email, client.createdDate, client.endDate)
