import math
from operator import add

list1=[1,2,3,4,5]
list2=[7,8,9,10]
list3=list1+list2
print(list3)
add_list=[]
for nos in list1:
    for nos2 in list2:
        add_list.append(nos+nos2)
print(add_list)
result=map(add,list1,list2)
print(list(result))

#Doubt