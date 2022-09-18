# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True



class WordDictionary:
    def __init__(self):
        self.trie = {}
        
    def addWord(self, word): # e.g., root -> [s] -> [e] -> [a] -> ['$']
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = None # end of word
        
    def search(self, word):
        n = len(word)
        def dfs(node, char_index = 0): # e.g., char_index, 0, 1, 2: [s] (0) -> [e] (1) -> [a] (2)  
            if char_index == n:
                return '$' in node
            if word[char_index] == ".":
                for letter in node:
                    if letter != '$' and dfs(node[letter], char_index+1):
                        return True
            elif word[char_index] in node:
                return dfs(node[word[char_index]], char_index+1)
            else:
                return False
        return dfs(self.trie)

test = WordDictionary()

word='bad'
test.addWord(word)
word='dad'
test.addWord(word)
word='mad'
test.addWord(word)
word='pad'
print(test.search(word))
word='bad'
print(test.search(word))
word='.ad'
print(test.search(word))
word='b..'
print(test.search(word))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
       


# root1.left = TreeNode(1)
# root1.left.right = TreeNode(2)

# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)

#LeetCode Solution

