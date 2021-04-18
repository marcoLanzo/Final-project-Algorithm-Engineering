from __init__ import printSwitch

class HeapMin:
    """
    Usiamo un heap (struttura rafforzata) che parte dall'elemento 0. I figli del nodo in posizione i si trovano in posizione
    2*i+1 e 2*i+2. Il padre di un nodo in posizione i>0 si trova in posizione floor((i-1)/2), ovvero
    (i-1)/2 con la divisione intera
    Ordiniamo per chiavi crescenti, perche' ci fa per heapselect
    E' piu' efficiente non modificare la reale dimensione della lista, anche a fronte di cancellazioni.
    Ci serve allora l'attributo length per conoscere la reale dimensione della lista a runtime.
    """
    
    def __init__(self, l):
        """It takes a list as the parameter
        """
        self.heap = l
        self.length = len(l)
    
    def isEmpty(self):
        return self.length == 0
    
    def minSon(self, fatherId):
        """Returns -1 if father is a leaf
        """
        if fatherId * 2 + 1 > (self.length - 1):
            return -1
        
        #just one son
        if fatherId * 2 + 2 > (self.length - 1):
            return fatherId * 2 + 1
        
        if self.heap[fatherId * 2 + 1] < self.heap[fatherId * 2 + 2]:
            return fatherId * 2 + 1
        else:
            return fatherId * 2 + 2
    
    
    def findMin(self):
        if self.length == 0:
            return None
        else:
            return self.heap[0]
    
    def moveDown(self, fatherId):
        """Ripristina l'ordinamento spostando verso il basso il nodo di indice fatherId
        """
        son = self.minSon(fatherId)
        while son != -1 and self.heap[son] < self.heap[fatherId]:
            self.heap[son], self.heap[fatherId] = self.heap[fatherId], self.heap[son]
            fatherId = son
            son = self.minSon(fatherId)
     
    def deleteMin(self):
        """O(log n)
        """
        if self.length == 0:
            return None
        #scambia primo ed ultimo elemento
        minValue = self.heap[0]
        self.heap[0], self.heap[self.length - 1] = self.heap[self.length - 1], self.heap[0]
        self.length -= 1
        self.moveDown(0) # ripristina l'ordinamento con muoviBasso() sul primo elelemto
        return minValue

    def heapify(self):
        """O(log n)
        """
        self.recursiveHeapify(0, self.length - 1)
    
    def recursiveHeapify(self, first, last):
        if printSwitch.dumpOperations:
            print("recursiveHeapify({},{})".format(first, last))
            
        if first > last:
            return
        self.recursiveHeapify(2 * first + 1, last) #rende un heap il sottoalbero sinistro di first
        self.recursiveHeapify(2 * first + 2, last) #rende un heap il sottoalbero destro di first
        
        if printSwitch.dumpOperations:
            print("moveDown({})".format(first))
            
        self.moveDown(first) #ripristina l'ordinamento spostando first verso il basso
        
        if printSwitch.dumpOperations:
            print(self.heap)
