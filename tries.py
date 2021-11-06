'''
Basic Trie data structure
'''

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26
    
    def get_idx(self, s):
        return ord(s) - ord('a')
    
    def get_char(self, idx):
        return chr(idx + ord('a'))

    def add_word(self, s):
        if not s:
            self.isEnd = True
            return

        if not self.children[self.get_idx(s[0])]:
            self.children[self.get_idx(s[0])] = TrieNode()

        self.children[self.get_idx(s[0])].add_word(s[1:])
    
    # inorder traversal of the tree
    def printout(self, s=""):
        if self.isEnd:
            print(s)

        for i in range(26):
            if self.children[i]:
                new_s = s + self.get_char(i)
                self.children[i].printout(new_s)

# driver code
trie = TrieNode()
while True:
    s = input()
    if s == "done":
        break
    trie.add_word(s)

print("------The dictionary is------")
trie.printout()