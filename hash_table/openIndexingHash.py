import hashFunctions

class DictOpenIndexingHash:
    """ Implementa una tabella hash ad indirizzamento aperto.

    Supporta le classiche operazioni di insert, search and delete key.
    """


    def __init__(self, size, DoubleHashFunction):
        self.canc = object() #just a marker...
        self.table = size * [None]    #each entry of the table is a pair [key,value]
        self.size = size
        self.hashFunction = DoubleHashFunction
        
    def insert(self, key, value):
        #scorro gli indici
        for i in range(0, self.size):
            ind = self.hashFunction.hash(key, i, self.size)
            if self.table[ind] == None or self.table[ind] == self.canc: #add it to the first None/Canc value
                self.table[ind] = [key, value]
                break
    
    def delete(self, key):
        for i in range(0, self.size):
            ind = self.hashFunction.hash(key, i, self.size)
            if self.table[ind] == None:
                return
            if self.table[ind] == self.canc:
                continue
            if self.table[ind][0] == key: #remember 0 is the key
                self.table[ind] = self.canc
                break

    def search (self, key):
        for i in range(0, self.size):
            ind = self.hashFunction.hash(key, i, self.size)
            if self.table[ind] == None:
                return None
            if self.table[ind] == self.canc:
                continue
            if self.table[ind][0] == key:
                return self.table[ind][1]
        return None 

if __name__ == "__main__":
    size = 13;

    hd = hashFunctions.doubleHash_linearScan()
    diz = DictOpenIndexingHash(size,hd)

    k=1
    v=2
    print ("insert({},{})".format(k,v))
    diz.insert(k, v)
    print (diz.table)
    
    k=14
    v=28
    print ("insert({},{})".format(k,v))
    diz.insert(k, v)
    print( diz.table)
    
    k=27
    v=54
    print( "insert({},{})".format(k,v))
    diz.insert(k, v)
    print( diz.table)
    
    k=2
    v=4
    print( "insert({},{})".format(k,v))
    diz.insert(k, v)
    print( diz.table)
    
    k=3
    v=6
    print( "insert({},{})".format(k,v))
    diz.insert(k, v)
    print( diz.table)
    
    k=4
    v=8
    print( "insert({},{})".format(k,v))
    diz.insert(k, v)
    print( diz.table)
    
    k=5
    v=10
    print( "insert({},{})".format(k,v))
    diz.insert(k, v)
    print( diz.table)
    
    k=6
    v=12
    print( "insert({},{})".format(k,v))
    diz.insert(k, v)
    print( diz.table)
    
    print( "search(1)=" + str(diz.search(1)))
    print( "search(3)=" + str(diz.search(3)))
    print( "search(13)=" + str(diz.search(13)))
    print( "search(4)=" + str(diz.search(4)))
    
    print( "delete(27)")
    diz.delete(27)
    print( diz.table)
    
    print( "delete(4)")
    diz.delete(4)
    print( diz.table)
    
    print( "delete(3)")
    diz.delete(3)
    print( diz.table)
    
    print( "delete(13)")
    diz.delete(13)
    print( diz.table)
    
    print( "delete(27)")
    diz.delete(27)
    print( diz.table)
        
    print( "search(4)=" + str(diz.search(4)))

    k=17
    v=34
    print( "insert({},{})".format(k,v))
    diz.insert(k, v)
    print( diz.table)
