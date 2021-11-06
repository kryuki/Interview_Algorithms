'''
Faster Trie
this can be used in the trie structure when you have to count the number of children
(ex: https://www.interviewbit.com/problems/shortest-unique-prefix/)
'''

class TrieNode:
    def __init__(self):
        self.trie = {}
        self.children = 0
    def add_word(self, word):
        cur = self
        for char in word:
            if char not in cur.trie:
                cur.trie[char] = TrieNode()
            cur.children += 1
            cur = cur.trie[char]
        cur.trie['$'] = True
    def get_unique(self, word):
        cur = self
        for i, char in enumerate(word):
            if cur.children == 1:
                return word[:i]
            cur = cur.trie[char]
        return word

class Solution:
	def prefix(self, strs):
        trie = TrieNode()
        for s in strs:
            trie.add_word(s)
        
        res = []
        for s in strs:
            res.append(trie.get_unique(s))
        
        return res




