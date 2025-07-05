print("\tCalculator\n\t=========")
while True:
    try:
        x=int(input("Enter First Number: "))
        break
    except ValueError:
        print("Please Enter Integer")

while True:
    try:
        y=int(input("Enter Second Number: "))
        break
    except ValueError:
        print("Please Enter Integer")

print("Operations:\n 1. Add\n 2. Subtract\n3. Multiply\n4. Divide\n5. Mode")

while True:
    try:
        c=int(input("Choose Operation: "))
        break
    except ValueError:
        print("Please Enter Integer")
        

if(c==1):
    print("Result= ", x+y)
elif(c==2):
    print("Result= ", x-y)
elif(c==3):
    print("Result= ", x*y)
elif(c==4):
    print("Result= ", x/y)
elif(c==5):
    print("Result= ", x%y)
else:
    print("No Operation Selected")