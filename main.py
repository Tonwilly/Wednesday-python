# for loop
for i in range(5):
    print(i)

print("Hello world")
# nested for loop
for i in range(5,0,-1):
    for y in range(i):
        print(y, end=" ")
    print()

# input with int method
y=0
for i in range(8):
    marks = int(input(f"Enter Marks{y+1}: "))
    if marks >= 0 and marks <= 39:
        print("Grade A")
    elif marks >=40 and marks <=69:
        print("Grade C")
    elif marks>=70 and marks<=79:
        print("Grade B")
    elif marks>=80 and marks<=100:
        print("Grade A")

