# https://leetcode.com/problems/deepest-leaves-sum/
# https://leetcode.com/submissions/detail/829033609/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [[root, 1]]
        level = 1
        sum = 0
        while len(queue) > 0:
            curr_node, curr_level = queue.pop(0)
            if curr_node.left:
                queue.append([curr_node.left, curr_level + 1])
            if curr_node.right:
                queue.append([curr_node.right, curr_level + 1])
            if curr_level > level:
                level = curr_level
                sum = 0
            sum += curr_node.val
        return sum
