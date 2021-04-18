from collisionsListHash import DictCollisionListHash
from openIndexingHash import DictOpenIndexingHash
from time import time
import hashFunctions

def testHash(steps, collList, hashFunction):
    """Semplice funzione per testare le tabelle hash.

    Dato in input il numero di iterazioni, una funzione hash ed un flag per
    testare collisioni, verranno svolte le operazioni tipiche di una tabella hash
    e dati in output le performance ottenute.
    """
    diz = None

    if collList:
        diz = DictCollisionListHash(int(steps / 5), hashFunction)
    else:
        diz = DictOpenIndexingHash(steps, hashFunction)

    print ("\tTest di {} (tempo medio per ogni operazione, calcolato su {}"\
           " chiamate):".format(
         ("DictionaryCollisionList" if collList else "DictionaryOpenIndexing")
         , steps))

    start = time()
    for i in range(steps):
        diz.insert(2 * i, i)
    elapsed = time() - start
    print ("\tTempo medio insert: \t\t\t\t%4.10f" % (elapsed / steps))

    start = time()
    for i in range(steps):
        diz.search(2 * i)
    elapsed = time() - start
    print ("\tTempo medio search a buon fine: \t\t%4.10f" % (elapsed / steps))

    start = time()
    for i in range(steps):
        diz.search(2 * i + 1)
    elapsed = time() - start
    print ("\tTempo medio search di elementi non presenti: \t%4.10f" \
            % (elapsed / steps))

    start = time()
    for i in range(steps):
        diz.delete(2 * i)
    elapsed = time() - start
    print ("\tTempo medio delete: \t\t\t\t%4.10f" % (elapsed / steps))


if __name__=="__main__":
    steps=2000

    f1d=hashFunctions.HashFunction_module()
    f1r=hashFunctions.HashFunction_Adv()
    f2=hashFunctions.doubleHash()
    f2linear=hashFunctions.doubleHash_linearScan()
    f2quad=hashFunctions.doubleHash_quadraticScan()
    print ("\nDouble hash")
    testHash(steps,False,f2)
    print ("\nDouble hash linear")
    testHash(steps,False,f2linear)
    print ("\nDouble hash quadratic")
    testHash(steps,False,f2quad)
    print ("\nHash divisione")
    testHash(steps,True,f1d)
    print ("\nHash ripiegamento")
    testHash(steps,True,f1r)
