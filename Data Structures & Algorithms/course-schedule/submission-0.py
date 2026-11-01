class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        visited=set()
        freqmap = {i: [] for i in range(numCourses)}
        for crs, pres in prerequisites:
            freqmap[crs].append(pres)
        
        def dfs(crs):
            if crs in visited:
                return False
            if not freqmap[crs]:
                return True
            visited.add(crs)
            for course in freqmap[crs]:
                if not dfs(course):
                    return False
    
            visited.remove(crs)
            freqmap[crs]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
