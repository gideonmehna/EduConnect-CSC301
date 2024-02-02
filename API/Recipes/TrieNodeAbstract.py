from abc import abstractclassmethod
from Recipes.ChildrenDictionary import ChildrenDictionary
import math
from typing import Dict
# For help in traversing children


class TrieNodeAbstract():
    @abstractclassmethod
    def __init__(self, char='', value: str = ''):
        self._value: str = value
        self._children: ChildrenDictionary = ChildrenDictionary()
        self._char: str = char

    @abstractclassmethod
    def insert(self, word: str) -> None:

        raise NotImplementedError

    @abstractclassmethod
    def __contains__(self, key: str):

        raise NotImplementedError

    @abstractclassmethod
    def __delitem__(self, key: str):

        raise NotImplementedError

    @abstractclassmethod
    def sort(self, decreasing=False):

        raise NotImplementedError

    @abstractclassmethod
    def autoComplete(self, prefix, N=10):

        raise NotImplementedError

    @abstractclassmethod
    def autoCorrect(self, word, errorMax=2):

        raise NotImplementedError

    @abstractclassmethod
    def merge(self, otherTrie):

        raise NotImplementedError
