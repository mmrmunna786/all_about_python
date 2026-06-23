# Author: Munna
# Date: 23/06/2026
'''
vowel_count
Write a function called vowel_count that accepts a string and returns a dictionary with 
the keys as the vowels and values as the count of times that vowel appears in the string.

vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''
def vowel_count( in_str ):
    vowel_count = {} # create a empty dictionary to store the vowel counts
    VOWELS = "aeiou" # constant vowels
    
    for char in in_str.lower(): # convert to lower case for case-insentivity
        if char in VOWELS:
            if char in vowel_count:
                vowel_count[ char ] += 1 # increment existing vowel 
            else: 
                vowel_count[ char ] = 1 # add a new vowel entry 
    return vowel_count
print(vowel_count('awesome')) # {'a': 1, 'e': 2, 'o': 1}
print(vowel_count('Elie')) # {'e': 2, 'i': 1}
print(vowel_count('Colt')) # {'o': 1}