#!/usr/bin/python3
## Updated by Robert Orr, 2016-Mar-14 - apparently the IA api changed!
## Further updated by Gabriel Bauer - added shebang and moved to Py3

## Original code from :
## Robin Camille Davis
## March 24, 2014
## downloads all items in a given Internet Archive collection
## !! will probably crash after 10 or so items !! feel free to edit the script to make it better for bigger collections
## See http://programminghistorian.org/lessons/data-mining-the-internet-archive for more detailed info
import os
import time
import sys
import internetarchive as ia
from internetarchive.session import ArchiveSession
from internetarchive import get_item
from internetarchive import download

search = ia.search_items('collection:%s' % sys.argv[1])

num = 0

for result in search: #for all items in a collection
	num = num + 1 #item count
	itemid = result['identifier']
	print('Downloading: #' + str(num) + '\t' + itemid)
	try:
		#download(itemid) 
		print(itemid)
		print('\t\t Download success.')
	except Exception as e:
		print("Error Occurred downloading () = {}".format(itemid, e))
	print('Pausing for 40 minutes')
	time.sleep(2400)# IA restricts the number of things you can download. Be nice to 
			# their servers -- limit how much you download, too. For me, this
			# time restriction is still not polite enough, and my connection gets
			# cut off all the dang time.
    
    
    
