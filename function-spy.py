NOREPEATS = [
"NOREPEATS",
"Event",
"attach",
"lastabc"
]
class Event(object):
  def __init__(self,dispatchevent,dispatcheventname):
    self.event = dispatchevent
    self.eventname = dispatcheventname
  def __call__(self,*a,**k):
    print "Function *"+self.eventname+"* called, arguments: ("+','.join([str(i) for i in a])+") , kwargs: ",k
    return self.__dispatchevent(self.event,a,k)
  def __dispatchevent(self,evt,a,k):
    return evt(*a,**k)
  def __cmp__(self,other,operator):
    return eval("self.event %s other"%operator)
  def __repr__(self):
    return str(self.event)
  def __str__(self):return repr(self)
  def __int__(self): return int(self)

def attach(*levels):
  for level in levels:
    for i,v in level.items():
        if callable(v) and i not in NOREPEATS:
          level[i]=Event(v,i)
  

def abc(d): return d+5 
lastabc = abc

attach(globals())

print lastabc==abc
