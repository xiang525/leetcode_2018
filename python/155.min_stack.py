class MinStack:
    # @param x, an integer
    # @return an integer
    

	def __init__(self):
	    self.q = []  # define a stack

	# @param x, an integer
	# @return an integer
	def push(self, x):
		currMin = self.getMin()
		if currMin == None or x < currMin:
			currMin = x
		self.q.append((x,currMin))

	    

	# @return nothing
	def pop(self):
		self.q.pop()
	    


	# @return an integer
	def top(self):
		if len(self.q) == 0:
			return None
		else:
			return self.q[len(self.q)-1][0]
	    


	# @return an integer
	def getMin(self):
		if len(self.q) == 0:
			return None
		else:
			return self.q[len(self.q)-1][1]



"""
类似与上面的解法，但可以使代码逻辑更easy
two stacks do insertation at the same time
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.minStack or self.minStack[-1] >= x:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()       
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

"""
Solution 2: 九章讲解为什么要用两个stack
"""
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if not self.minStack  or x <= self.minStack[-1]:
            self.minStack.append((x))
        

    def pop(self):
        """
        :rtype: nothing
        """
        p = self.stack.pop()
        if p == self.minStack[-1]:
            self.minStack.pop()  
        

    def top(self):
        """
        :rtype: int
        """
        #if self.stack is not None:
        return self.stack[-1]
        
        

    def getMin(self):
        """
        :rtype: int
        """   
        return self.minStack[-1]


"""
这道题目我们的想法是如何去做到这个特殊的getMin，想到的方法当然是空间换时间啦，那么用什么空间呢？当然是另一个
栈啦，所以我们就有了这么一个想法：用另一个栈来记录当前最小值，那么查找最小值就不需要遍历了，这样就实现了时间复杂
度和空间复杂度都是O(n)。的确这个想法已经很不错了，用java（官方题解就是这个版本）和C++（亲测）。但是我用
python就MLE了，让我纠结了好久。所以在没办法就要优化内存了，这里采用的方法是在minStack中插值的时候对相同的
值不重复插入，而是记录他的次数，终于AC.
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        #self.minStack.append(0)
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.minStack) == 0 or self.minStack[-1][0] > x:
            #print 'minn change'
            self.minStack.append((x,1))
        elif x == self.minStack[-1][0]:
            self.minStack[-1] = (x, self.minStack[-1][1] + 1)
 
    # @return nothing
    def pop(self):
        p = self.stack.pop()
        #print 'pop ' , p
        if p == self.minStack[-1][0]:
            if self.minStack[-1][1] > 1:
                #print 'minn pop'
                self.minStack[-1] = (self.minStack[-1][0], self.minStack[-1][1] - 1)
            else:
                self.minStack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        #print self.minStack
        return self.minStack[-1][0]








	    
	        
