try:
    age=int(input("Enter your age"))
    if(age<18):
        raise ValueError(age)
except ValueError:
    print(age," is out of allowed range")
else:
    print(age," is within range")

