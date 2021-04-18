from time import time
from random import randint
import Selection

# Global parameters
amount = 100000
position = amount / 2

def test1():
    print "Input gia' ordinato. Lista di {} elementi.\n".format(amount)
    
    l = range(amount)
    start = time()
    res = Selection.sortSelect(l, position)
    elapsed = time() - start
    print "sortSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res)
    
    l = range(amount)
    start = time()
    res = Selection.heapSelect(l, position)
    elapsed = time() - start
    print "heapSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res)
    
    l = range(amount)
    start = time()
    res = Selection.quickSelectRand(l, position)
    elapsed = time() - start
    print "quickSelectRand takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res)
    
    l = range(amount)
    minLen = 0
    start = time()
    res = Selection.quickSelectDet(l, position, minLen)
    elapsed = time() - start
    print "quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen, elapsed, position, res)
    
    l = range(amount)
    minLen = 15
    start = time()
    res = Selection.quickSelectDet(l, position, minLen)
    elapsed = time() - start
    print "quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen, elapsed, position, res)
    
    l = range(amount)
    minLen = 30
    start = time()
    res = Selection.quickSelectDet(l, position, minLen)
    elapsed = time() - start
    print "quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen, elapsed, position, res)
    
    if trivial:
        l = range(amount)
        start = time()
        res = Selection.trivialSelect(l, position)
        elapsed = time() - start
        print "trivialSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res)
    
    print "\nEnd."

def test2():
    print "Input ordinato inversamente. Lista di {} elementi.\n".format(amount)
    
    l = range(amount, -1, -1)
    start = time()
    res = Selection.sortSelect(l, position)
    elapsed = time() - start
    print "sortSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res)
    
    l = range(amount, -1, -1)
    start = time()
    res = Selection.heapSelect(l, position)
    elapsed = time() - start
    print "heapSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res)
    
    l = range(amount, -1, -1)
    start = time()
    res = Selection.quickSelectRand(l, position)
    elapsed = time() - start
    print "quickSelectRand takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res)
    
    l = range(amount, -1, -1)
    minLen = 0
    start = time()
    res = Selection.quickSelectDet(l, position, minLen)
    elapsed = time() - start
    print "quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen, elapsed, position, res)
    
    l = range(amount, -1, -1)
    minLen = 15
    start = time()
    res = Selection.quickSelectDet(l, position, minLen)
    elapsed = time() - start
    print "quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen, elapsed, position, res)
    
    l = range(amount, -1, -1)
    minLen = 30
    start = time()
    res = Selection.quickSelectDet(l, position, minLen)
    elapsed = time() - start
    print "quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen, elapsed, position, res)
    
    if trivial:
        l = range(amount, -1, -1)
        start = time()
        res = Selection.trivialSelect(l, position)
        elapsed = time() - start
        print "trivialSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res)
    
    print "\nEnd."

def test3():
    print "Input random(0,{}). Lista di {} elementi.\n".format(amount, amount)
    
    basel = [randint(0, amount) for i in range(amount)] #@UnusedVariable
    l=list(basel)
    start = time()
    res = Selection.sortSelect(l, position)
    elapsed = time() - start
    print "sortSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res)
    
    l=list(basel)
    start = time()
    res = Selection.heapSelect(l, position)
    elapsed = time() - start
    print "heapSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res)
    
    l=list(basel)
    start = time()
    res = Selection.quickSelectRand(l, position)
    elapsed = time() - start
    print "quickSelectRand takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res)
    
    l=list(basel)
    minLen = 0
    start = time()
    res = Selection.quickSelectDet(l, position, minLen)
    elapsed = time() - start
    print "quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen, elapsed, position, res)
    
    l=list(basel)
    minLen = 5
    start = time()
    res = Selection.quickSelectDet(l, position, minLen)
    elapsed = time() - start
    print "quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen, elapsed, position, res)
    
    l=list(basel)
    minLen = 30
    start = time()
    res = Selection.quickSelectDet(l, position, minLen)
    elapsed = time() - start
    print "quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen, elapsed, position, res)
    
    if trivial:
        l=list(basel)
        start = time()
        res = Selection.trivialSelect(l, position)
        elapsed = time() - start
        print "trivialSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res)
    
    print "\nEnd."

if __name__ == "__main__":
    test1()
    test2()
    test3()
