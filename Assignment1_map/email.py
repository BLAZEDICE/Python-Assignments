mydict={"Hello":"World","RoSe":"FLOwer","ManGO":"fruiT"}
result=map(lambda a:(a[0]+"gmail.com",a[1]+"gmail.com"),mydict.items())
mydict=map(lambda a:(a[0].lower()+"gmail.com",a[1].lower()+"gmail.com"),mydict.items())
print(list(mydict))