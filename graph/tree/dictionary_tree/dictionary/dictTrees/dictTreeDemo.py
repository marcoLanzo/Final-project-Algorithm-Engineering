from dictionary.dictionaryListDemo import test
from dictBinaryTree import DictBinaryTree
from dictionaryAVL import DictAVL
from time import time
 
def testBinary(steps, avl):
    diz = None
    if avl:
        diz = DictAVL()
    else:
        diz = DictBinaryTree() 
    
    print "\nTest di {} (tempo medio per ogni operazione, calcolato su {} chiamate):\n".format(("DictionaryAVL" if avl else "DictionaryBinaryTree"), steps)
    
    start = time()
    for i in range(steps):
        diz.insert(2 * i, i)
    elapsed = time() - start
    print "Tempo medio insert:", elapsed / steps
    
    start = time()
    for i in range(steps):
        diz.search(2 * i)
    elapsed = time() - start
    print "Tempo medio search a buon fine:", elapsed / steps
    
    start = time()
    for i in range(steps):
        diz.search(2 * i + 1)
    elapsed = time() - start
    print "Tempo medio search di elementi non presenti:", elapsed / steps
    
    start = time()
    for i in range(steps):
        diz.delete(2 * i)
    elapsed = time() - start
    print "Tempo medio delete:", elapsed / steps
    

if __name__ == "__main__":
    steps = 2000
    test(steps)
    testBinary(steps, False)
    testBinary(steps, True)
    
