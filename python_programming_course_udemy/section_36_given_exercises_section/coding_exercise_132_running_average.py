# Author: Munna
# Date: 12/07/2026

'''
Create a function running_average that returns a function. 
When the function returned is passed a value, the function returns the current average of 
all previous function calls. You will have to use closure to solve this. 
You should round all answers to the 2nd decimal place.

For example:
rAvg = running_average()
rAvg(10) # 10.0
rAvg(11) # 10.5
rAvg(12) # 11

rAvg2 = running_average()
rAvg2(1) # 1
rAvg2(3) # 2
'''
'''
algorithm:
1. Create a function called running_average():
   a. Initialize sum = 0 and count = 0
   b. Define an inner function that takes a number:
      i. Add the number to sum
      ii. Increment count by 1
      iii. Calculate average = sum / count
      iv. Return average rounded to 2 decimal places
   c. Return the inner function
'''
def running_average():
    sum = 0
    count = 0
    def inner_func( in_num ):
        nonlocal sum, count
        sum += in_num
        count += 1
        return round( sum / count, 2 )
    return inner_func

# rAvg2 = running_average()
# print(rAvg2(1)) # 1
# print(rAvg2(3)) # 2

rAvg = running_average()
print(rAvg(10))  # 10.0
print(rAvg(11))  # 10.5
print(rAvg(12))  # 11.0