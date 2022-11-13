import math


l=[10,-20,-5,6,-8,55,-4]

def filterNegativeNum(i):
    if(i<0):
        return True

output=list(filter(filterNegativeNum,l))
print(output)

numbers = (1,2,3,4,5,6,7,8)

def oddNumFilter(i):
    if i%2!=0:
        return True
    return False

check_odd = list(filter(oddNumFilter,numbers))
print("Odd Numbers : ",check_odd)

mystring = "Hello World"
lowerCharacters = list(filter(lambda x: True if
x.lower() in "aeiou" else False, mystring))
print(lowerCharacters)
vow_list=['i','e','a','o','u']
def vow(i):
    if i in vow_list:
        return True
print (list(filter(vow,mystring)))


str="Winter Olympics in 2022 will take place in Beijing China"
lst=lst = list(filter(lambda x: True if x in
"0123456789" else False, str))
print(lst)


lst=[-1000, 500, -600, 700, 5000, -90000, -17500]
num = list(filter(lambda x: True if x>0 else False,map(lambda x: x*-1, lst)))
print(num)
#Doubt

num2=list(filter(lambda x: abs(x) if x<0 else "",lst))
print(list(num2))


blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13,
'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8,
'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments':
1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]

total_likes = 0
for post in blog_posts:
    try:
        total_likes = total_likes + post['Likes']

    except:
        post["Likes"]=0
print(total_likes)
