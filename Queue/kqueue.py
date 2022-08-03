"""
k queue in single array 
we use 3 array for this purpose
"""



class Kqueue:
    def __init__(self,no_of_queue,size_of_array) :
        self.n=no_of_queue
        self.size=size_of_array
        self.array=[0]*self.size
        self.front=[-1]*self.n
        self.rear=[0]* self.n
        # next store the free space available space 
        self.next=[int(i)  for i in range(1,self.size+1)]
        self.next.append(-1) # science after last index no space is left 

        self.free=0

    def empty(self,k):
        return True if self.front[k]==-1 else False

    def full(self):
        return True if self.free==-1 else False

    def enqueue(self,element,k):
        if(self.full()):
            print("array is full ")
            return 
        i=self.free
        self.free=self.next[i]
        if self.empty(k) :
            self.front[k]=i
        else:
            self.next[self.rear[k]]=i
       
        self.next[i]=-1 # to store the -1 means  we reach the last  element and after it no 
                        # element present in k th queue
        self.rear[k]=i
        self.array[i]=element

    def dequeue(self,k):
        """
        no need to change the rear array as when we enqueue it stores the i th index
        i,e, it store the index where the last element is inserted 
        """
        if(self.empty(k)):
            print(f"{k} stack is empty !!!!")
            return -1

        i=self.front[k]
        self.front[k]=self.next[i] # storing the next front of kth queue
        self.next[i]=self.free # means that the free space after next[i] is at free
        self.free=i # as we have dequeue the front means a space is free 
        
        # no need to change the array as when we enqueue then automatically array[i] 
        # value is updated 
        return self.array[i]


if __name__=='__main__':
    k_queue=Kqueue(3,10) # k=3 and n=10
    print(k_queue.dequeue(2))
    k_queue.enqueue(15,2)
    k_queue.enqueue(45,2)

    k_queue.enqueue(17,1)
    k_queue.enqueue(39,1)
    k_queue.enqueue(49,1)

    k_queue.enqueue(11,0)
    k_queue.enqueue(9,0)
    k_queue.enqueue(7,0)

    print(f"dequeue from {2} : {k_queue.dequeue(2)}")
    print(f"dequeue from {1} : {k_queue.dequeue(1)}")
    print(f"dequeue from {0} : {k_queue.dequeue(0)}")
    print(f"dequeue from {0} : {k_queue.dequeue(0)}")


        

