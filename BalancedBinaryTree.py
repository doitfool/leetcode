"""
	@Project: leetcode
	@file: BalancedBinaryTree.py
	@author: AC
	@time: 2016/5/7 22:49
	@Description:	Given a binary tree, determine if it is height-balanced.
    For this problem, a height-balanced binary tree is defined as a binary tree in which
    the depth of the two subtrees of every node never differ by more than 1.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def height(self, root):
        if root is None:
            return -1
        else:
            return 1+max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            lh = self.height(root.left)
            rh = self.height(root.right)
            if abs(lh-rh) <= 1:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
            else:
                return False

s = Solution()
nodes = []
for i in range(6):
    nodes.append(TreeNode(i))
nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[3].left = nodes[5]
for i in range(6):
    print s.height(nodes[i])

print s.isBalanced(nodes[0])
