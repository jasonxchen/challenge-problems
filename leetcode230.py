# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# https://leetcode.com/submissions/detail/829073674/
# Note: slow solve trying to get used to quicksort

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li = []
        curr_node = root
        def rAdd(curr_node):
            li.append(curr_node.val)
            if curr_node.left:
                rAdd(curr_node.left)
            if curr_node.right:
                rAdd(curr_node.right)
            return
        rAdd(curr_node)
        
        def quick_sort(li):
            if len(li) <= 1:
                return li
            else:
                pivot = li[0]
                # i = 1
                # j = len(li) - 1
                # while i < j:
                #     while li[i] <= pivot and i < len(li) - 1:
                #         i += 1
                #     while li[j] > pivot:
                #         j -= 1
                #     if i < j:
                #         li[i], li[j] = li[j], li[i]
                # return quick_sort(li[1:j]) + [pivot] + quick_sort(li[j + 1:])
                left = [i for i in li[1:] if i <= pivot]
                right = [i for i in li[1:] if i > pivot]
                return quick_sort(left) + [pivot] + quick_sort(right)
        return quick_sort(li)[k - 1]
