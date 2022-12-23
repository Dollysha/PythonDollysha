#formatting the string
a="my name is dollysha"
b="how are you"
print("welcome",a,b)#for concatenation
print("welcome",b,a)
print("welcome {} {}".format(a,b))#concatenation
print("welcome {1} {0}".format(a,b))#reversing like in place of a we have b and b in place of a
#d=a+b
#print(d)
#line 11 we have declred a variable about and question and pass value a and b
print("welcome {about} {question}".format(about=a,question=b))
