"""
    @Project: leetcode
    @file: Minimum Depth of Binary Tree.py
    @author: AC
    @time: 16-5-12
    @Description:   Given a binary tree, find its minimum depth.
    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is not None and root.right is None:
            return 1+self.minDepth(root.left)
        elif root.left is None and root.right is not None:
            return 1+self.minDepth(root.right)
        else:
            return 1+min(self.minDepth(root.left), self.minDepth(root.right))

nodes = []
nodes.append(TreeNode(0))
nodes.append(TreeNode(1))
nodes.append(TreeNode(2))
nodes.append(TreeNode(3))
nodes.append(TreeNode(4))
nodes.append(TreeNode(5))
nodes.append(TreeNode(6))

nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left = nodes[5]

s = Solution()
print s.minDepth(nodes[0])

nodes[3].left = nodes[6]
print s.minDepth(nodes[0])
