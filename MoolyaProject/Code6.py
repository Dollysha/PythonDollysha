#lists
l=[10,20,40,"Abc",87,0.765,True]
print(l[0])
print(l[3])
print(l[5],l[6])
#print(l[7])#index error list index out of range
li1=[10,10,"abc","abc"]#list can accept duplicate values also
print(li1[3])
print(li1[-1])
print(li1[-3:-1])#for
print(li1[0:3:1])#for printing 10,10,abc go till 0,1,2 last 1 is for step
print(type(li1))#for the type
print(li1[1:1])#nothing will be there
print(li1[1:2:4])
#list methods
li1.append(60)#appending the element
print(li1)
li1.insert(2,"Hello")
print(li1)
li2=[54,98,"ABC",0.56,"Selenium",70]
li2.extend(li1)
print(li2)
li3=[5,7,9,2]
print(sum(li3))
print(li3.pop())
print(li3)
del li3[0]
print(li3)




