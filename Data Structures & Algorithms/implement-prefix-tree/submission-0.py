class PrefixTree:

    def __init__(self):

        self.store = set()
        self.tree = {}
        self.tree["#"] = {}
        

    def insert(self, word: str) -> None:

        self.store.add(word)

        node = self.tree["#"]

        for c in word:
            if c in node:
                node = node[c]

            else:
                node[c] = {}
                node = node[c]

        return None


    def search(self, word: str) -> bool:

        if word in self.store:
            return True

        return False
        

    def startsWith(self, prefix: str) -> bool:

        node = self.tree["#"]

        for c in prefix:

            if c in node:
                node = node[c]

            else:
                return False


        return True
        
        