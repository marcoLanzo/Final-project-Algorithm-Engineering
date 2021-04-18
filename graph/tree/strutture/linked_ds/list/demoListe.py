from LinkedList import ListaCollegata
from DoubleLinkedList import ListaDoppiamenteCollegata
from time import time

# Se eseguiamo direttamente questo modulo, ossia NON lo importiamo in un altro.
if __name__ == "__main__":
    print("Comparison among different list implementations")
    
    #Pushing elements
    print("\tAdding elements in front of the considered list")
    print("ListaCollegata")
    l = ListaCollegata()
    start = time()
    for i in range (50000):
        l.addAsFirst(i)
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", l.getFirst())
    print("Last:", l.getLast())

    print("ListaDoppiamenteCollegata")
    dl = ListaDoppiamenteCollegata()
    start = time()
    for i in range (50000):
        dl.addAsFirst(i)
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", dl.getFirst())
    print("Last:", dl.getLast())

    print("ArrayList (Python built-in implementation)")
    pl = []    
    start = time()
    for i in range (50000):
        pl.insert(0, i)
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", pl[0])
    print("Last:", pl[-1])
    
    #Appending elements
    print("\tAppending elements to the considered list")
    print("ListaCollegata")
    start = time()
    for i in range (50000, 100000):
        l.addAsLast(i)
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", l.getFirst())
    print("Last:", l.getLast())

    print("ListaDoppiamenteCollegata")
    start = time()
    for i in range (50000, 100000):
        dl.addAsLast(i)
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", dl.getFirst())
    print("Last:", dl.getLast())

    print("ArrayList (Python built-in implementation)")
    start = time()
    for i in range (50000, 100000):
        pl.append(i)
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", pl[0])
    print("Last:", pl[-1])
    
    #Removing first elements
    print("\tRemoving the first elements from the considered list")
    print("ListaCollegata")
    start = time()
    for i in range (50000):
        l.popFirst()
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", l.getFirst())
    print("Last:", l.getLast())

    print("ListaDoppiamenteCollegata")
    start = time()
    for i in range (50000):
        dl.popFirst()
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", dl.getFirst())
    print("Last:", dl.getLast())

    print("ArrayList (Python built-in implementation)")
    start = time()
    for i in range (50000):
        pl.pop(0)
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", pl[0])
    print("Last:", pl[-1])
    
    #Removing last elements
    print("\tRemoving the last elements from the considered list")
    print("ListaCollegata does not expose such kind of a method!")

    print("ListaDoppiamenteCollegata")
    start = time()
    for i in range (50000):
        dl.popLast()
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", dl.getFirst())
    print("Last:", dl.getLast())

    print("ArrayList (Python built-in implementation)")
    start = time()
    for i in range (50000):
        pl.pop()
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    if len(pl) == 0:
        print("Empty list!")
    else:
        print("First:", pl[0])
        print ("Last:", pl[-1])
