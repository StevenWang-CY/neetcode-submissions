from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_dict = defaultdict(int)
        for letter in s:
            letter_dict[letter] += 1
        for letter in t:
            letter_dict[letter] -= 1
        return set(letter_dict.values()) == {0}
        