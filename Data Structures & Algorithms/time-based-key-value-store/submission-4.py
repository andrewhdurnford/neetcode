class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append([value, timestamp])
        return None

    def get(self, key: str, timestamp: int) -> str:
        if self.keys[key] == []: return ""
        lst = self.keys[key]
        l, r = 0, len(lst) - 1
        res = ""

        while l <= r:
            m = l + ((r - l) // 2)

            if lst[m][1] <= timestamp:
                l = m + 1
                res = lst[m][0]
            else:
                r = m - 1
        
        return res
            