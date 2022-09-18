# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True



class Trie:

    def __init__(self):
        self.d={}
        
    def insert(self, word: str) -> None:
        if word not in self.d.keys():
            self.d[word]=word

    def search(self, word: str) -> bool:
        if word in self.d.keys():
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for key in self.d.keys():
            if len(self.d[key])>=len(prefix) and self.d[key][:len(prefix)] == prefix:
                return True        
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
       

root1 = TreeNode(1)
root1.right = TreeNode(2)
# root1.left = TreeNode(1)
# root1.left.right = TreeNode(2)

# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(buildTree(preorder, inorder))

#LeetCode Solution

