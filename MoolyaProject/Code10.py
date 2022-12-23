#set
se={10,20,30,40,50,50,'A'}
print(se)#unordered pattern
print(len(se))
print(20 in se)
se.add(100)#inserting in random order not as list
print(se)
se.pop()#it removes in an ordered way
print(se)
se.pop()
print(se)
se.remove(30)
print(se)
m={23,98,65,40}
n={90,80,70,60,40,20}
z=m.union(n)
print(z)
t=m.symmetric_difference(n)#it will remove the common element
print(t)
l={20,47}#subset of t
print(l.issubset(t))
y={}
print(l.issubset(t))
print(t.issuperset(l))
l.discard(47)#it can take only one argument
print(l)