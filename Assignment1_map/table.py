nos=[1,2,3,4]
def mult(i):
    for a in range(1,11):
       return a*i
# mult(10)
result=map(mult,nos)
print(list(result))

def mymult(a):
    for i in range(11):
        return i*a

result2=map(lambda a:(a*i for i in range(1,11)),nos)
print(list(result2))
#Doubt