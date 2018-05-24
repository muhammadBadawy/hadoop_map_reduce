#!/usr/bin/env python

 
import sys
 
# input comes from STDIN (standard input)
for line in sys.stdin:
   # try: 
	
        line = line.strip() 
        splits = line.split("\t")
         
                  
	print '%s\t%s\t%s' % (splits[1],splits[2],splits[0])         


