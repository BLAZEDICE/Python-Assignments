x="Hello"
mylist=["Hello","Hello","Are","You"]

def myfunc(e):
    duplist=[]
    for letters in e:
        if(letters not in duplist):        
            return e
        duplist.append(letters)

def dupfunc(e):
    duplist=[]
    for letters in e:
        if letters not in duplist: #if l not in ['H','E','l','l']
            print(letters)
            duplist.append(letters)
        # print(duplist)
        return duplist
        
dupfunc("Hello")
result=map(dupfunc,mylist)
print(list(result))
#Doubt