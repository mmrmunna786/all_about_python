user_input = input("Enter the number of miles you've run: ")
miles = float(user_input)
kilometers = round(miles * 1.60934, 2)
print(f"You've run {kilometers} kilometers.")