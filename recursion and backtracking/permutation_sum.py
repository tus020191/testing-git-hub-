
# program to find all permutation of given string 

# function to swap the characters of string in python
def swap(index,i,s):

    # swapping the index and i th character in python as string is unmutable, so using replace function 
    s=list(s) # converting to list
    s[index],s[i]=s[i],s[index] # swapping the i and index character
    
    return "".join(s) 
#function to calculate the permutation
def find(input_string ,output_list,n,index,st): 
    
    # base case
    if(index==n-1):
        # check for duplicate

        if(input_string not in st):
            st.add(input_string)
            output_list.append(input_string)
        return  # void 
    for i in range(index,n):
        # swapping the characters
        input_string=swap(index,i,input_string)

        find(input_string,output_list,n,index+1,st)
        
        # undoing the changes made in string while swapping 
        input_string=swap(index,i,input_string)


def all_permutation(S):
    output_list=[] # for storing the answer 
    n=len(S)

    st=set() # empty set  
    find(S,output_list,n,0,st)
    sorted(output_list)

    return output_list




# main function

input_string="ABA"
output_list=all_permutation(input_string) 
print(output_list)

