n = int(input("Enter the number: "))

arr = list(map(int, input("Enter the elements of the array:").split()))

for i in range(0, n):  # i from 0 to n (inclusive)
    print(arr[i])
