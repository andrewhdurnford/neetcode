class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        wildcard = defaultdict(set)
        for word in wordList:
            for i in range(n):
                wildcard[word[0:i] + '*' + word[i + 1:n]].add(word)

        visit = set([beginWord])
        q = deque([beginWord])
        distance = 0


        while q:
            distance += 1
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(n):
                    s = word[0:i] + '*' + word[i + 1:n]
                    neighbors = wildcard[s]
                    for nei in neighbors:
                        if nei == endWord:
                            return distance + 1
                        
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)

        return 0
