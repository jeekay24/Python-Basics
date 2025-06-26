n = int(input("Enter the no of elements:"))
while True:
    arr = list(map(int, input("Enter the numbers of the string:").split()))
    if len(arr) == n:
        break
    else:
        print("Please enter exactly the desired n of integers")

print(*arr)
