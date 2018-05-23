# Replace this with your mapper code
# This will actually not get graded at the moment, because it's
# pretty hard to properly simulate Hadoop cluster in our system :-)
# Thi will serve as a storage for your code.
#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    if line[0] == "id":
        continue
    id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string,
    last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
    
    if node_type == "question":
        identifier = id
    if node_type == "answer":
        identifier = parent_id
        
    print "{0}\t{1}\t{2}".format(identifier, node_type, len(body))
