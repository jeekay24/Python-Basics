n = int(input("Enter the no of elements:"))
while True:
    arr = list(map(int, input("Enter the elements:").split()))
    if len(arr) == n:
        break
    else:
        print("Enter exact n no of elements")
print(*arr)

target = int(input("Enter the target:"))


def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1


t = binary_search(arr, target)
if t != -1:
    print(f"{target} found at index {t}")
else:
    print("Index not found")
