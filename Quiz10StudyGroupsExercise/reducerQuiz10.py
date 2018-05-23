# Replace this with your reducer code
import sys

oldKey = None
dict = {}
list = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    thisKey, thisAuthor = data_mapped

    if oldKey and oldKey != thisKey:
        dict[oldKey] = list
        list = []
        oldKey = thisKey
        
    
    oldKey = thisKey
    list.append(thisAuthor)

if oldKey != None:
    dict[oldKey] = list
    
for key in dict:
    print key, "\t", dict[key]
    
            