NOREPEATS = [
"NOREPEATS",
"Event",
"attach"
]

class Event():
  def __init__(self,dispatchevent,dispatcheventname):
    self.event = dispatchevent
    self.eventname = dispatcheventname
  def __call__(self,*a,**k):
    print "Function *"+self.eventname+"* called, arguments: ("+','.join([str(i) for i in a])+") , kwargs: ",k
    return self.dispatchevent(self.event,a,k)
  def dispatchevent(self,evt,a,k):
    return evt(*a,**k)

def attach(level):
  for i,v in level.items():
      if callable(v) and i not in NOREPEATS:
        level[i]=Event(v,i)
  return level
  
def abc(d):return d+5 
attach(globals())

print(abc(5))
