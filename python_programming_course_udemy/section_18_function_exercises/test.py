# def last_element( lst ):
#     # returns the last value in the list
#     if lst != []:
#         return lst[ -1 ]
#     # returns None if the list is empty
#     return None

# print( last_element( [1,2,3] ) )

# flesh out multiple_letter count:

# def multiple_letter_count( a_string ):
#     # function takes in one parameter (a string) and returns a dictionary with
#     # the keys being the letters and the values being the count of the letter
#     result = { letter : a_string.count(letter) for letter in a_string }
#     return result

# print( multiple_letter_count( "awesome" ) )

# def list_manipulation( lst, command, location, value=None ):
#         #If the command is "remove" and the location is "end", the function should remove the last value in the list and return the value removed
#     if command == "remove" and location == "end":
#         return lst.pop()
#     #If the command is "remove" and the location is "beginning", the function should remove the first value in the list and return the value removed
#     elif command == "remove" and location == "beginning":
#         return lst.pop(0)
#     # If the command is "add" and the location is "beginning", the function should add the value (fourth parameter) to the beginning of the list and return the list
#     elif (command == "add" and location == "beginning"):
#         lst.insert(0, value)
#         return lst
#     # If the command is "add" and the location is "end", the function should add the value (fourth parameter) to the end of the list and return the list
#     elif (command == "add" and location == "end"):
#         lst.append(value)
#         return lst

# print(list_manipulation([1,2,3], "remove", "end")) # 3
# print(list_manipulation([1,2,3], "remove", "beginning")) #  1
# print(list_manipulation([1,2,3], "add", "beginning", 20)) #  [20,1,2,3]
# print(list_manipulation([1,2,3], "add", "end", 30)) #  [1,2,3,30]


# def is_palindrome( user_input ):
#     # convert the user_input to a string and all lowercase
#     user_input = str(user_input).lower()
#     # read the user_input backwards and save it in a variable
#     user_input_reversed = "" # varible to store the reversed string
#     for i in range( len( user_input )-1, -1, -1 ):
#         user_input_reversed += user_input[i]
#     if user_input == user_input_reversed:
#         return True
#     return False
# print( is_palindrome(500) )


# def multiply_even_numbers(lst):
#     # 1. initialise a variable called product to 1
#     product = 1
#     # 2. Loop through each number in the input list
#     # 3. For each number, check if it is even
#     # 4. A number is even if number % 2 == 0
#     # 5. If the number is even, multiply it with product and store the result back into product
#     # 6. After the loop ends, return product
#     for item in lst:
#         if item % 2 == 0:
#             product *= item
#     return product

# print( multiply_even_numbers( [1,2,3,4] ) )

# flesh out intersection pleaseeeee
def intersection( lst1, lst2 ):
    resultant_lst = []
    
    for i in lst1:
        for j in lst2:
            if i == j:
                resultant_lst.append( i )
    return resultant_lst          
print(intersection( [1,2,3], [2,3,4] ))