#! /usr/bin/python2.7
from bs4 import BeautifulSoup
import lxml
import urllib2
matchList=[]
matchLink=[]
url="http://www.cricbuzz.com/cricket-match/live-scores"
i=1
print('\n')
print "****************"
print("* Live Matches *")
print "****************"
print('\n')
fine=urllib2.urlopen(url)
soup=BeautifulSoup(fine,'html.parser')

#To display the matches

for line in soup.find_all('a', {'class':"text-hvr-underline text-bold"}):
	link=line.get('href')
	name=line.get('title')
	matchLink.append(link)
	matchList.append(name)
	print i,".",name
	i=i+1

#menu

while(1):
	print '\n'
	print "Enter option(-1 to exit): ",
	n=input()
	if n==-1:
		break;
	print '\n'
	print "\t","\033[4m",matchList[n-1],"\033[0m"
	print '\n'
	url1="http://www.cricbuzz.com"+matchLink[n-1]
	fine1=urllib2.urlopen(url1)
	soup1=BeautifulSoup(fine1,'lxml')
	flag=0
	#for line in soup1.findAll('div', ""):
	for line in soup1.findAll('div', "cb-col cb-col-67 cb-scrs-wrp"):
		flag=1
		print "\t",line.text
		for result in soup1.findAll('div', "cb-text-complete"):
			print "\t",result.text
	if flag==1:
		continue
	if flag==0:
		for line2 in soup1.findAll('div', "cb-col cb-col-100 cb-font-18 cb-toss-sts cb-text-abandon"):
			flag=1
			print "\t",line2.text
		if flag==1:
			continue
	print "\t","Match is Yet to Begin"
