"""
	@Project: leetcode
	@file: Implement Stack using Queues.py
	@author: AC
	@time: 2016/5/11
	@Description: Implement the following operations of a stack using queues.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.
    Notes:
    You must use only standard operations of a queue -- which means only push to back, peek/pop
    from front, size, and is empty operations are valid.
    Depending on your language, queue may not be supported natively. You may simulate a queue by
    using a list or deque (double-ended queue), as long as you use only standard operations of a
    queue. You may assume that all operations are valid (for example, no pop or top operations
    will be called on an empty stack).
"""

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.top_index = -1
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.top_index += 1
        self.stack.append(x)



    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop(self.top_index)
        self.top_index -= 1


    def top(self):
        """
        :rtype: int
        """
        if self.top_index >= 0:
            return self.stack[self.top_index]
        else:
            return None

    def empty(self):
        """
        :rtype: bool
        """
        if self.top_index == -1:
            return True
        else:
            return False

s = Stack()
s.push(1)
s.pop()
s.push(2)
print s.top()
