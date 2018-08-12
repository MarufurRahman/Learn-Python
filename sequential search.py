# Sequential search of a list
# programmed by Marufur Rahman

mylist = [10,11,3,4,55,12,23,14,16]
n = len(mylist)
print('List lenth is ', n)
for i in range(n):
    print (mylist[i], end=" ")
search = int(input("\nPlease enter a number to search for: "))
print (search)
found = False
for i in range(n):
    if mylist[i] == search:
        found = True
        index = i
print()
if found == True:
    print (str(search) + " found at index " + str(index))
else:
    print (str(search) + " not found")
