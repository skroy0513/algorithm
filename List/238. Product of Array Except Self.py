from typing import List
from math import prod


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            list = nums.copy()
            list.remove(i)
            mul = prod(list)
            answer.append(int(mul))
        print(answer)
        return answer
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        answer = []
        p = 1
        for i in nums:
            answer.append(p)
            p = p * i
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * p
            p = p * nums[i]
        print(answer)
        return answer

Solution().productExceptSelf2([1, 2, 3, 4])