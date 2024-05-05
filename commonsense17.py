class TrieNode:

    def __init__(self):
        self.children = {}

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        currentNode = self.root

        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                return None
            
        return currentNode
    
    def insert(self, word):
        currentNode = self.root
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                childNode = TrieNode()
                currentNode.children[char] = childNode

                currentNode = childNode

        currentNode.children["*"] = None

    def collectAllWords(self, node=None, word="", words=[]):

        currentNode = node or self.root

        for key, childNode in currentNode.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(childNode, word + key, words)
        
        return words
    
    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectAllWords(currentNode)


    def traverse(self, node = None):
        currentNode = node or self.root

        for key, child in currentNode.children.items():
            print(key)
            if key != "*":
                self.traverse(child)
    

    def autocorrect(self, prefix):

        returnWord = ""
        currentNode = self.root

        for char in prefix:
            if currentNode.children.get(char):
                returnWord += char
                currentNode = currentNode.children[char]
            else:
                while (currentNode.children):

                    firstChildKey = next(iter(currentNode.children.keys()), None)

                    if  firstChildKey == "*":
                        break

                    if firstChildKey:
                        returnWord += firstChildKey

                        currentNode = currentNode.children[firstChildKey]
                    else:
                        break
                return returnWord



        
        return returnWord
            
        
