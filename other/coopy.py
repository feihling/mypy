import copy  
  
al = [[1],[2],[3]]  
bl = copy.copy(al)  
cl = copy.deepcopy(al)
dl = al
  
print "before=>"  
print al  
print bl  
print cl  
print dl  
  
al[0][0] = 0  
al[1] = None  
  
print "after=>"  
print al  
print bl  
print cl  
print dl