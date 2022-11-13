import math
num=[2,3,4,5,6]
def listTripler(item):
    return math.floor(math.pow(item,3))

resultList=list(map(listTripler,num))
print(resultList)


nums=[0,1,2,3,4,5,6,7,8,9,10]
def evenList(i):
    if(i%2==0):
        return i
def oddList(i):
    if(i%2!=0):
        return i

evenNumbers=list(filter(lambda
x:x,map(evenList,nums)))
oddNumbers=list(filter(lambda x:x,map(oddList,nums)))
print("Odd numbers : {0}".format(oddNumbers))
print("Even numbers : {0}".format(evenNumbers))


import re #regular expression
string = ""
str = "hello world hello"
def findDuplicate(i):
    global string
    if re.search(i,string) == None:
        string += i

ans=map(findDuplicate,str)
print(list(ans)) 
# you need to print this list for map function as it is mandatory
print("String with unique characters:",string)




#Table 
number=int(input("Enter number for multiplication table :"))
l=int(input("Enter limit till you want to print table:"))
print("Table solution")
def multiples(i):
    return number*i

limitList=[]
for i in range(1,l+1):
    limitList.append(i)

res =list(map(multiples,limitList))
print("Multiplication Table : ",res)


names ={'a':'anna','b':'BHarat','c':'carlo','d':'dim'}
gmail = dict(map(lambda
x:(x[0],x[1].lower()+'@gmail.com'),names.items()))
print(gmail)