#list
li1=[6,9,'a',4,3,7]
li2=[100,200,300,600,700,400,900,300]
s=zip(li1,li2)#map or pairing the two list together with zip method
print(list(s))#output will be in form of tuples, inside list tuple are there,here square bracket are there
print(s)#it return a zip object

#tuples
ti1=("Apple","banana","orange","guava")
ti2=(1,2,3,4,5)
tu=zip(ti1,ti2)
print(tuple(tu))#inside tuple tuple are there,here round bracket are there
print(tu)
