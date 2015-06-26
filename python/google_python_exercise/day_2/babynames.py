#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

#author : Saurabh Patel
#contact : skpatel@syr.edu or saurabh.ce1590@gmail.com

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_year(filedata):
	"""
	Given a filedata as string , function will search year from it using regex search function.
	"""
	regex = r"Popularity\sin\s(\d\d\d\d)"
	year = re.search(regex, filedata)
	return re.search(r'\d+', year.group()).group()

def extract_babynames(filedata):
	"""
	Given a filedata as string , function will find all names from provided string using regex findall function.
	"""
	regex = r"<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>"
	nameswithrank = re.findall(regex, filedata)
	return nameswithrank

def extract_names(filename,summary):
	"""
	Given a file name for baby.html, builds and dictionary starting with the name string
	followed by the name-rank string. As per summary flag either print them or write in file name.
	"""
	fileobject = open(filename, "rb")
	filedata = fileobject.read()
	# read year from input file data
	year = extract_year(filedata)
	# read male and female baby names
	names={}
	for pair in extract_babynames(filedata) :
		(rank,male_name,female_name) = pair
		names[male_name] = rank
		names[female_name] = rank
	if(summary):
		write_babynames(filename,names,year)
	else :
		print_babynames(names,year)
	
def print_babynames(babynames, year):
	"""
	print babynames as expected.
	"""
	print year
	for key in sorted(babynames) :
		print key+ " " + str(babynames[key])
	
def write_babynames(filename,babynames,year):
	"""
	write babynames in <filename>.summary file.
	"""
	targetfile = open(filename+".summary","w")
	targetfile.write(year)
	targetfile.write("\n")
	for key in sorted(babynames) :
		targetfile.write(key)
		targetfile.write(" ")
		targetfile.write(str(babynames[key]))
		targetfile.write("\n")

def main():
	# This command-line parsing code is provided.
	# Make a list of command line arguments, omitting the [0] element
	# which is the script itself.
	args = sys.argv[1:]

	if not args:
		print 'usage: [--summaryfile] file [file ...]'
		sys.exit(1)

	# Notice the summary flag and remove it from args if it is present.
	summary = False
	if args[0] == '--summaryfile':
		summary = True
		del args[0]

	# For each filename, get the names, then either print the text output
	# or write it to a summary file as per summaryfile option.
	for filename in args:
		extract_names(filename,summary)
	
if __name__ == '__main__':
  main()
