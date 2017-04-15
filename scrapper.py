import requests
from bs4 import BeautifulSoup
import urllib
import os

link_ends = ["24501","24500","24499","24498","24497","24496","24495","24494","24493","24492","24491","24490","24489","24488"]

base_url = "https://tspace.library.utoronto.ca/"

for le in link_ends :
	page_link = "https://tspace.library.utoronto.ca/handle/1807/" + le
	print "Downloading files from " + page_link	
	r = requests.get(page_link)
	soup = BeautifulSoup(r.content, "html.parser")

	# print soup.prettify
	# print soup.find_all("a",{"target":"_blank"})

	links = soup.find_all("a",{"target":"_blank"})

	for link in links :
		download_link = base_url + link.get("href")
		file_name = download_link.split("/")[-1]
		folder_name = file_name.split("_")[-1].split(".")[0]

		print "Downloading " +file_name+" to folder " + folder_name + "....",

		try :
			urllib.urlretrieve (download_link, folder_name + "/" + file_name)
		except IOError:
			os.mkdir(folder_name)
			urllib.urlretrieve (download_link, folder_name + "/" + file_name)
		
		print "Downloaded !"
		


# print r.content
