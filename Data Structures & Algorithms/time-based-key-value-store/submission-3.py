class TimeMap:

    def __init__(self):
        self.data = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        # If no data, return empty string
        if not self.data[key]: return ""
        
        # Get previous value
        dct = self.data[key]
        lst = list(dct.keys())
        l, r = 0, len(lst) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2
            
            if lst[m] <= timestamp:
                res = dct[lst[m]]
                l = m + 1
            else:
                r = m - 1
        
        return res



