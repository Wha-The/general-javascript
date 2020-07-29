def attach(level):
  for i,v in level.values():
      def replaceddef(*a,**k):
          print(i,v,a,k)
          v(*a**k)
      level[i]=replaceddef
    
dump = {}
def abc(d,e,f): print(d,e,f)
dump["abc"] = abc

attach(dump)
dump.["abc"]("1",2,3)
