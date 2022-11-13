lst=[-1000, 500, -600, 700, 5000, -90000, -17500]
num = list(filter(lambda x: True if x>0 else False,map(lambda x: x*-1, lst)))
t=map(lambda x: x*-1, lst)
print(list(t))
print(num)
#Doubt  

# num2=list(filter(lambda x: abs(x) if x<0 else "",lst))
# print(list(num2))