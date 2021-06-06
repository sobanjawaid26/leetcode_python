myList = [-3, 2, 0, -6, 3, 7, -9]

print('##########################        1       #####################################')


def Pos_Neg(num):
    if num == 0:
        print('ZERO')
    else:
        if num > 0:
            print('Positive')
        else:
            print('Negative')


# for num in myList:
#     Pos_Neg(num)

print('##########################        2       #####################################')

for row in range(5):
    for col in range(5):
        print(col, end=' ')
    print()

print('##########################        3       #####################################')

for row in range(1, 11):
    for col in range(1, row + 1):
        print(col, end=' ')
    print()
print(dir())

print('##########################        4       #####################################')
