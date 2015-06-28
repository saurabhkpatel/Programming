#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Saurabh Patel
# skpatel@syr.edu


import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
	"""Returns a list of the puzzle urls from the given log file,
	extracting the hostname from the filename itself.
	Screens out duplicate urls and returns the urls sorted into
	increasing order."""
	basefilename=os.path.basename(filename)
	fileobject = open(filename,"r+")
	regex = r"GET\s(\/edu\/\S+)"
	imageurls = re.findall(regex, fileobject.read())
	underbar_index = filename.index('_')
	hostname  = filename[underbar_index+1:]
	url_dict = {}
	for url in imageurls :
		localimageurl = 'http://' + hostname + url
		url_dict[localimageurl] = 1;
  	return url_dict

def download_images(img_urls, dest_dir):
	"""Given the urls already in the correct order, downloads
	each image into the given directory.
	Gives the images local filenames img0, img1, and so on.
	Creates an index.html in the directory
	with an img tag to show each local image file.
	Creates the directory if necessary.
	"""
	# +++your code here+++
	try:
		os.makedirs(dest_dir)
	except OSError, e:
		print e
        pass
	# download all images and store in html page.
	fileobject = open( os.path.join(dest_dir, "index" + "." + "html"),"w")
	fileobject.write("<html><body>\n")
	i = 0
	for key in sorted(img_urls.keys()):
		imagefile_name = 'img%d'%i
		urllib.urlretrieve(key, os.path.join(dest_dir, imagefile_name))
		print "Retrieving... " , key
		fileobject.write('<img src="'+imagefile_name+'">')
		i = i+1
	fileobject.write("\n</body></html>")
		

def main():
	args = sys.argv[1:]

	if not args:
		print 'usage: [--todir dir] logfile '
		sys.exit(1)

	todir = ''
	if args[0] == '--todir':
		todir = args[1]
		del args[0:2]

	img_urls = read_urls(args[0])
	if todir:
		download_images(img_urls, todir)
	else:
		print '\n'.join(img_urls)

if __name__ == '__main__':
	main()
