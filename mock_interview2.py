# 1 parameter is a string of numbers
# print highest and lowest digits in the string

def print_high_low(nums):
    # split the string into array based on white space
    arr = nums.split(" ")
    # initialize low and high variables
    low = arr[0]
    high = arr[0]
    # search through index to check if the current num is lower than the low or higher than the high
    for num in arr:
        if int(num) < int(low):
            low = num
        elif int(num) > int(high):
            high = num
    return f"low number is: {low} \nhigh number is {high}"

print(print_high_low("8 43 9 5 64 7 31"))
