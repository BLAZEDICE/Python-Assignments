try:
    print('try block')
    num1=int(input("Enter number"))
    num2=int(input("Enter number"))
    result=num1/num2
    print("Output ",result)
except:
    print("Except Block")
    print("Number 1 is not divisible by 0")
    
finally:
    print("Exception Handling Program")

