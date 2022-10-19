# palindrome
# if reverse string is the same as forward string (e.g. racecar)

def is_palindrome(string):
    # reverse the string
    reverse = string[::-1]
    # check if the reverse is same as the string in the parameter of the function
    if (reverse == string):
        # return true if they match
        return True
    # else return false
    else: 
        return False

print(is_palindrome("racecar"))
print(is_palindrome("jason"))
print(is_palindrome("tacocat"))
