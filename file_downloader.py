import sys
from tqdm import tqdm
import urllib
import os

i = 0
for link in tqdm(sys.argv[1:] ):
	# os.mkdir('file-from')
	temp = link.split('.')
	print "Downloading file " + temp[-2].split('/')[-1]+ '.' +temp[-1]
	urllib.urlretrieve(link, temp[-2].split('/')[-1]+ '.' +temp[-1])