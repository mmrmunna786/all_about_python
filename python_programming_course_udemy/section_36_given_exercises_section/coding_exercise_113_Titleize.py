# Author: Munna
# Date: 02/07/2026

"""
Write a function called titleize which accepts a string of words and returns 
a new string with the first letter of first word in the string is capitalized.
"""
def titleize( in_str ):
    return ", ".join( s[0].upper() +  s[ 1: ] for s in in_str.split( " " ) )

print( titleize( "oNLy cAPITALIZe fIRSt" ) ) 