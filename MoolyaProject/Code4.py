str="Dollysha"
print((str[::-1]))#slicing for reversing

str1='''
Since Selenium is a collection 
of different tools, it also had different developers.
 Below are the key persons who made
 notable contributions to the Selenium Project
'''
print((str1[::-1]))#to reverse the whole string
print((str1[::1]))#slicing of strings
print(str1[1])
print(str1[-1])#count from right
print(str1[-2])
print(str1[0:8])#count till 8-1=7, 8 is given by incrementing one to it values will be 0,1,2,3,4,5,6,7
print(str1[7:15])#it will print the value of 7,8,9,10,11,12,13,14
print(str1[0:])#print the whole string
print(str1[-8:-1])#last word from right from left to right
print(str1[-8:])#for printing the last word
print(str1[-8:-2])
print(str1.find("Project"))
print(str1.find("Since"))


