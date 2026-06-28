class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()
        for i, num in enumerate(nums):
            potential_pair = target - num
            if potential_pair in num_dict:
                return [num_dict[potential_pair], i]
            num_dict[num] = i
            
        