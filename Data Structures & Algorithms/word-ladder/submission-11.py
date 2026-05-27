class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # word -> template
        # template -> word
        # bfs starting at beginWord
        # on visit, go through each template beginWord is in
        # at each template add each non-visited word to the q
        # track length
        if endWord not in wordList:
            return 0

        words = defaultdict(list)
        temps = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                temp = word[0:i] + '*' + word[i + 1: len(word)]
                words[word].append(temp)
                temps[temp].append(word)

        for i in range(len(beginWord)):
            temp = beginWord[0:i] + '*' + beginWord[i + 1: len(beginWord)]
            words[beginWord].append(temp)

        q = deque([beginWord])
        visit = set([beginWord])
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                for temp in words[word]:
                    for nei in temps[temp]:
                        if nei == endWord:
                            return res + 1
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
        
        return 0



        

