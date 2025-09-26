from trie import *


class TrieComparator:

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

    def same_document(T1, T2):
        """Devuelve True si ambos tries representan el mismo documento"""
        palabras_T1 = TrieComparator.get_all_words(T1)
        palabras_T2 = TrieComparator.get_all_words(T2)
        return palabras_T1 == palabras_T2



t1 = Trie()
t1.insert("hola")
t1.insert("mundo")
t1.insert("python")

t2 = Trie()
t2.insert("python")
t2.insert("mundo")
t2.insert("hola")

print(TrieComparator.same_document(t1, t2))  # True

t3 = Trie()
t3.insert("hola")
t3.insert("java")

print(TrieComparator.same_document(t1, t3))  # False