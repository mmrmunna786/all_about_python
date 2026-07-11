# Author: Munna
# Date: 06/07/2026

'''
Write a function called range_in_list which accepts a list and start and end indices, and returns 
the sum of the values between (and including) the start and end index.

If a start parameter is not passed in, it should default to zero. If an end parameter is not passed 
in, it should default to the last value in the list. Also, if the end argument is too large, the sum 
should still go through the end of the list.

For example:
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
'''

def range_in_list( in_lst, start_idx=None, end_idx=None ):
    # check if the strat and end indices are None, if so, set them to default values
    if start_idx is None:
        start_idx = 0
    if end_idx is None:
        end_idx = len(in_lst) - 1
    # slice the input list based on the start and end indeces
    lst_to_sum = in_lst[ start_idx:end_idx+1 ]
    sum = 0
    for num in lst_to_sum:
        sum += num
    return sum

print(range_in_list([1,2,3,4],0,2)) #  6
print(range_in_list([1,2,3,4],0,3)) # 10
print(range_in_list([1,2,3,4],1)) #  9
print(range_in_list([1,2,3,4])) # 10
print(range_in_list([1,2,3,4],0,100)) # 10
print(range_in_list([],0,1)) # 0