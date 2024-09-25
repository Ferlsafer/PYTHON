def Votter():
    name = input("Enter your full name: ")
    age = int (input("Enter your age: "))

    if age >= 18:
        print(f"{name}, You can vote from now on")
    else:
        print(f"{name}, Your age is below the age to be eligable to vote")

    return age

print(Votter())