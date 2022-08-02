from queue import Empty, Full, Queue
#from time import sleep

# Empty is an raise exception when queue is empty and we execute get_nowait() 
# similarly Full for put_nowait()
q=Queue(maxsize=5)

print(q.full())

print(q.empty())

 #print(q.get())
q.put(6) # put does not raise any exception instead it wait for element to pop
q.put(65)
q.put(68)
q.put(612)
q.put(16)
try:
    q.put_nowait(163) # it raise exception 
except (Full) as obj:
    print(obj)

print(q)
q.get() # is also not raise any exception it simply waits till element is inerted
try:
    q.get_nowait() # raise exception when empty
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()

except (Empty) as obj:
    print(obj)

print(q.qsize())




