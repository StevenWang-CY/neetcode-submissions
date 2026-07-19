class Solution:
    def canAttendMeetings(self, intervals):
        
        # 按开始时间排序
        intervals.sort(key=lambda x: x.start)
        
        for i in range(1, len(intervals)):
            
            # 前一个会议结束时间
            prev_end = intervals[i-1].end
            
            # 当前会议开始时间
            curr_start = intervals[i].start
            
            # 有重叠
            if curr_start < prev_end:
                return False
        
        return True