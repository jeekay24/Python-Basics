def can_make_equal(A, B, X):
    diff = abs(A - B)
    if diff % X == 0:
        return "YES"
    else:
        return "NO"

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the parameters for each test case
    input_list = input().split()
    A = int(input_list[0])
    B = int(input_list[1])
    X = int(input_list[2])

    # Check if A and B can be made equal
    result = can_make_equal(A, B, X)

    # Print the result
    print(result)
