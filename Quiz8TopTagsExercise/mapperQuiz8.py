# Replace this with your mapper code
# This will actually not get graded at the moment, because it's
# pretty hard to properly simulate Hadoop cluster in our system :-)
# This will serve as a storage for your code.
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    if line[0] == "id":
        continue
    id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string,
    last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
    
    tags = tagnames.strip().split(" ")
        for i in tags:
            print "0".format(i)

# The challenge part            
#    if node_type == "question":
#        tags = tagnames.strip().split(" ")
#        for i in tags:
#            print "0".format(i)
