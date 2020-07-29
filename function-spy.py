def attach(level):
  for i,v in level.values():
      def replaceddef(*a,**k):
          print(i,v,a,k)
          v(*a**k)
      level[i]=replaceddef
