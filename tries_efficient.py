'''
Faster Trie
this can be used in basic trie structure (without having to count the number of children)
(ex: https://leetcode.com/problems/implement-trie-prefix-tree/)
'''

class Trie:
    def __init__(self):
        self.trie = {}
    
    def add_word(self, word):
        trie = self.trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie['$'] = True
    
    def search(self, word):
        trie = self.trie
        for char in word:
            if char not in trie:
                return False
            trie = trie[char]
        return '$' in trie
    
    def starts_with(self, prefix):
        trie = self.trie
        for char in prefix:
            if char not in trie:
                return False
            trie = trie[char]
        return True

t = Trie()
while True:
    w = input()
    if w == "done":
        break
    t.add_word(w)

