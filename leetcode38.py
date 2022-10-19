# https://leetcode.com/problems/count-and-say/
# https://leetcode.com/submissions/detail/825727167/

def countAndSay(n):
    if n == 1:
        return "1"
    say = str(countAndSay(n - 1))
    index = 1
    count = 1
    new_say = ""
    def recursive_count():
        nonlocal index
        nonlocal count
        nonlocal new_say
        while len(say) > 1 and index < len(say) and say[index] == say[index - 1]:
            count += 1
            index += 1
        if count > 1:
            new_say += str(count) + say[index - 1]
            count = 1
        else:
            new_say += "1" + say[index - 1]
        if index == len(say):
            return new_say
        else:
            index += 1
            return recursive_count()
    return recursive_count()

print(countAndSay(1))    # expect "1"
print(countAndSay(2))    # expect "11"
print(countAndSay(3))    # expect "21"
print(countAndSay(4))    # expect "1211"
