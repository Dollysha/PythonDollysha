a=2
print(a ** 3)#exponential **
#precedence of operator
print(5+8-2)
print(5-8+2)
#string manipulation
a="Dollysha"
print(len(a))
print(a[4])
b=7832
print(str(b))
z=str(b)#string are immutable can not be changed , String is a object
print(type(z))
#operations in strings
#find()
p="Hello"
print(p.find("l"))
print(p.find("z"))
print(p.upper())
print(p)
print(p.lower())
print(p.count("l"))#how many times a particular character has occured
print(p.islower())
print(p.isupper())
str1=" Lucknow "
print(str1)
print(str1.strip())#removing space
print(str1.lstrip())
#Replace()
print(str1.replace("o","a"))
str2="visakhapatnam"
print(str2.replace("a","B"),str2.upper())#Combining two operations

str3=" ABC "
print(str3)
print(str3.lstrip())#removing space from left side
print(str3.rstrip())#removing space from right side

str4="Selenium is a free (open-source) automated testing framework used to validate web applications across different browsers"
print(str4.replace(" ",""))#to remove all space
#split operation(dividing)
#print(str4.split())#dividing on basis of space
print(str4.split("a"))#dividing on basis of a
print(str4.split("free"))#dividing on basis of free

str5="dollysha\" rastogi"#escape character
print(str5)
#multiline string
z=''' #'3' single quotes or double quotes can be used for multline string
hello
dollysha
lucknow
'''
print(z)
print("dollysha" in z)