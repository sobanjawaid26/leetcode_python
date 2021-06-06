n = 1
n1 = n2 = int('9' * n)


def myFunc(i, j):
    for i in range(i, 0, -1):
        if isPalindrome(i, j):
            return (i * j) % 1337
        if j > 0:
            j = j - 1
            if isPalindrome(i, j):
                return (i * j) % 1337


def isPalindrome(num1, num2):
    res = num1 * num2
    strin = str(res)
    length = len(strin)
    for i in range(0, ((length - 1) // 2) + 1):
        if strin[i] != strin[length - i - 1]:
            return False
    return True


res = int(n1 * n2)

i = n1
j = n2
print(myFunc(i, j))

# for i in range(i, 0, -1):
#     if isPalindrome(i, j):
#         print('YESSSSS ', (i * j) % 1337)
#     if j > 0:
#         j = j - 1
#         if isPalindrome(i, j):
#             print('YESSSSSSSSSSSSS ', (i * j) % 1337)
