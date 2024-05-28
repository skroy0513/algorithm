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


Solution().productExceptSelf([-1, 1, 0., -3,3])