myset={7,10,15,3,7,56,32,344,57}
myset2={"First","Second",'Third',"First"}

def conv_to_list(myset):
    list_set=list(myset)
    list_set.reverse
    return list_set
    

result=map(conv_to_list,myset2)

print(list(result))
#Doubt