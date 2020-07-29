class Event():
  def __init__(self,dispatchevent):
    self.event = dispatchevent
  def __call__(self,*a,**k):
    print(a,k,self.dispatchevent)
    return self.dispatchevent(a,k)

def attach(level):
  for i,v in level.values():
      level[i]=Event(v)
    
dump = {}
def abc(d,e,f): print(d,e,f)
dump["abc"] = abc

attach(dump)
dump["abc"]("1",2,3)
