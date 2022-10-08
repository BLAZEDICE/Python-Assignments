nos=[1,2,3,4,5,6,7,8,9,10]

def check_even(num):
    if num%2==0:
        return True
    return False

even_nos_iterator=filter(check_even,nos)
even_nos=list(even_nos_iterator)
print(list(even_nos_iterator))
print(even_nos)
my_even=filter(lambda x:(x%2==0),nos)
print(list(my_even))