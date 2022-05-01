number : int = int(input("Enter number : "))

square_root : int = 0

for i in range(number):
    square_root = i * i
    if square_root == number:
        print(i)
        break;
    elif i == number - 1:
        print("The square of the number could not be found.")
    else: 
        i += 1
    
