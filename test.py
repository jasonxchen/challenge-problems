# Resolve #2:
# def order_arr(arr1, arr2):
#     output = []
#     dictionary = {}
#     for num in arr1:
#         if num in dictionary:
#             dictionary[num] += 1
#         else:
#             dictionary[num] = 1
#     unsorted = []
#     for num in dictionary:
#         if num in arr2:
#             for _ in range(dictionary[num]):
#                 output.append(num)
#         else:
#             for _ in range(dictionary[num]):
#                 unsorted.append(num)
#     unsorted.sort()
#     return output + unsorted

# Initial solve:
# def order_arr(arr1, arr2):
#     output = []
#     dictionary = {}
#     for num in arr1:
#         dictionary[num] = 0
#     for num in arr1:
#         dictionary[num] += 1
#     for num in arr2:
#         # for _ in range(dictionary[num]):
#         #     output.append(num)
#         output.append([num] * dictionary[num])
#         dictionary[num] = 0
#     unsorted = []
#     for key, value in dictionary.items():
#         if value != 0:
#             for _ in range(value):
#                 unsorted.append(key)
#     unsorted.sort()
#     return output + unsorted

# Resolve #1:
def order_arr(arr1, arr2):
    queue = []
    for num2 in arr2:
        for i, num1 in enumerate(arr1):
            if num1 == num2:
                queue.append(arr1.pop(i))
    arr1.sort()
    return queue + arr1

# order_arr([2,3,1,3,2,4,6,9,2,19,23,7], [2,1,4,3,9,6])
print(order_arr([2,3,1,3,2,4,6,9,2,19,23,7], [2,1,4,3,9,6]))
