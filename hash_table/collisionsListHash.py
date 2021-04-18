import sys
sys.path.append("../dictionary_tree/dictionary")
from dictionaryUnorderedLinkedList import DictionaryUnorderedLinkedList
import hashFunctions

class DictCollisionListHash:
    """ Implementa una tabella hash con liste di collisione.

    Supporta le classiche operazioni di insert, search and delete key.
    """
    def __init__(self, size, singleHashFunction):
        if type(size) is not int:
            raise ValueError
        self.lists = size * [None]
        self.size = size
        for i in range(size):
            self.lists[i] = DictionaryUnorderedLinkedList()
        self.hashFunction = singleHashFunction

    def insert(self, key, value):
        ind = self.hashFunction.hash(key, self.size)
        self.lists[ind].insert(key, value)

    def delete(self, key):
        ind = self.hashFunction.hash(key, self.size)
        self.lists[ind].delete(key)

    def search(self, key):
        ind = self.hashFunction.hash(key, self.size)
        return self.lists[ind].search(key)

    def stampa(self):
        for i in range(0, self.size):
            self.lists[i].theList.stampa()


if __name__ == "__main__":
    size = 13;
    fdiv = hashFunctions.HashFunction_module()
    frip = hashFunctions.HashFunction_Adv()

    print ("Metodo divisione")

    diz = DictCollisionListHash(size, fdiv)
    for i in range(0, 30):
        print ("insert(" + str(i) + "," + str(2 * i) + ")")
        diz.insert(i, 2 * i)
    diz.stampa()

    print ("Metodo ripiegamento")

    diz = DictCollisionListHash(size, frip)
    for i in range(0, 30):
        print ("insert(" + str(i) + "," + str(2 * i) + ")")
        diz.insert(i, 2 * i)
    diz.stampa()

