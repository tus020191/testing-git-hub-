from queue import Queue
def rec_reverse(q):
    # base case
    if(q.empty()):
        return 
    else:
        x=q.get_nowait()
        rec_reverse(q)
        q.put_nowait(x)
    
    
def rev(q):
    #add code here
    rec_reverse(q)
    return q

q=Queue(maxsize=100)
for i in range(1,10):
    q.put_nowait(i)

q=rev(q)
for i in range(1,10):
    print(q.get_nowait() )
    

