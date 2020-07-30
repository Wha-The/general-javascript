NOREPEATS = [
"NOREPEATS",
"Event",
"attach"
]

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
      if callable(i) and i not in NOREPEATS:
         level[i]=Event(v)
  
def abc(d):print(d+5)  
  
attach(globals())

abc(5)
