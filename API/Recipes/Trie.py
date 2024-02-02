from Recipes.TrieNodeAbstract import TrieNodeAbstract
from Recipes.ChildrenDictionary import ChildrenDictionary
import math
from typing import Dict, List, Union
# For help in traversing children
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


class Stack:
    """A last-in-first-out (LIFO) stack of items.

    Stores data in a last-in, first-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.
    """
    # === Private Attributes ===
    # _items:
    #     The items stored in this stack. The end of the list represents
    #     the top of the stack.
    _items: List

    def __init__(self) -> None:
        """Initialize a new empty stack."""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.
        """
        return self._items == []

    def push(self, item) -> None:
        """Add a new element to the top of this stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the element at the top of this stack.
        Raise an EmptyStackError if this stack is empty.
        """
        if self.is_empty():
            raise EmptyStackError
        else:
            return self._items.pop()


class EmptyStackError(Exception):
    """Exception raised when an error occurs."""
    pass


class TrieTree(TrieNodeAbstract):
    def __init__(self, char='', value: str = ''):
        '''
        Initializes:
            This node's char, `self._char`, ie. your current character in the key
            This node's set of subtrees, 'children', using a dictionary
            This node's value, `self._value`  only set iff its a valid word in the dictionary
        '''
        self._value = value
        self._children: ChildrenDictionary = ChildrenDictionary()
        self._char = char

    # TASK 1
    def insert(self, word: str) -> None:
        '''
        Insert your new word, keep in mind, you must insert all child nodes
        >>> trie = TrieTree()
        >>> trie.insert("")
        >>> trie.insert("word")
        >>> trie.insert("wood")
        >>> trie.insert("worm")
        >>> trie.insert("water")
        >>> trie.insert("banana")
        >>> "word" in str(trie)
        True
        >>> "wood" in str(trie)
        True
        >>> "worm" in str(trie)
        True
        >>> "water" in str(trie)
        True
        >>> "bob" in str(trie)
        False
        >>> "banana" in str(trie)
        True
        >>> "word" in trie
        True
        >>> "water" in trie
        True
        >>> "wat" in trie
        False
        >>> "banana" in trie
        True
        >>> "other" in trie
        False
        >>> "wor" in trie
        False
        >>> "waters" in trie
        False
        '''
        i = 0
        curr = self
        while i < len(word):
            if word[i] in curr._children.keys():
                curr = curr._children[word[i]]
                if i == len(word) - 1:
                    curr._value = word
                    return
                i += 1
            else:
                if i == len(word) - 1:
                    curr._children[word[i]] = TrieTree(word[i], word)
                    return
                curr._children[word[i]] = TrieTree(word[i])
                curr = curr._children[word[i]]
                i += 1
    # TASK 2

    def __contains__(self, key: str):
        '''
        Returns True iff key is in tree, otherwise False
        >>> trie = TrieTree()
        >>> trie.insert("word")
        >>> trie.insert("water")
        >>> trie.insert("wat")
        >>> trie.insert("banana")
        >>> "word" in trie
        True
        >>> "water" in trie
        True
        >>> "wat" in trie
        True
        >>> "banana" in trie
        True
        >>> "other" in trie
        False
        >>> "wate" in trie
        False
        >>> "waters" in trie
        False
        >>> "" in trie
        True
        '''
        if key == '':
            return True
        i = 0
        curr = self
        while i < len(key):
            if key[i] in curr._children.keys():
                curr = curr._children[key[i]]
                if i == len(key) - 1:
                    return curr._value == key
                i += 1
            else:
                return False
        return False

    # TASK 3
    def __delitem__(self, key: str):
        '''
        Deletes entry in tree and prunes unecessary branches if key exists, otherwise changes nothing
        >>> trie = TrieTree()
        >>> trie.insert("word")
        >>> "word" in trie
        True
        >>> del trie["word"]
        >>> "word" in trie
        False
        >>> str(trie)
        'TrieTree'
        >>> trie.insert('ab')
        >>> trie.insert('abs')
        >>> str(trie)
        'TrieTree\\n   `- a\\n      `- b : ab\\n         `- s : abs'
        >>> del trie['ab']
        >>> str(trie)
        'TrieTree\\n   `- a\\n      `- b\\n         `- s : abs'
        >>> trie.insert('ab')
        >>> str(trie)
        'TrieTree\\n   `- a\\n      `- b : ab\\n         `- s : abs'
        >>> del trie['abs']
        >>> str(trie)
        'TrieTree\\n   `- a\\n      `- b : ab'
        '''
        st = Stack()
        i = 0
        curr = self
        while i < len(key):
            if key[i] in curr._children.keys():
                st.push(curr)
                curr = curr._children[key[i]]
                if i == len(key) - 1:
                    if curr._value == key:
                        curr._value = None
                        while not st.is_empty():
                            if not curr._children and not curr._value:
                                parent = st.pop()
                                parent._children.pop(curr._char)
                                curr = parent
                            else:
                                return
                    return
                i += 1
            else:
                return
        return

    # TASK 4
    def sort(self, decreasing=False):
        '''
        Returns list of words in tree sorted alphabetically
        >>> trie = TrieTree()
        >>> trie.insert('banana')
        >>> trie.insert('cherry')
        >>> trie.insert('apple')
        >>> trie.sort()
        ['apple', 'banana', 'cherry']
        >>> trie.sort(decreasing=True)
        ['cherry', 'banana', 'apple']
        >>> trie1 = TrieTree()
        >>> trie1.insert('hi')
        >>> trie1.insert('bye')
        >>> trie1.insert('by')
        >>> trie1.insert('h')
        >>> trie1.insert('hihi')
        >>> trie1.sort()
        ['by', 'bye', 'h', 'hi', 'hihi']
        >>> trie1.sort(decreasing=True)
        ['hihi', 'hi', 'h', 'bye', 'by']
        '''

        if not decreasing:
            return self.sort_true()
        #lst = self.sort_true()
        #return lst[::-1]
        rev_alphabet = ALPHABET[::-1]
        return self.sort_false(rev_alphabet)

    def sort_true(self):
        """Helper for sort, returns a pre-order list"""
        if self._children == {}:
            if self._value:
                return [self._value]
            return []
        else:
            lst = []
            if self._value:
                lst += [self._value]
            for c in ALPHABET:
                if c in self._children.keys():
                    lst += self._children[c].sort_true()
            return lst

    def sort_false(self, rev_alphabet):
        """Helper for sort, returns a post-order list"""
        if self._children == {}:
            if self._value:
                return [self._value]
            return []
        else:
            lst = []
            for c in rev_alphabet:
                if c in self._children.keys():
                    lst += self._children[c].sort_false(rev_alphabet)
            if self._value:
                lst += [self._value]
            return lst

    # TASK 5
    def autoComplete(self, prefix, N=10):
        '''
        if given a valid prefix, return a list containing N number of suggestions starting with that prefix in alphabetical order
        else return an empty list
        >>> trie = TrieTree()
        >>> trie.insert('apple')
        >>> trie.insert('dad')
        >>> trie.insert('apples')
        >>> trie.insert('application')
        >>> trie.insert('app')
        >>> trie.insert('about')
        >>> trie.autoComplete('a')
        ['about', 'app', 'apple', 'apples', 'application']
        >>> trie.autoComplete('a', N=2)
        ['about', 'app']
        >>> trie.autoComplete('app')
        ['app', 'apple', 'apples', 'application']
        >>> trie.autoComplete('c')
        []
        >>> trie.autoComplete('d')
        ['dad']
        >>> trie = TrieTree()
        >>> trie.insert('dig')
        >>> trie.insert('dog')
        >>> trie.insert('dug')
        >>> trie.insert('duck')
        >>> trie.autoComplete('d', 4)
        ['dig', 'dog', 'duck', 'dug']
        >>> trie.autoComplete('d', 3)
        ['dig', 'dog', 'duck']
        >>> trie.autoComplete('', 2)
        ['dig', 'dog']
        '''
        if prefix == '':
            #lst = self.sort_true()
            #return lst[:N]
            return self.autocomplete_helper(N)
        i = 0
        curr = self
        while i < len(prefix):
            if prefix[i] in curr._children.keys():
                curr = curr._children[prefix[i]]
                if i == len(prefix) - 1:
                    return curr.autocomplete_helper(N)
                    #lst = curr.sort_true()
                    #return lst[:N]
                i += 1
            else:
                return []
        return []

    def autocomplete_helper(self, n):
        """Pre-order traversal using a loop, helper for autocomplete"""
        rev_alphabet = ALPHABET[::-1]
        lst = []
        stack = [self]
        while len(stack) > 0:
            current = stack.pop()
            if current._value and n > 0:
                lst.append(current._value)
                n -= 1
            for c in rev_alphabet:
                if c in current._children.keys():
                    stack.append(current._children[c])
        return lst

    # TASK 6
    def autoCorrect(self, word, errorMax=2):
        '''
        Given a word, if misspelt return a list of possible valid words from the last valid prefix, with up to errorMax errors
        >>> trie = TrieTree()
        >>> trie.insert('dab')
        >>> trie.autoCorrect('dod')
        ['dab']
        >>> trie.autoCorrect('dod', errorMax=1)
        []
        >>> trie.autoCorrect('dad', errorMax=1)
        ['dab']
        >>> trie.insert('apple')
        >>> trie.insert('dad')
        >>> trie.insert('dude')
        >>> trie.insert('apples')
        >>> trie.insert('application')
        >>> trie.insert('app')
        >>> trie.insert('about')
        >>> trie.insert("apples")
        >>> trie.insert("application")
        >>> trie.insert('app')
        >>> trie.insert('apple')
        >>> sorted(trie.autoCorrect('apl', errorMax=10))
        ['app', 'apple', 'apples', 'application']
        >>> trie.autoCorrect('aboot')
        ['about']
        >>> sorted(trie.autoCorrect('dea'))
        ['dab', 'dad']
        >>> sorted(trie.autoCorrect('dod'))
        ['dab', 'dad', 'dude']
        >>> sorted(trie.autoCorrect('dea', errorMax=3))
        ['dab', 'dad', 'dude']
        >>> trie = TrieTree()
        >>> trie.insert('dog')
        >>> trie.insert('dig')
        >>> trie.insert('duck')
        >>> trie.insert('dug')
        >>> trie.insert('lukasz')
        >>> trie.insert('dang')
        >>> trie.insert('aero')
        >>> sorted(trie.autoCorrect('deg', errorMax=2))
        ['dig', 'dog', 'dug']
        >>> trie = TrieTree()
        >>> trie.insert('dad')
        >>> sorted(trie.autoCorrect('d', errorMax=2))
        ['dad']
        >>> trie = TrieTree()
        >>> trie.insert('haha')
        >>> sorted(trie.autoCorrect('hehe', errorMax=2))
        ['haha']
        >>> trie = TrieTree()
        >>> trie.insert('a')
        >>> trie.insert('aa')
        >>> trie.insert('aaa')
        >>> trie.insert('aaaa')
        >>> trie.insert('aaaaa')
        >>> trie.insert('aaaaaa')
        >>> trie.insert('aaaaaaa')
        >>> sorted(trie.autoCorrect('ab'))
        ['aa', 'aaa']
        >>> sorted(trie.autoCorrect('ababaaa'))
        ['aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa']
        >>> trie = TrieTree()
        >>> trie.insert('apple')
        >>> trie.insert('apples')
        >>> sorted(trie.autoCorrect('applos'))
        ['apple', 'apples']
        '''
        i = 0
        curr = self
        while i < len(word):
            if word[i] in curr._children.keys():
                curr = curr._children[word[i]]
                if i == len(word) - 1:
                    if curr._value == word:
                        return [word]
                    return curr.helper_autoCorrect(i, word[:i], word, errorMax)
                i += 1
            else:
                return curr.helper_autoCorrect(i, word[:i], word, errorMax)
        return []

    def helper_autoCorrect(self, index, prefix, word, e):
        if e < 0:
            return []
        if self._children == {}:
            if self._value and e >= 0 and len(self._value) > len(prefix):
                return [self._value]
            return []
        else:
            lst = []
            if self._value and e >= 0 and len(self._value) > len(prefix):
                lst += [self._value]
            for c in self._children.keys():
                #if c in self._children.keys(): implementation using ALPHABET
                if len(word) > index and word[index] == c:
                    lst += self._children[c].helper_autoCorrect(index + 1, prefix, word, e)
                else:
                    lst += self._children[c].helper_autoCorrect(index + 1, prefix, word, e - 1)
            return lst

    # TASK 7
    def merge(self, otherTrie: TrieNodeAbstract):
        '''
        Merges another TrieTree into this one
        >>> trie1 = TrieTree()
        >>> trie2 = TrieTree()
        >>> trie1.insert('amazing')
        >>> trie2.insert('amazon')
        >>> trie1.merge(trie2)
        >>> 'amazon' in trie1
        True
        '''
        lst = otherTrie.sort(False)
        for word in lst:
            self.insert(word)
        return

    def pPrint(self, _prefix="", _last=True, index=0):
        '''
        DONT CHANGE THIS
        '''
        ret = ''
        if index:
            ret = _prefix + ("`- " if _last else "|- ") + self._char
            _prefix += "   " if _last else "|  "
            if self._value:
                ret += ' : ' + self._value
            ret += '\n'
        else:
            ret = _prefix + "TrieTree"
            _prefix += "   " if _last else "|  "
            ret += '\n'
        child_count = len(self._children)
        for i, child in enumerate(self._children):
            _last = i == (child_count - 1)
            ret += self._children[child].pPrint(_prefix, _last, index+1)
        return ret

    def __str__(self):
        return self.pPrint().strip()


trie = TrieTree()
trie.insert('apple')
trie.insert('apricot')
trie.insert('ariole')
trie.insert('chicken')
trie.insert('lamb')
trie.insert('calf')
trie.insert('beef')
trie.insert('onion')
trie.insert('garlic')
trie.insert('parsley')
trie.insert('olive')
trie.insert('bread')
trie.insert('rice')
trie.insert('spaghetti')
trie.insert('potato')
trie.insert('salt')
trie.insert('pepper')
trie.insert('sugar')
trie.insert('water')
trie.insert('honey')
trie.insert('cucumber')
trie.insert('flour')
trie.insert('vinegar')
trie.insert('lime')
trie.insert('lemon')
trie.insert('carrot')





# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
