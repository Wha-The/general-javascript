def attach(level):
  for i,v in level.values():
      def replaceddef(*a,**k):
          print(i,v,a,k)
          v(*a**k)
      level[i]=replaceddef
    
cmd = {}
def abc(d,e,f): print(d,e,f)
cmd.abc = abc

attach(cmd)
cmd.abc("1",2,3)
