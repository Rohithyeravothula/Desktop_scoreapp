import requests
from bs4 import BeautifulSoup



def getinfo(link):
    link_length = len(link)
    info = ["null", "null"]
    for i in range(0, link_length - 4):
        if link[i:i + 4] == "-vs-":
            j = i
            while link[j] != '/':
                j = j - 1
            info[0] = link[j+1:i]
            j = i + 4
            while link[j] != '-':
                j = j + 1

            info[1] = link[i + 4:j]
    return info

def removeduplicates(link):
    link_length = len(link)
    new_link=[]
    add_link=[]
    for i in range(0,link_length):
        if link[i][1] not in add_link:
            new_link.append(link[i])
            add_link.append(link[i][1])
    return new_link


def getinternationaldata(link):
    link_length =len(link)
    link_int=[]
    team_int = ["ind","pak","sl","eng","wi","ban","zim","nz","aus","rsa"]
    for i in range(0,link_length):
        if link[i][1][0] in team_int and link[i][1][1] in team_int:
            link_int.append(link[i])
    return link_int


def getdata():
    r = requests.get('http://cricbuzz.com/')
    soup = BeautifulSoup(r.text)
    all_link = []
    for link in soup.find_all('a'):
        all_link.append(link.get('href'))
    live_link = []
    for link in all_link:
        if "live-cricket-scores" in link:
            live_link.append(link)
    link_info = []
    for link in live_link:
        link_info.append([link, getinfo(link)])
    link_info=removeduplicates(link_info)
    link_info=getinternationaldata(link_info)
    return link_info

#info = getdata()
#l=len(info)
#for i in range(0,l):
#    print info[i][0]
