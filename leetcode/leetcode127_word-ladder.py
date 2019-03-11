'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''
from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def construct_dict(wordList):
            d = {}
            for word in wordList:
                for i in range(len(word)):
                    key = word[:i] + "_" + word[i+1:]
                    d[key] = d.get(key, []) + [word]
            print "d = ", d
            return d

        def bfs(beginWord, endWord, wordList):
            
            print "beginWord = ", beginWord, " endWord = ", endWord, " wordList = ", wordList
            print "wordList.values() = ", wordList.values()
            queue = deque([(beginWord, 1)])
            visited = set()
            print "000 queue = ",queue
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == endWord:
                        return steps
                    for i in range(len(word)):
                        key = word[:i] + "_" + word[i+1:]
                        neigh_words = wordList.get(key, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps+1))
            print "queue = ", queue
            return 0

    
        d = construct_dict(wordList )
        print " 111 d = ", d
        return bfs(beginWord, endWord, d)



if __name__ == '__main__':
    s = Solution()
    
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    ret = s.ladderLength(beginWord, endWord, wordList)
    print "ret = ", ret









