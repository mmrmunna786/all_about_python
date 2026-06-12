from csv import reader # library and module to get help working with csv files 
# with open( "fighters.csv" ) as file: 
#     csv_reader = reader( file ) # reader is the method which returns and iterator
#     next( csv_reader ) # called next to avoid the header being printed
#     for row in csv_reader: # looping over the iterator to print each line/row as lists
#         print( f"{row[0]} is from {row[1]} and the height is {row[2]} cm.\n\n" )