class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        
        for i in range(len(nums)):
            # 当前点无法到达
            if i > maxReach:
                return False
            
            # 更新最远距离
            maxReach = max(maxReach, i + nums[i])
        
        return True