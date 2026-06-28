class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_dic = dict()
        for num in nums:
            if num in hash_dic.keys():
                return True
            hash_dic[num] = 1
        return False
