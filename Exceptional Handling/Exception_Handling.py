try:
    print('try block')
    num1=int(input("Enter number"))
    num2=int(input("Enter number"))
    result=num1/num2
except:
    print("Except Block")
    print("Number 1 is not divisible by 0")
else:
    print("Else Block")
    print("Output ",result)
finally:
    print("Exception Handling Program")

