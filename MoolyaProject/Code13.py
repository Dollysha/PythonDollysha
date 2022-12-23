#dictionary
a={"URL1":"google.com",
   "URL2":"demoqa.com",
   "URL3":"amazon.com"}#url1 is 'key' and google.com is 'value'
b={1:"Dollysha",2:"India",3:"USA"}
print(b[1])#integer value no quotes
print(a["URL2"])#strings will be in quotes
#print(b["India"])#we can not aceess key by passing value
#print(a["google.com"])#impossible
b[4]="China"
print(b)#all the elements of b set will be printed
#print(b[5])#can not access because fifth element is not there
print(b.get(1))#china will be printed
print(b.get(12))#none will be printed as no 12th element is there
print(b.keys())#will tell number of keys present in b
print(b.items())#print with keys and values the values came will be in the form of tuple
print(b.values())#print all the values of set b
print(b.pop(1))#delete the first element
print(b)
#print(b.pop())#atleast one value should be passed
print(b.popitem())#it will delete the last item
print(b)
b.update({3:"France"})#for updating the new value instead of old
print(b)
b.update({2:"Autralia",5:"Singapore",6:"Italy"})#adding more values
print(b)
b.setdefault(7,"India")#refer python docs
print(b)
b.clear()
print(b)