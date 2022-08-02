"""
k queue in single array 
we use 3 array for this purpose
"""



class Kqueue:
    def __init__(self,no_of_queue,size_of_array) :
        self.n=no_of_queue
        self.size=size_of_array
        self.array=[]
        self.front=[-1]*self.n
        self.rear=[0]* self.n
        # next store the free space available space 
        self.next=[int(i)  for i in range(1,self.size+1)]
        self.next.append(-1) # science after last index no space is left 

        self.free=0

    def empty(self,k):
        return True if self.front[k]==-1 else False

    def full(self,k):
        return True if self.free==-1 else False

    def enqueue(self,element,k):
        i=self.free
        self.free=self.next[i]
        if self.empty() :
            self.front[k]=element
        else:
            self.next[self.rear[i]]=i
        self.next[i]=-1 # to store the -1 means  we reach the last  element and after it no 
                        # element present in k th queue
        self.rear[k]=i
        self.array[i]=element



        

