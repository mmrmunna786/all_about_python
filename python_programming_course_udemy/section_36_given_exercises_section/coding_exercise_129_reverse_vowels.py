# Author: Munna
# Date: 11/07/2026

'''
Write a function called reverse_vowels. This function should reverse the vowels in a string. 
Any characters which are not vowels should remain in their original position. 
You should not consider "y" to be a vowel.

For example:
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''
'''
algorithm:
1. Find all the vowels in the string.
2. Reverse that vowel list.
3. Put those reversed vowels back into the original positions.
'''

def reverse_vowels( in_str ):
    # 1. Find all the vowels in the string.
    vowels = "aeiouAEIOU"
    vowels_in_input_string = [ char for char in in_str if char in vowels ]
    # print( vowels_in_input_string )
    # 2. Reverse that vowel list.
    reverse_vowels_in_input_string = vowels_in_input_string[ ::-1 ]
    # print( reverse_vowels_in_input_string )
    # 3. Put those reversed vowels back into the original positions.
    result = []
    j = 0
    for ch in in_str:
        if ch in vowels:
            result.append( reverse_vowels_in_input_string[ j ] )
            j += 1
        else:
            result.append( ch )
    return "".join( result )

# print(reverse_vowels("Hello!")) # "Holle!" 
# print(reverse_vowels("Tomatoes")) # "Temotaos" 
print(reverse_vowels("Reverse Vowels In A String")) # "RivArsI Vewols en e Streng"
# print(reverse_vowels("aeiou")) # "uoiea"
# print(reverse_vowels("why try, shy fly?")) # "why try, shy fly?"