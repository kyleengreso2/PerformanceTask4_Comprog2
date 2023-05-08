def odd_numbers(a, b):
    if a == 0:
        return
    odd_numbers(a-1, b)
    if b(a):
        print(a)


n = int(input("Please enter an integer: "))


odd = lambda x: x % 2 == 1

odd_numbers(n,odd)