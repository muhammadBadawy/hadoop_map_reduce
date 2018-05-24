import sys
 
# input comes from STDIN (standard input)
for line in sys.stdin:
   # try: 
	
	user_id="-1"
	prod_id = "-"
	location = "-"

        line = line.strip() 
        splits = line.split("\t")
         
        if len(splits) == 5:
		 
		user_id = splits[2]            
		prod_id = splits[1]
            
		

        else:
           
		user_id = splits[0]
	    
		location = splits[3]
                  
	print '%s\t%s\t%s' % (user_id,prod_id,location)         

