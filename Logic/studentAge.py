role = input("Enter your role")
age = int(input("Enter your age"))
eligible = role == "student" and age < 21
print("Eligible", eligible)