from Final.data_structures.hash_table import DynamicHash
from Final.data_structures.queue import Queue


class TrieNode:
    def __init__(self):
        self.children = DynamicHash()
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.is_end_of_word = True

    def search(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.is_end_of_word

    def starts_with(self, word):
        """ checks if there is any word that starts with the given word """
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True

    def print(self, curr_node=None, word=""):
        if curr_node is None:
            curr_node = self.root

        if curr_node.is_end_of_word:
            print(" -", word)

        for char in curr_node.children:
            child_node = curr_node.children[char]
            if child_node is not None:
                self.print(child_node, word + char)

    def get_all_words(self, curr_node=None, prefix="", words=None):
        if words is None:
            words = Queue()

        if curr_node is None:
            curr_node = self.root

        if curr_node.is_end_of_word:
            words.enqueue(prefix)

        for char in curr_node.children:
            child_node = curr_node.children[char]
            self.get_all_words(child_node,prefix + char, words)

        return words
