from trie import *

class TrieUtils:

    def get_all_words(trie):
        """Devuelve un conjunto con todas las palabras del trie"""
        result = set()

        def dfs(node, path):
            if node.isEndOfWord:
                result.add("".join(path))
            current = node.children.head
            while current:
                child = current.value
                dfs(child, path + [child.key])
                current = current.next

        dfs(trie.root, [])
        return result

    def has_inverted_pairs(trie):
        """Devuelve True si existen dos palabras invertidas en el trie"""
        words = TrieUtils.get_all_words(trie)
        for word in words:
            if word[::-1] in words and word[::-1] != word:  # evitar palíndromos
                return True
        return False


t = Trie()
t.insert("abcd")
t.insert("dcba")
t.insert("python")
t.insert("nothyp")

print(TrieUtils.has_inverted_pairs(t))  # True (abcd/dcba, python/nothyp)

t2 = Trie()
t2.insert("hola")
t2.insert("mundo")

print(TrieUtils.has_inverted_pairs(t2))  # False
