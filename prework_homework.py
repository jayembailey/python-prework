# Quesion 1
# Write a function to print "hello_USERNAME!"
# USERNAME is the input of the function.
# The first line of the code has been defined as below.

def hello_name(user_name):
    print('hello_' + user_name + '!')

hello_name('USERNAME')

# Question 2
# Write a python function, first_odds that prints
# the odd numbers from 1-100 and returns nothing

def first_odds(nums):
    for num in nums:
        if num % 2 != 0:
            print(num)

first_odds(range(100))

# Question 3
# Please write a Python function, max_num_in_list to return
# the max number of a given list.
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    a_list.sort()
    return a_list[-1]

max_num = max_num_in_list([1,5,2,9,3])
print(max_num)

max_num = max_num_in_list([38745,34587,9693874,52525252])
print(max_num)

# Question 4
# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100,
#     unless it is also divisible by 400.
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0 or a_year % 400 == 0:
        return True
    else:
        return False
year_question = is_leap_year(2400)
print(year_question)

# Question 5
# Write a function to check to see if all numbers in list are
# consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers,
# but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.

def is_consecutive(a_list):
    a_list.sort()
    for i in a_list:
        i += 1
        if a_list[i + 1] == a_list[i] + 1:
            return True
        elif a_list[i + 1] != a_list[i] + 1:
            return False
     
value = is_consecutive([4,2,5,3,6])
print(value)
value = is_consecutive([4,5,3,9,6,7])
print(value)
