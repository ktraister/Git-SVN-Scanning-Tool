#! python3

import requests
import sys
import os
import datetime 

outfile = "svn_scan.txt"

try:
    base = str(sys.argv[1])

    if sys.argv[2] == "--auth":
        user = sys.argv[3]
        passwd = sys.argv[4]
        search_string = sys.argv[5]
        auth_flag = 1
    elif sys.argv[2] != "--auth":
        search_string = sys.argv[2]
        auth_flag = 0

except:
    print("Usage: myscanner.py {user} {passwd} {string_to_search}")
    quit()


#I'd like a function to call for each dir to make looping easy
def dircrawl(EXT, LIST):

    newpage = "%s%s" % (base, EXT)

    if auth_flag == 1:
        r = requests.get(newpage, auth=(user, passwd))
    elif auth_flag == 0:
        r = requests.get(newpage)

    page = str(r.content)

    mylist = page.split('href')

    for entry in mylist:
        line = entry 
        line = line.split('>')
        line = line[0].replace('=', '')
        if line.startswith("b'"):
            continue
        if '../' in line:
            continue
        if '%20' in line:
            line = line.replace('%20', ' ')
        line = line.replace('"', '')
        if line.endswith('/'):
            line = "%s%s" % (EXT, line)
            print("Adding %s to list" % line)
            LIST.append(line)
        #here's the part where we compile a list of files to check
        elif not line.endswith('/'):
            line = "%s%s" % (EXT, line)
            target_files.append(line)
        else:
            print("We failed to match the line! Bad Ju-Ju...")

    #to keep this going, lets return a list of dirs found by our crawl
    #we're doing this by appending directly to the list we're told to

def filekek(FILE, SEARCH_STRING):
    outfile = "svn_scan.txt"
    print("Scanning file %s for search string" % FILE)
    #this is where we'll actually check the files
    url = "%s%s" % (base, FILE)

    #checking for auth flag to see if we need to authenticate with host
    if auth_flag == 1:
        r = requests.get(url, auth=(user, passwd))
    elif auth_flag == 0:
        r = requests.get(url)
    r = str(r.content)
    #print("Response: ", r)
    #print()
    #print("Search string: ", SEARCH_STRING)
    if SEARCH_STRING in r:
        print("FOUND STRING %s IN FILE %s" % (SEARCH_STRING, FILE))
        if os.path.isfile('svn_scan.txt') and fileck_flag == 0:
            outfile = "%s%s" % ("svn_scan.txt", str(datetime.datetime.now()))
            fileck_flag = 1
        with open(outfile, "a") as scanfile:
            scanfile.write(FILE)



#list for files we're going to check 
target_files = []

#lists to hold directories we're going to check for files 
#each one corresponds to a level of directory we're going to check 
#i.e. {https://repo-url/one/two/three/...}
one_deep = []
two_deep = []
three_deep = []
four_deep = []
five_deep = []
six_deep = []
seven_deep = []
eight_deep = []
nine_deep = []
ten_deep = []
eleven_deep = []
twelve_deep = []
thirteen_deep = []
fourteen_deep = []
fifteen_deep = []
#extra list to catch dirs more than 15 deep
#but seriously, 15 dirs deep?!?!?!
lifeboat_list = []

#lets kick this crawl off
dircrawl('', one_deep)

#for each dir we find, scan that dir for dirs.....
#to keep mem usage down, lets clear the lists when we're done

for line in one_deep:
    dircrawl(line, two_deep)
one_deep = []

for line in two_deep:
    dircrawl(line, three_deep)
two_deep = []

for line in three_deep:
    dircrawl(line, four_deep)
three_deep = []

for line in four_deep:
    dircrawl(line, five_deep)
four_deep = [] 

for line in five_deep:
    dircrawl(line, six_deep)
five_deep = []

for line in six_deep:
    dircrawl(line, seven_deep)
six_deep = []

for line in seven_deep:
    dircrawl(line, eight_deep)
seven_deep = []

for line in eight_deep:
    dircrawl(line, nine_deep)
eight_deep = []

for line in nine_deep:
    dircrawl(line, ten_deep)
nine_deep = []

for line in ten_deep:
    dircrawl(line, eleven_deep)
ten_deep = []

for line in eleven_deep:
    dircrawl(line, twelve_deep)
eleven_deep = []

for line in twelve_deep:
    dircrawl(line, thirteen_deep)
twelve_deep = []

for line in thirteen_deep:
    dircrawl(line, fourteen_deep)
thirteen_deep = []

for line in fourteen_deep:
    dircrawl(line, fifteen_deep)
fourteen_deep = []

for line in fifteen_deep:
    dircrawl(line, lifeboat_list) 
fifteen_deep = []

#warn the user that they overran our ability to scan the repo
for line in lifeboat_list:
    print("********************************************")
    print("WARNING: unable to scan dir ", line)
    print("********************************************")

#when we're finally ready to search our compiled list of files....
for line in target_files:
    filekek(line, search_string)

