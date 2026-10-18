class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i=0
        res=[]
        start=intervals[0][0]
        end=intervals[0][1]
        while i<len(intervals):
            if i+1>=len(intervals):
                res.append([start,end])
                break

            if end>=intervals[i+1][0]:
                end=max(end,intervals[i+1][1])
                i+=1
            else:
                res.append([start,end])
                start=intervals[i+1][0]
                end=intervals[i+1][1]
            
        return res

            