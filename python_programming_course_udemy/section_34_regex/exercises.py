'''
Time Validating
Write a function called is_valid_time that accepts a single string argument.  
It should return True if the string is formatted correctly as a time, like 
3:15 or 12:48 and return False otherwise.  Note that times can start with a 
single number (2:30) or two (11:18).  
is_valid_time("10:45")       #True
is_valid_time("1:23")        #True
is_valid_time("10.45")       #False
is_valid_time("1999")        #False
is_valid_time("145:23")      #False

In order to return True, the string should ONLY contain the time, and no other characters
is_valid_time("it is 12:15") #False
is_valid_time("12:15")       #True

Don't worry about impossible times like 88:76, just focus on the formatting!
is_valid_time("34:55") #True
'''
import re
def is_valid_time( input_string ):
    # 1.create the regular expression
    # starts with 1 to 2 numbers from 0 to 9 
    # then a colon
    # then 1 to 2 numbers from 0 to 9
    # then end (put a dollar sign)
    time_regex = re.compile( r'^[0-9]{1,2}:[0-9]{1,2}$' )
    time_regex_match = time_regex.search( input_string )
    if time_regex_match and (time_regex_match.group() == input_string):
        return True
    return False

print(is_valid_time("10:45"))       #True
print(is_valid_time("1:23"))        #True
print(is_valid_time("10.45"))       #False
print(is_valid_time("1999"))        #False
print(is_valid_time("145:23"))      #False

# another simpler solution 
def is_valid_time(input):
    pattern = re.compile(r'^\d\d?:\d\d$')
    match = pattern.search(input)
    if match:
        return True
    return False

print(is_valid_time("10:45"))       #True
print(is_valid_time("1:23"))        #True
print(is_valid_time("10.45"))       #False
print(is_valid_time("1999"))        #False
print(is_valid_time("145:23"))      #False

'''
Parsing Bytes Exercise
Write a function called parse_bytes that accepts a single string.  
It should return a list of the binary bytes contained in the string.  
Each byte is just a combination of eight 1's or 0's. For example:

parse_bytes("11010101 101 323")    # ['11010101']
parse_bytes("my data is: 10101010 11100010")    # ['10101010', '11100010']

parse_bytes("asdsa")   # []

Hints: take advantage of \b Not all bytes will have a space before and 
after, some come at the beginning of a file or at the end.  Use findall!
'''
def parse_bytes( input_string ):
    # 1.create the regular expression
    find_byte_regex = re.compile( r'\b[0-1]{8}\b' )
    return find_byte_regex.findall( input_string )

print("\n\n", parse_bytes("11010101 101 323"))

# another simpler solution
def parse_bytes(input):
    binary_regex = re.compile(r'\b[10]{8}\b')
    results = binary_regex.findall(input)
    return results

'''
Date Parsing Exercise
Define a function called parse_date  that accepts a single string.  
Your code should check to see if the string matches a date format.  
We're going to use the DMY format of "dd/mm/yyyy", but it should 
also work with "dd.mm.yyyy" and "dd,mm,yyyy". If you are American, 
note that Day if before Month!  However, rather than simply returning 
True or False if the string matches...you should instead return a 
dictionary containing the three parts of the date with the keys 
"d" , "m" , and "y"  like so:
parse_date("01/22/1999") # {'d': '01', 'm': '22', 'y': '1999'}

Note: the string should be an EXACT match, containing the date and 
nothing else. If there is no match, return None
parse_date("12,04,2003")  #{'d': '12', 'm': '04', 'y': '2003'}
parse_date("12.11.2003")  #{'d': '12', 'm': '11', 'y': '2003'}
parse_date("12.11.200312") #None
'''
def parse_date( in_str ):
    # crete the regular expression
    # date part: 1 to 31
    # 1st separation part: / or . or , note that for period we use a escape charracter
    # dmy_regex = re.compile( r'(?P<date_part>[0-9]{2})(?P<first_separation_part>[/.,])(?P<month_part>[0-9]{2})(?P<second_separation_part>[/.,])(?P<year_part>\d{4})$' )
    dmy_regex = re.compile(r"^(?P<date_part>\d\d)(?P<first_separation_part>[/.,])(?P<month_part>\d\d)(?P<second_separation_part>[/.,])(?P<year_part>\d{4})$")
    dmy_regex_match = dmy_regex.search( in_str )
    if dmy_regex_match:
        return {
                "d" : f"{dmy_regex_match.group('date_part')}",
                "m" : f"{dmy_regex_match.group('month_part')}",
                "y" : f"{dmy_regex_match.group('year_part')}"
            }
    return None
print( parse_date('01/22/1999') )
'''
Regex Profanity Filter
Define a function called censor  that accepts a single string. Rather than censoring any real profanity, 
we're going to censor any words that start with "frack".  This includes "fracking", "fracker", "frack", etc.  
Replace the entire word with the string "CENSORED".  Your regex should be case insensitive. For example:

censor("Frack you")                #"CENSORED you"
censor("I hope you fracking die")  #"I hope you CENSORED die"
censor("you fracking Frack")       #"You CENSORED CENSORED"
'''
def censor( in_str ):
    pattern = re.compile(r'\bfrack\w*\b', re.I)
    result = pattern.sub("CENSORED", in_str)
    return result

censor("Frack you") 
censor("I hope you fracking die")
censor("you fracking Frack") 
# text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

# pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
# result = pattern.sub("\g<1> \g<2>", text)
# print(result) # Mr. D # Ms. C # Mrs. M