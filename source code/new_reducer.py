import sys
 
# input comes from STDIN (standard input)
last = "-"
count = 0
location = "non"
for line in sys.stdin:
    try: 
	
        line = line.strip() 
        splits = line.split("\t")   
	
        if last == "-":   
		last = splits[0]
		location = splits[1]
		count=count+1
		continue

	elif last == splits[0]:
		if splits[1] == location:
			continue
		elif splits[1] != location:
			location = splits[1]
			count=count+1

	else:
		print "%s\t%s" % (last,count)
		last = splits[0]
		location = splits[1]
		count =1
		continue
	     
#	print "%s\t%s\t%s" % (splits[0],splits[1],splits[2])
	   
    except: #errors are going to make your job fail which you may or may not want
        pass
