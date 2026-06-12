# there's a file called story.txt in the current directory
# to open the file in read mode(default) we write this code(1st method):
# file = open( "story.txt" )
# # my_text = file.read()
# print(file.read())
# file.close()
# ========================================================
# 2nd method:
# with open( "story.txt" ) as file:
#     print(file.read())
# file.close()
# ========================================================
# open the file in write mode(will overwrite everything in the file) and write some lines of texts:
# with open( "story.txt", "w" ) as file:
#     file.write( "writing files is great\n" )
#     file.write( "here's another line of text\n" ) 
#     file.write( "closing now, goodbye!\n" )
# ========================================================
# open the file in append mode(will add to the end of the file) and write some lines of texts:
# with open( "story.txt", "a" ) as file:
#     file.write( "appending to the file\n" )
#     file.write( "here's another line of text\n" )
#     file.write( "closing now, goodbye!\n" )
    
# with open( "story.txt", "r" ) as file:
#     print(file.read())
# ========================================================
# open the file in read and write mode, move the cursor to a specific position and write something:
# with open( "story.txt", "r+" ) as file:
#     file.seek(13)
#     file.write(".")
# ========================================================
# The readlines() method returns a list containing each line in the file as a list item.
# with open( "story.txt" ) as file:
#     for line in file.readlines():
#         print(line)