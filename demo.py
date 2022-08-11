from queue import Queue,LifoQueue
def fun(q):
    q.put(23)
def fun2(st):
    st.put(2673)
    st.put(2678)
    st.put(26789)
def rec():
    pass

q=Queue()
fun(q)
print(q.empty())
print(q.get_nowait())
q.put(56)
a=q
print(a is q)

print(a.get_nowait())

st=LifoQueue()
fun2(st)
print(st.get_nowait())
print(st.get_nowait())
print("bfbfbf")

print("vdvdndvsv")
print("vdvdndvsv")
print("vdvdndvsv")
print("vdvdndvsv")
print("vdvdndvsv")
print("vdvdndvsv")
print("vdvdndvsv")
print("vdvdndvsv")
