class TimeMap:

    def __init__(self):
        
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp,value))
                

    def get(self, key: str, timestamp: int) -> str:

        li = self.timeMap.get(key,[])

        l = 0
        r = len(li)-1
        res = ""
        while l<=r:
            mid = (l+r)//2
            if li[mid][0] > timestamp:
                r = mid-1

            else :
                l = mid+1
                res = li[mid][1]

        return res
            
                
        
        
        
