# Replace this with your reducer code
#!/usr/bin/env python

import sys

oldKey = None
oldLen = 0
number_answer = 0
length_answer = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        continue
    thisKey, thisNodeType, thisLen = data_mapped

    if oldKey and oldKey != thisKey:
        if number_answer == 0:
            ave_answer = 0
        else:
            ave_answer = float(lengthj_answer / number_answer)
        print "{0}\t{1}\t{2}".format(oldKey, oldLen, ave_answer)
        number_answer = 0
        length_answer = 0
        oldKey = thisKey
        oldLen = thisLen
        
    if thisNodeType == "answer":
        number_answer += 1
        length_answer += float(thisLen)
    
    oldKey = thisKey
    oldLen = float(thisLen)

if oldKey != None:
    if number_answer == 0:
        ave_answer = 0
    else:
        ave_answer = float(lengthj_answer / number_answer)
    print "{0}\t{1}\t{2}".format(oldKey, oldLen, ave_answer)

            