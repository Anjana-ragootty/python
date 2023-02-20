dic={'c':15,'d':20,'a':5,'b':10}
l=list(dic.items())
l.sort()
d=dict(l)
print("Ascendind is :",d)
l=list(dic.items())
l.sort(reverse=True)
d=dict(l)
print("Descending is :",d)