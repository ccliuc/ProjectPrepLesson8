# Replace this with your reducer code
#!/usr/bin/env python

import sys

active_hours = [0] * 24
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    thisKey, thisTime = data_mapped

    if oldKey and oldKey != thisKey:
        most_active_hour_posts = max(active_hours)
        for hour, post_count in enumerate(active_hours):
            if post_count == most_active_hour_posts:
                print "{0}\t{1}".format(oldKey, hour)
                active_hours = [0] * 24

    active_hour = int(thisTime)
    active_hours[active_hour] += 1
    oldKey= thisKey

if oldKey != None:
    most_active_hour_posts = max(active_hours)
    for hour, post_count in enumerate(active_hours):
        if post_count == most_active_hour_posts:
            print "{0}\t{1}".format(oldKey, hour)
            
            