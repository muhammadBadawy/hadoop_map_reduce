  import sys
  
# maps words to their counts
current_location=""
country_flag = False
 
# input comes from STDIN
for line in sys.stdin:
    # remove space
    line = line.strip()
     
    try:
        # parse the input we got from mapper
        user_id,prod_id,location = line.split('\t')
	if location != "-":
		current_location = location
		country_flag = True

	if location == "-" and country_flag:
		location = current_location
		print "%s\t%s\t%s" %(user_id,prod_id,location)

    except:
        pass
try:
    print '%s\t%s' % (foundKey,currentCount)
except:
    pass
