
#  all path possible to reach the end of matrix

def is_safe(x,y,n,m):
    if(x<n and y<m):
        return True
    False
def path(input,output,tmp,x,y,n,m):
    path1=0
    path2=0
    tmp1=tmp[::]  #  or tmp1=tmp.copy()

    if(x==n-1 and y==m-1):  # base case

        tmp1.append(input[x][y])
        output.append(tmp1)
       
        return True
    if(is_safe(x,y,n,m)):
        tmp1.append(input[x][y])

        if( path(input,output,tmp1,x+1,y,n,m)):
            path1=1
        
        if( path(input,output,tmp1,x,y+1,n,m)):
            path2=1
        if(path1==1 or path2==1):
            return True
        tmp1.pop()
        return False

    return False

def all_path(input,n,m):
    output=[] // 2d list 
    path(input,output,[],0,0,n,m)
   
    return output


input=[
    [3,2],
    [1,2],
    [4,5],
    [6,7]
    ]
output=all_path(input,4,2)

for i in output:
    for j in i:
        print(f"{j} ",end="")
    print()

