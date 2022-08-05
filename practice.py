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