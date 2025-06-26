def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]


n = int(input("Enter a number:"))

if is_palindrome(n):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
