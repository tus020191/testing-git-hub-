from queue import LifoQueue

class QueueUsingStack:
    def __init__(self):
        self.stack=LifoQueue()
        self.front=-1

    def push(self,element):
        self.stack.put(element)
   
    def pop(self): # recursion 
        if(self.stack.empty()):
            return -1
        """
        note here do not make self.a as this means a is attribute of self object
        so its  value is shared during all recursion call
        but we want that for each recursion call a holds the  corresponding 
        top value  
        """
        a=self.stack.get() # now a is local to pop function,so each time 
                        # pop is called a new memory is created for a and it 
                        # will restore its value during recursion
        
        if(self.stack.empty()): # if after removing element stack is empty means element is front 
            return a
        self.front=self.pop() # recursion 

        
        
        self.stack.put(a)

        return self.front



q1=QueueUsingStack()
q1.push(12)
q1.push(123)
q1.push(124)
q1.push(125)

print("dequeue : ",q1.pop())
print("dequeue : ",q1.pop())
print("dequeue : ",q1.pop())
print("dequeue : ",q1.pop())
print("dequeue : ",q1.pop())
print("dequeue : ",q1.pop())

       





