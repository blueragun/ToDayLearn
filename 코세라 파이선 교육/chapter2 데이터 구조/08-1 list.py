fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()
    words = line.split()
    for a in words :
    	if not (a in lst) : 
         lst.append(a)
         lst.sort()  
            
print(lst)