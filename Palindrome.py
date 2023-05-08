def palindrome(a, b):
    if len(a) <= 1:
        return True
    elif b(a[0], a[-1]):
        return palindrome(a[1:-1], b)
    else:
        return False


string = input("Please enter a string or a number: ")


check = lambda x, y: x == y

if palindrome(string, check):
    print("The input is a palindrome!")
    print(f"The last three characters/digits of the palindrome are: {string[-3:][::-1]}")
else:
    print("The input is not a palindrome.")

