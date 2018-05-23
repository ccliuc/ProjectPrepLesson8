# Replace this with your reducer code
import sys

oldKey = None
number_tag = 0
list = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        continue
    thisKey = data_mapped

    if oldKey and oldKey != thisKey:
        list.append([number_tag, oldKey])
        number_tag = 0
        oldKey = thisKey
        
    
    oldKey = thisKey
    number_tag += 1

if oldKey != None:
    list.append([number_tag, oldKey])
    
top_N = sorted(list, reverse=True)[0:10]
top_N = sorted(top_N, reverse=True)
for pair in top_N:
    print "{0}\t{1}".format(pair[1], pair[0])
    
            