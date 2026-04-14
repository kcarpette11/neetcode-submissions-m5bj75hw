class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
          
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
           
     
    

        

    def search(self, word: str) -> bool:
        nodes = [self.root]
        for c in word:
            new_nodes = []
            for node in nodes:
                if c == ".":
                    new_nodes.extend(node.children.values())
                else:
                    if c in node.children:
                        new_nodes.append(node.children[c])
            if not new_nodes:
                return False
            nodes = new_nodes
        return any(node.word for node in nodes)
       
            
                

        
    

        
