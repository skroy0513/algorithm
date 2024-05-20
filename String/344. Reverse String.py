from typing import List


class Soloution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            k = len(s) - 1
            s[i], s[k - i] = s[k - i], s[i]
    def reverseString2(self, s: List[str]) -> None:
        s.reverse()

s = ["h", "e", "l", "l", "o"]
Soloution.reverseString(Soloution, s)