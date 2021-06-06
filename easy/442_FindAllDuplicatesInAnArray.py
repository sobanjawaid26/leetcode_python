from typing import List

# nums = [4, 3, 2, 7, 8, 2, 3, 1]
nums = [1, 1]
# nums = [10,2,5,10,9,1,1,4,3,7]

# [1, 2, 2, 3, 3, 4, 7, 8]


def findDuplicates(nu: List[int]) -> List[int]:
    nu.sort()
    print(nu)
    output = []
    temp = nu[0]
    # if len(nu) == 2 and nu[0] == nu[1]:
    #     output.append(nu[0])
    for i in range(1, len(nu)):
        # print(temp, nu[i])
        if temp == nu[i]:
            output.append(temp)
        temp = nu[i]
    return output


print(findDuplicates(nums))
