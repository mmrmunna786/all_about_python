# =====================================================================
"""
copy
Write a function called copy, which takes in a file name and a new file 
name and copies the contents of the first file to the second file.

(Note: we've provided you with the first chapter of Alice's Adventures 
in Wonderland to give you some sample text to work with. This is also the text used in the tests.

copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
"""
# def copy(file, file_name):
#     # open the file in read mode and copy the content into a variable
#     with open(file, "r") as file:
#         file_content = file.read()
#     # open the file in write mode and write the content in the file_content 
#     # variable to the story_2.txt file
#     with open(file_name, "w") as file:
#         file.write(file_content)
# =====================================================================
"""
copy_and_reverse
Write a function called copy_and_reverse, which takes in a file name and 
a new file name and copies the reversed contents of the first file to the second file.

(Note: we've provided you with the first chapter of Alice's Adventures 
in Wonderland to give you some sample text to work with. This is also the text used in the tests.)
"""
# def copy_and_reverse( file, new_file ):
#     # open the old file in read mode
#     # read the content of the file and reverse it using slicing
#     with open( file, "r" ) as file:
#         content_reversed = file.read()[ ::-1 ]
#         # print( content_reversed )
#     # open the new file in write mode and write the reversed content to it
#     with open( new_file, "r+" ) as file:
#         file.write( content_reversed )
#          # need this beacuse after writing the cursor is at EOF so this will bring it to the beginning
#         file.seek(0)
#         # not the below print statement will print the content 
#         print( file.read() )
#     # with open( new_file, "r" ) as file:
#     #     print( file.read() )
# copy_and_reverse( "story.txt", "story_2.txt" )
# =====================================================================
'''
statistics
Write a function called statistics, which takes in a file name and returns 
a dictionary with the number of lines, words, and characters in the file.

(Note: we've provided you with the first chapter of Alice's Adventures in 
Wonderland to give you some sample text to work with. This is also the text used in the tests.)
'''
# def statistics( file ):
#     # which takes in a file name and returns a dictionary with the number of lines, words, and characters in the file
#     # create three variables to store each requirements
#     num_of_lines = 0
#     words = 0
#     characters = 0
#     # create an empty dictionary to store the results
#     dictionary = {}
#     # open the file in read mode and loop through each line in the file, for each line add 1 to 
#     # the num_of_lines variable, add the number of words in the line to the words variable and 
#     # add the number of characters in the line to the characters variable
#     with open( file, "r" ) as file:
#         for line in file:
#             num_of_lines += 1
#             words += len(line.split())
#             characters += len(line)
#     dictionary["lines"] = num_of_lines
#     dictionary["words"] = words
#     dictionary["characters"] = characters
#     return dictionary
# print( statistics( "story.txt" ) )
# =====================================================================
'''
find_and_replace
Write a function called find_and_replace, which takes in a file name, a word to search for, and 
a replacement word. Replaces all instances of the word in the file with the replacement word.

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give 
you some sample text to work with. This is also the text used in the tests.)
'''
def find_and_replace( file_name, word_to_search, replacement_word ):
    # open the file in read mode and store the content in a variable
    with open( file_name, "r" ) as file:
        content = file.read()
    # replace all instances of the target word with replacement word
    updated_content = content.replace( word_to_search, replacement_word )
    # overwrite the given file with updated content
    with open( file_name, "w" ) as file:
        file.write( updated_content )

find_and_replace( "story.txt", "now", "after" )

