'''
* what is regular expression?
=> It is a way of describing patterns within search strings.
* what are the applications of regex?
=> validationg emails, searching for specific content in a file etc.

* meaning of some symbols
=> [] use square brakects to specify custom ranges or groups of characters
=> ^ = starts with. However, if used inside the square brackets then this means NOT
=> - = range, e.g., a-z means ranging from a to z
=> + = one or more
=> $ = the end
=> for example, consider this expression inside the parathises: ( ^[ a-zA-Z0-9_.+- ]+@[ a-zA-Z0-9- ]+\.[ a-zA-Z0-9-. ]+$ )
this means, Starts with 1 or more letter, number, +, _, -, . then
            A single @ sign then
            1 or more letter, number, or - then
            A single dot then
            ends with 1 or more letter, number, -, or .
            
* Some regex syntax (some characters)
=> \d = digit 0-9
=> \w = letter, digit, or underscore
=> \s = whitespace character
=> \D = not a digit
=> \W = not a word character
=> \S = not a whitespace character
=> .  = any character except line break

* Some regex syntax ( quatifiers )
=> +     = One or more
=> {3}   = Exactly x times. {3} - 3 times
=> {3,5} = Three to five times
=> {4,}  = Four or more times
=> *     = Zero or more times
=> ?     = Once or none (optional)

* Some regex syntax (anchors and boundaries)
=> ^  = start of string or line
=> $  = end of string or line
=> \b = word boundary
'''





