def multiply(num):
    return num*num
def toUpper(str):
   return str.upper()

result=map(multiply,(2,4,6,8))
result2=map(lambda i : i*i,(2,4,6,8))
res=map(toUpper,("Software","sem","3"))
newlist=list(res)
newlist.append("Hey")
print(newlist)
# newtuple1=tuple(res)
# newtuple1.append("Hey tuple")
# print(newtuple1)
print(tuple(result))
print(list(result2))
print(list(res))


dict_item={"a":"Car","b":"Bike","c":"Train"}
a=map(lambda i:(i[0]+"__",i[1]+"s"),dict_item.items())
dict_item={"a":"Car","b":"Bike","c":"Train"}
a2=map(lambda i:i+"__",dict_item.keys())
print(dict(a))
print(a2)