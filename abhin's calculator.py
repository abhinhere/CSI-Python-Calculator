print("Welcome to Calculator")
a=int(input("Enter a number :"))
b=int(input("Enter another number :"))
print("1 = addition\n2 = multipication\n3 = division")
c=int(input("select the operation that you want to do :"))
if c==1:
   print(f"{a}+{b}=",a+b)
elif c==2:
   print(f"{a}*{b}=",a*b)
elif c==3:
   print(f"{a}/{b}=",a/b)
else:
   print("Invalid Entry")
   
