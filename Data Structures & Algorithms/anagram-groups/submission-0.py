from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s: str, t: str) -> bool:
            if len(s) != len (t):
                return False
            
            count_t, count_s = {}, {}

            for i in range(len(s)):
                count_t[t[i]] = count_t.get(t[i],0) + 1
                count_s[s[i]] = count_s.get(s[i],0) + 1
            return count_t == count_s

        mp = defaultdict(list)

        for str in strs:
            added = False
            for key in mp.keys():
                if isAnagram(str, key):
                    mp[key].append(str)
                    added = True
            if not added:
                mp[str].append(str)
        empty_list = []
        for str_list in mp.values():
            empty_list.append(str_list)
        
        return empty_list
                
            
        