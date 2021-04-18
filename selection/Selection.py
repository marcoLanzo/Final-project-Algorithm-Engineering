from HeapMin import HeapMin
from __init__ import printSwitch
from math import ceil
from sorting.Sorting import mergeSort, partition

def trivialSelect(l, position):
    if printSwitch.dumpOperations:
        print("trivialSelect of ", str(l), "with position", str(position))
    length = len(l)
    if position <= 0 or position > length:
        return None

    for i in range(0, position):
        minimum = i
        for j in range(i + 1, length):
            if l[j] < l[minimum]:
                minimum = j
        l[minimum], l[i] = l[i], l[minimum]
    if printSwitch.dumpOperations:
        print("  returns", l[position - 1])
    return l[position - 1]


# Ordina la sequenza in input, e restituisce il k-esimo elemento. Richiede tempo O(n log n)
def sortSelect(l, position):
    if printSwitch.dumpOperations:
        print("sortSelect")
    if position <= 0 or position > len(l):
        return None
    mergeSort(l)
    if printSwitch.dumpOperations:
        print(l)
    return l[position - 1]

def heapSelect(l, position):
    if printSwitch.dumpOperations:
        print("heapSelect")
    if position <= 0 or position > len(l):
        return None
    
    heap = HeapMin(l)
    heap.heapify()
    if printSwitch.dumpOperations:
        print(heap.heap)
    for i in range(0, position - 1):  # @UnusedVariable i
        heap.deleteMin()
    if printSwitch.dumpOperations:
        print(heap.heap)
    
    return heap.findMin()

# QUICKSELECT RANDOMIZZATO (ricorsivo)
""" Prende un perno random x, ed individua gli elementi A <= di x e quelli B >x.
    Se |A|+1=k, l'elemento cercato e' x. Se |A|<=k, prosegue ricorsivamente la ricerca
    in A.
    Altrimenti prosegue ricorsivamente su B, questa volta cercando k'=k-(|A|+1)
    Richiede tempo atteso O(n)
    Somiglia a quickSort randomizzato, con la differenza che si fa una sola chiamata
    ricorsiva anziche' 2
    (il che suggerisce perche' il tempo d'esecuzione sia migliore)
"""

def quickSelectRand(l, position): #position 1...n
    if position <= 0 or position > len(l):
        return None
    return recursiveQuickSelectRand(l, 0, len(l) - 1, position)
    
def recursiveQuickSelectRand(l, left, right, position):
    if printSwitch.dumpOperations:
        print("recursiveQuickSelectRand({},{},{})".format(left, right, position))
    
    if left > right: #controllo superfluo
        return
    
    if left == right and position - 1 == left:
        return l[position - 1]
        
    mid = partition(l, left, right)
    if printSwitch.dumpOperations:
        print("mid: {}".format(mid))
    
    if position - 1 == mid:
        return l[mid]
    if position - 1 < mid:
        return recursiveQuickSelectRand(l, left, mid - 1, position)
    else:
        return recursiveQuickSelectRand(l, mid + 1, right, position)

# End of quickSelect

# QUICKSELECT DETERMINISTICO
""" Divide l'input in gruppi di 5 (tranne al piu' l'ultimo gruppo), e per ciascun
    gruppo calcola il mediano.
    Quindi calcola ricorsivamente il mediano dei mediani, ed utilizza quello come perno.
    Si puo' dimostrare che sia la sottosequenza sinistra che quella destra contengono
    al piu' 7n/10 elementi.
    Quindi il tempo d'esecuzione dell'algoritmo e' T(n)=O(n)+T(n/5)+T(7n/10)=O(n)
"""
def quickSelectDet(l, position, minLen, whoami="QuickSelectDet"):
    if position <= 0 or position > len(l):
        return None
    return recursiveQuickSelectDet(l, 0, len(l) - 1, position, minLen, whoami)

def recursiveQuickSelectDet(l, left, right, position, minLen, whoami):
    if printSwitch.dumpOperations:
        condOutput(whoami, "recursiveQuickSelectDet({},{},{},{})".format(left, right, position, minLen) + "\n" + "[" + "- "*left + str(l[left:right + 1])[1:-1] + "- "*(len(l) - right - 1) + "]")

    if left == right:
        return l[left]

    # si usa stop per decidere quando smettere di ricorrere ed utilizzare un algoritmo diverso
    if len(l) < minLen:
        med = trivialSelect(l[ left: right + 1], position - left)
        if printSwitch.dumpOperations:
            condOutput(whoami, "return:" + str(med))
        return med

    # compute groups of five
    numElem = right - left + 1
    numGroups = int(ceil(numElem / 5.0))
    median = []
    for i in range(0, numGroups):
        dimGroup = (5) if (i < numGroups - 1 or numElem % 5 == 0) else (numElem - (numGroups - 1) * 5)
        a = left + i * 5
        b = left + i * 5 + dimGroup - 1

        if printSwitch.dumpOperations:
            condOutput(whoami, "dimGroup: " + str(dimGroup) + "\n" + "Compute median in group {}".format(l[a:b + 1]))
        m = trivialSelect(l[a:b + 1], int(ceil(dimGroup / 2.0)))
        median.append(m)

    if printSwitch.dumpOperations:
        condOutput(whoami, "Compute the median of " + str(median))
    vperno = quickSelectDet(median, ceil(len(median)/2), minLen, "Median Recursion on list {}".format(median))

    if printSwitch.dumpOperations:
        condOutput(whoami, "Partitioning wrt " + str(vperno))
    perno = partitionDet(l, left, right, vperno)  # Watch: this is a new function which takes  the pivot as the parameter

    posperno = perno + 1
    if posperno == position:
        if printSwitch.dumpOperations:
            condOutput(whoami, "return " + str(l[perno]))
        return l[perno]
    if posperno > position:
        if printSwitch.dumpOperations:
            condOutput(whoami, "Recursion on the LEFT partition.")
        return recursiveQuickSelectDet(l, left, perno - 1, position, minLen, whoami)
    else:
        if printSwitch.dumpOperations:
            condOutput(whoami, "Recursion on the RIGHT partition.")
        return recursiveQuickSelectDet(l, perno + 1, right, position, minLen, whoami)

def partitionDet(l, left, right, pivot):
    inf = left
    sup = right

    while True:
        while inf <= right and l[inf] <= pivot:
            if l[inf] == pivot and l[left] != pivot:
                l[left], l[inf] = l[inf], l[left]
            else:
                inf += 1

        while sup >= 0 and l[sup] > pivot:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[left], l[sup] = l[sup], l[left]

    # if printSwitch.dumpOperations:
    #    print("- "*left + str(l[left:right + 1]) + " -"*(len(l) - right - 1))

    return sup

# For debugging info
oldstate = ""
def condOutput(whoami, msg):
    global oldstate
    if oldstate != whoami:
        print("\t" + whoami)
        oldstate = whoami
    print(msg)

if __name__ == '__main__':
    basel = [5, 34, 26, 1, 4, 2, 17, 50, 41]
    k = 5
    l = list(basel)
    print(l)
    #print(trivialSelect(l,k))
    #print(sortSelect(l, k))
    #print(heapSelect(l, k))
    print(quickSelectRand(l, k))
    #print(quickSelectDet(l, k, 3))

    
