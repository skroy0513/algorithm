## 125. Valid Palindrome
import collections


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s :
            if char.isalnum():              # isalnum() : 해당 문자열이 영문자, 숫자 여부를 판별하는 함수
                strs.append(char.lower())   # 함수를 통과한다면 소문자로 변환하여 strs에 추가
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():   # 0을 지정하면 맨 앞의 값을 가져와서 맨 뒤의 값과 비교
                return False                # 맨 앞과 뒤가 같지 않다면 False를 바로 반환
        return True

    def isPalindrome2(self, s: str) -> bool:
        strs : Deque = collections.deque()      # strs를 배열이 아닌 Deque로 지정

        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.popleft() != strs.pop():    # .popleft()를 통해 맨 앞의 값을 추출하여 맨 뒤의 값과 비교
                return False
        return True

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "
Solution.isPalindrome2(Solution, s1)