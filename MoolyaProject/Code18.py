#use of break statement

i=0
while i<=10:
    break
    print(i)
    i=i+1
    print("out of the loop")
#print("out of the loop")

#use of continue

i=0
while i<=10:
    print(i)
    continue#it will not go in line 17 so only 0 will be printed infinite times
    i=i+1
    #print("out of the loop")
print("out of the loop")