'''
add_user
For this exercise, you'll be working with a file called users.csv . Each row of data consists of 
two columns: a user's first name, and a user's last name.

Implement the following function:
add_user : Takes in a first name and a last name and adds a new user to the users.csv file.
'''
# from csv import writer
# def add_user(fname, lname):
#     with open( "users.csv", "a" ) as file:
#         csv_writer = writer( file )  
#         csv_writer.writerow( [ fname, lname ] )
# =============================================================================================
# this is to create the file and add the header with an entry in it
# from csv import writer
# with open( "users.csv", "w" ) as file:
#     csv_writer = writer( file )  
#     csv_writer.writerow( [ "First Name", "Last Name" ] )
#     csv_writer.writerow( [ "Munna", "Rahman" ] )
# =============================================================================================
# add_user( "Munna", "Rahman" )
'''
print_users
For this exercise, you'll be working with a file called users.csv . Each row of data consists of two 
columns: a user's first name, and a user's last name.

Implement the following function:
print_users : prints out all of the first and last names in the users.csv file
'''
# from csv import DictReader # library and module to get help working with csv files 

# def print_users():
#     with open( "users.csv" ) as file: 
#         csv_reader = DictReader( file ) # DictReader is the method which returns an iterator
#         # next( csv_reader ) # called next to avoid the header being printed
#         # print( csv_reader )
#         # print( list( csv_reader ) ) # this will print the whole csv as a list of OrderedDicts
#         for row in csv_reader: # looping over the iterator to print each line/row as lists
#             # print( f"{row[0]} is from {row[1]} and the height is {row[2]} cm." )
#             print( f"{row[ "First Name" ]} {row[ "Last Name" ]}" )
# print_users()
# =============================================================================================
'''
find_user
For this exercise, you'll be working with a file called users.csv . Each row of data consists 
of two columns: a user's first name, and a user's last name.

Implement the following function:
find_user : Takes in a first name and a last name and searches for a user with that first and 
last name in the users.csv file. If the user is found, find_user returns the index where the 
user is found. Otherwise it returns a message stating that the user wasn't found.
'''
# from csv import reader
# def find_user( fname, lname ):
#     # open the file as read mode
#     with open( "users.csv" ) as file:
#         # create a reader object using reader() method
#         users = reader( file )
#         #next( users ) # called next to avoid the header being printed
#         # variables to store row index if the searched user is found
#         user_found_idx = 0
#         # iterate over and see the data structure first
#         for user in users:
#             # compare first name and last name in each row
#             if fname == user[0] and lname == user[1]:
#                 # user_found_idx = general_idx
#                 return user_found_idx
#             user_found_idx += 1 # keep incrementing the index
#         return f"{fname} {lname} not found."
            
# print( find_user( "Munna", "Rahman" ) )
# =============================================================================================
'''
update_users
For this exercise, you'll be working with a file called users.csv . Each row of data consists 
of two columns: a user's first name, and a user's last name.

Implement the following function:
update_users : Takes in an old first name, an old last name, a new first name, and a new last 
name. Updates the users.csv file so that any user whose first and last names match the old 
first and last names are updated to the new first and last names. The function should return 
a count of how many users were updated.
'''
# from csv import reader, writer
# def update_users( old_first_name, old_last_name, new_first_name, new_last_name ):
#     # open the users.csv file
#     with open( "users.csv" ) as file:
#         csv_reader = reader( file ) # create a reader object
#         rows = list( csv_reader )
#         # print( rows[0][0] )
#         count_of_updated_users = 0 
#         # # print each row to see the structure of data
#         for row in rows:
#             print( row )
#             # Updates the users.csv file so that any user whose first and last names match the old 
#             # first and last names are updated to the new first and last names
#             if old_first_name == row[0] and old_last_name == row[1]:
#                 count_of_updated_users += 1
#                 row[0] = new_first_name
#                 row[1] = new_last_name
#     # write it back to the file
#     with open( "users.csv", "w" ) as file:
#         csv_writer = writer( file )
#         csv_writer.writerows( rows )
#     return f"Users updated: {count_of_updated_users}."
            
# print( update_users( "Munna", "Rahman", "Mohammad", "Munna" ) )
# update_users( "Munna", "Rahman", "Mohammad", "Munna" )
# =============================================================================================
'''
delete_users
For this exercise, you'll be working with a file called users.csv . Each row of data consists of 
two columns: a user's first name, and a user's last name.

Implement the following function:
delete_users : Takes in a first name and a last name. Updates the users.csv file so that any user 
whose first and last names match the inputs are removed. The function should return a count of how 
many users were removed.
'''
from csv import reader, writer
def delete_users( fname, lname ):
    # open the users.csv file
    with open( "users.csv" ) as file:
        csv_reader = reader( file ) # create a reader object
        rows = list( csv_reader )
        # print( rows[0][0] )
        count_of_deleted_users = 0
        # # print each row to see the structure of data
        for row in rows:
            print( row )
            # Updates the users.csv file so that any user whose first and last names match the old 
            # first and last names are updated to the new first and last names
            if fname == row[0] and lname == row[1]:
                count_of_deleted_users += 1
                rows.remove( row )
    # write it back to the file
    with open( "users.csv", "w" ) as file:  
        csv_writer = writer( file )
        csv_writer.writerows( rows )
    return f"Users deleted: {count_of_deleted_users}."