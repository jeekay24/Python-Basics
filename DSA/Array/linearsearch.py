def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


n = int(input("Enter the number of elements in the array:"))
arr = list(map(int, input("Enter the n number of elements:").split()))
target = int(input("Enter the target:"))

ls = linear_search(arr, target)

if ls != -1:
    print(f"The element {target} is found in the index {ls}")
else:
    print("Element not found")
