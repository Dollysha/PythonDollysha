#list methods
li1=[10,10,"abc","abc"]

li1.append(60)#appending the element
print(li1)
li1.insert(2,"Hello")
print(li1)
li1.insert(10,"Hello")#it will insert at last even if 10 th position is not there
print(li1)
li1.remove("Hello")
print(li1)#it will only remove the first hello instead of second
li1.remove("Hello")
print(li1)
li2=[54,98,"ABC",0.56,"Selenium",70]
li2.extend(li1)
print(li2)
li3=[5,7,9,2]
print(li3)
li3.sort()
print(li3)
print(sum(li3))
print(li3.pop())#it will delete  the last element
print(li3)
del li3[0]
print(li3)
li3.sort()
