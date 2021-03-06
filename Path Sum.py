"""
	@Project: leetcode
	@file: Path Sum.py
	@author: AC
	@time: 2016/5/10
	@Description:	Given a binary tree and a sum, determine if the tree has a
	root-to-leaf path such that adding up all the values along the path equals the given sum.
    For example:
    Given the below binary tree and sum = 22,
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \      \
            7    2      1
    return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        else:
            if root.left is None and root.right is None and sum == root.val:
                return True
            else:
                return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

s = Solution()
nodes = []
nodes.append(TreeNode(0))
nodes.append(TreeNode(1))
nodes.append(TreeNode(2))
nodes.append(TreeNode(3))

nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].right = nodes[3]
print s.hasPathSum(nodes[0], 2)

