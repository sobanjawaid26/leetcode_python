amount = 5
coins = [1, 2, 5]
l = len(coins)
# coins.sort(reverse=True)
counter = 0

# for row in range(0, l):
#     tempSum = amount
#     for col in range(row, l):
#         if tempSum != 0 and tempSum > 0:
#             tempSum = tempSum - coins[col]
#     if tempSum == 0:
#         counter = counter + 1
# print(counter)


dic = {0: 1}
for coin in coins:
    for j in range(amount + 1):
        dic[j] = dic.get(j, 0) + dic.get(j - coin, 0)
print(dic.get(amount, 0))
