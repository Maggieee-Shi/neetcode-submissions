class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=collections.Counter(nums)
        heap=[]
        for num in dic.keys():
            heapq.heappush(heap,(dic[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        print(heap)
        res=[]
        for _ in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        return res