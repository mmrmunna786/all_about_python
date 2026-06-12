'''
Reading CSV files using CSV module
=> reader - lets you iterate over rows of the csv as lists
=> Dictreader - lets you iterate over rows of the CSV as OrderedDicts
'''
# ===================================================================================
# example of using "reader" method from csv library
# from csv import reader # library and module to get help working with csv files 
# with open( "fighters.csv" ) as file: 
#     csv_reader = reader( file ) # reader is the method which returns and iterator
#     next( csv_reader ) # called next to avoid the header being printed
#     for row in csv_reader: # looping over the iterator to print each line/row as lists
#         print( f"{row[0]} is from {row[1]} and the height is {row[2]} cm.\n\n" )
# ===================================================================================
# example of using "Dictreader" method from csv library
# from csv import DictReader # library and module to get help working with csv files 
# with open( "fighters.csv" ) as file: 
#     csv_reader = DictReader( file ) # DictReader is the method which returns and iterator
#     # next( csv_reader ) # called next to avoid the header being printed
#     # print( csv_reader )
#     for row in csv_reader: # looping over the iterator to print each line/row as lists
#         # print( f"{row[0]} is from {row[1]} and the height is {row[2]} cm." )
#         print( row[ 'Name' ] )
# ===================================================================================
'''
Reading CSV files using CSV module
=> writer - creates a writer object for writing to csv
=> writenow - method on a writer to write a row to the csv
'''
# ===================================================================================
# for example:
from csv import writer 
with open( "cats.csv", "w" ) as file:
    csv_writer = writer( file ) # this will create an writer object <class '_csv.writer'>
    csv_writer.writerow( [ "Name", "Age" ] )  
    csv_writer.writerow( ["Mini", 2] )

        

