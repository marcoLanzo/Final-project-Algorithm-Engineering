
class Record:
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class ListaCollegata:
    def __init__(self):
        self.first=None
        self.last=None
        
    def isEmpty(self):
        return (self.first==None)
    
    def getFirst(self):
        if self.first==None:
            return None
        else:
            return self.first.elem

    def getLast(self):
        if self.last==None:
            return None
        else:
            return self.last.elem
        
    def addAsLast(self,elem):
        rec=Record(elem)
        if self.first==None:
            self.first=self.last=rec
        else:
            self.last.next=rec
            self.last=rec

    def addAsFirst(self,elem):
        rec=Record(elem)
        if self.first==None:
            self.first=self.last=rec
        else:
            rec.next=self.first
            self.first=rec
    
    def popFirst(self):
        if self.first==None:
            return None
        else:
            res=self.first.elem
            self.first=self.first.next
            if self.first==None:
                self.last=None #abbiamo svuotato la lista
            return res
              
    #popLast e deleteRecord non sarebbero efficienti, per ora!

    def getFirstRecord(self):
        if self.first==None:
            return None
        else:
            return self.first        

    def getLastRecord(self):
        if self.first==None:
            return None
        else:
            return self.last

    def stampa(self):
        if self.first==None:
            print("[]")
            return
        print("Elements in the collection (ordered):")
        s="["
        current=self.first
        while current!=None:
            if len(s)>1:
                s+=", "
            s+=str(current.elem)
            current=current.next
        s+="]"
        print(s)


# Se eseguiamo direttamente questo modulo, ossia NON lo importiamo in un altro.
if __name__=="__main__":
    l=ListaCollegata()
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
