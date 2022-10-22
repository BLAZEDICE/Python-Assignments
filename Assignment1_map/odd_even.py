#2.Seperate all odd and even nos
nos=[1,2,3,4,5,6,7]
def my_function(i):
    if i%2==0:
        print("Even :",i)
    else:
        print("Odd :",i)

def my_function2(i):
    even_list=[]
    odd_list=[]
    if i%2==0:
        # x=even_list.append(i)
        return True
    
    
    # else:
    #    y=odd_list.append(i)
    #    return y

result=map(my_function2,nos)
result=filter(my_function2,nos)
print(list(result))
result2=map(lambda a:"even" if a%2==0 else "odd",nos)
print (list(result2))

#Doubt