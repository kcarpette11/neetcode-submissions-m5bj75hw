class TrieNode:
   def __init__(self):
     self.children = [None] * 26
     self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

   



        

    def insert(self, word: str) -> None:
        #insert string into prefix tree
        curr = self.root #initialize curr with root node
        for c in word: #iterate through string
            index = ord(c) - ord('a')
            if curr.children[index] is None: # if node does not exist, create a new one
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.endOfWord = True # end of the word



    def search(self, word: str) -> bool:
        # search for key 
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.endOfWord # return if true

        

    def startsWith(self, prefix: str) -> bool:
        #check for prefix
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False 
            curr = curr.children[index] # move to the next node
          
        return True

        
        