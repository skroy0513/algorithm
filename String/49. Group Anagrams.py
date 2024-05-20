import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            print(''.join(sorted(word)))
            print(sorted(word))
            anagrams['_'.join(sorted(word))].append(word)
        print(anagrams.values())
        return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Solution.groupAnagrams(Solution, strs)