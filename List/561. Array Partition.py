from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        answer = 0
        for i in range(len(nums)//2):
            answer += min(nums[i*2], nums[i*2 + 1])
            print(i)
        print(answer)

Solution().arrayPairSum([6,2,6,5,1,2])