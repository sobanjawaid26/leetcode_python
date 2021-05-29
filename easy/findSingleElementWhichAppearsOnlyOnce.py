# presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
# for i in range(len(presidents)):
#     print("President {}: {}".format(i + 1, presidents[i]))
from typing import List

nums = [1, 1, 2]

if len(nums) == 1:
    print(nums[0])
if (len(nums) - 1) % 2 == 0 and nums[len(nums) - 1] != nums[len(nums) - 2]:
    print(nums[len(nums) - 1])
for i in range(len(nums) - 1):
    if i % 2 == 0 and nums[i] != nums[i + 1]:
        print(nums[i])
