from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return[num_map[complement], i]
            num_map[num] = i

# instance of solution class
sol = Solution()

nums = [3, 2, 4]
target = 6
print(sol.twoSum(nums, target))