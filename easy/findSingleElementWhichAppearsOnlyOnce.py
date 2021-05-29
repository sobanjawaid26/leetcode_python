# presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
# for i in range(len(presidents)):
#     print("President {}: {}".format(i + 1, presidents[i]))
from typing import List

nums = [3, 3, 7, 7, 10, 11, 11]


for i in range(len(nums) - 1):
    if i % 2 == 0 and nums[i] != nums[i + 1]:
        print(nums[i])

