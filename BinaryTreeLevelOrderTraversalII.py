"""
	@Project: leetcode
	@file: BinaryTreeLevelOrderTraversalII.py
	@author: AC
	@time: 2016/5/8 23:19
	@Description:	Given a binary tree, return the bottom-up level order traversal of its nodes' values.
	(ie, from left to right, level by level from leaf to root).
    For example:
    Given binary tree {3,9,20,#,#,15,7},
        3
       / \
      9  20
        /  \
       15   7
    return its bottom-up level order traversal as:
    [
      [15,7],
      [9,20],
      [3]
    ]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        result = [[root.val]]
        while queue:
            pop_nodes, pop_nums = [], []
            for i in xrange(len(queue)):
                pop_nodes.append(queue.pop(0))
            for i in xrange(len(pop_nodes)):
                if pop_nodes[i].left is not None:
                    queue.append(pop_nodes[i].left)
                    pop_nums.append(pop_nodes[i].left.val)
                if pop_nodes[i].right is not None:
                    queue.append(pop_nodes[i].right)
                    pop_nums.append(pop_nodes[i].right.val)
            result.append(pop_nums)
        result = result[:-1]
        result.reverse()
        return result

s = Solution()
nodes = []
nodes.append(TreeNode(1))
nodes.append(TreeNode(2))
nodes.append(TreeNode(3))
nodes.append(TreeNode(4))
nodes.append(TreeNode(5))
nodes.append(TreeNode(6))

nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[2].right = nodes[4]
nodes[3].left = nodes[5]
print s.levelOrderBottom(nodes[0])
