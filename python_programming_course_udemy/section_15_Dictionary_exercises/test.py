# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# # make sure your solution is assigned to the answer variable so the tests can work!
# answer = { list1[i]: list2[i] for i in range(len(list1)) }
# print(answer)

# # another solution using zip
# answer = dict(zip(list1,list2))
# print(answer)

# answer = {}.fromkeys( "aeiou", 0 )
# print(answer)

answer = { nums:chr(nums) for nums in range( 65, 90+1 ) }
print(answer)