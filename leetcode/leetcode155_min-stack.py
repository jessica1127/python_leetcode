'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # push x and current_min 
        current_min = self.getMin()
        if current_min == None or x < current_min:
            current_min = x
        self.q.append((x, current_min))
        

    def pop(self):
        """
        :rtype: void
        """
        self.q.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q)-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q)-1][1]


obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(-5)
obj.push(-8)
obj.pop()
print "obj =", obj
param_3 = obj.top()
print "param_3 = ", param_3
param_4 = obj.getMin()
print "param_4 = ", param_4