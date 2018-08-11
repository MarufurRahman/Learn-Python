# Making class of a calculator
# programmed by Marufur Rahman

class cal():
    def __init__(self,a,b): 
        self.a=a
        self.b=b
    def add(self):
        # add function will addition them
        return self.a+self.b
    def mul(self):
        # mul function will multiplication them
        return self.a*self.b
    def div(self):
        # div function will division them
        return self.a/self.b
    def sub(self):
        # sub function will division them
        return self.a-self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=cal(a,b)
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",obj.add())
    elif choice==2:
        print("Result: ",obj.sub())
    elif choice==3:
        print("Result: ",obj.mul())
    elif choice==4:
        print("Result: ",round(obj.div(),2))
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
 
print()

