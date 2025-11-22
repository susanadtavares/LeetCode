# Find Minimum Operations to Make All Elements Divisible by Three
# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.
# Return the minimum number of operations to make all elements of nums divisible by 3.

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if 1 <= len(nums) <= 50:
            nOperations = 0

            for num in nums:
                if not 1 <= num <= 50:
                    return 0
                if (num % 3) != 0:
                        nOperations = nOperations + 1
            return nOperations
        return 0