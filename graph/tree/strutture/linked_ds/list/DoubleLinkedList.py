import LinkedList

class DoubleRecord(LinkedList.Record):
    def __init__(self,elem):
        LinkedList.Record.__init__(self,elem)
        self.prev=None

class ListaDoppiamenteCollegata(LinkedList.ListaCollegata):
    
    def addAsLast(self,elem):
        rec= DoubleRecord(elem)
        if self.first==None:
            self.first=self.last=rec
        else:
            rec.prev = self.last
            self.last.next = rec
            self.last = rec
    
    def addAsFirst(self,elem):
        rec=DoubleRecord(elem)
        if self.first==None:
            self.first=self.last=rec
        else:
            self.first.prev = rec
            rec.next = self.first
            self.first = rec
    
    def popFirst(self):
        if self.first==None:
            return None
        else:
            res = self.first.elem
            self.first = self.first.next
            if self.first!=None:
                self.first.prev = None #Il controllo serve a gestire il caso di lista vuota    
            else:
                self.last = None
            return res
    
    #Ora possiamo cancellare efficientemente anche l'ultimo.
    def popLast(self):
        if self.first==None:
            return None
        else:
            res = self.last.elem
            self.last = self.last.prev
            if self.last!=None:
                self.last.next = None
            else:
                self.first = None
            return res
    #Ora possiamo cancellare efficientemente anche un record generico.
    def deleteRecord(self,rec):
        if rec==None:
            return  #restituisce None!
        if rec.prev!=None:
            rec.prev.next = rec.next
        else:
            self.first = rec.next
        if rec.next!=None:
            rec.next.prev = rec.prev
        else:
            self.last = rec.prev


# Se eseguiamo direttamente questo modulo, ossia NON lo importiamo in un altro.
if __name__=="__main__":
    l= ListaDoppiamenteCollegata()
    l.stampa()
    
    print("addAsFirst(2)")
    l.addAsFirst(2)
    print("addAsFirst(3)")
    l.addAsFirst(3)
    print("addAsLast(4)")
    l.addAsLast(4)    
    l.stampa()
    
    print("getFirst()", l.getFirst())
    print("getLast()", l.getLast())
    l.stampa()
    print("popFirst()", l.popFirst())
    l.stampa()
    print("findFirst()=", l.getFirst())
    print("popFirst()", l.popFirst())
    print("popFirst()", l.popFirst())
    l.stampa()
    print("findLast()=", l.getLast())
    print

    print("rec1=insertFirst(2)")
    l.addAsFirst(2)
    rec1 = l.getFirstRecord()
    print("rec2=insertFirst(3)")
    l.addAsFirst(3)    
    rec2 = l.getFirstRecord()
    print("rec3=insertLast(4)")
    l.addAsLast(4)
    rec3 = l.getLastRecord()
    l.stampa();
    print("delete(rec1)")
    l.deleteRecord(rec1)
    l.stampa()
    print("delete(rec2)")
    l.deleteRecord(rec2)
    l.stampa()
    print("delete(rec3)")
    l.deleteRecord(rec3)
    l.stampa()
