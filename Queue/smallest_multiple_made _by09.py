from queue import Queue
from unicodedata import name

class Smallestmultiple :
    def __init__(self) -> None:
        self.q=Queue()
        self.l=[]
        self.maxcount=1000000
    def convertstringtonum(self,string):
        n=len(string)
        num,power=0,1
        for i in range(n-1,-1,-1):
            digit=ord(string[i]) - ord("0")
            num=num+ (digit*power)
            power*=10
        return num

    def allnumber90(self,X):
        self.q.put("9")
        while(self.maxcount):
            front=self.q.get()
            num=self.convertstringtonum(front)
            #self.l.append(front)
            if(self.smallestdivnum(X,num)):
                return num

            s1=front+"0"
            front=front+"9"
            self.q.put(s1)
            self.q.put(front)
            self.maxcount-=1
    
    def smallestdivnum(self,X,num):
        """
        self.allnumber90()
        
        for i in self.l:
            num=self.convertstringtonum(i)
            if(num%X==0):
                return num
        """
        return True if num%X==0 else False
    
if __name__=="__main__":
    X=1211
    num=Smallestmultiple()
    
    print(num.allnumber90(X))
    #print(num.l)


    