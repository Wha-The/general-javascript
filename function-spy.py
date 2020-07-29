class Event():
  def __init__(self,dispatchevent):
    self.event = dispatchevent
  def __call__(self,*a,**k):
    print(a,k,self.event)
    return self.dispatchevent(self.event,a,k)
  def dispatchevent(self,evt,a,k):
    return evt(*a,**k)

def attach(level):
  for i,v in level.items():
      level[i]=Event(v)
    
dump = {}
def abc(d,e,f): print(d,e,f)
dump["abc"] = abc

attach(dump)
dump["abc"]("1",2,3)
