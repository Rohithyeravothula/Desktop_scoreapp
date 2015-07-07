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
    return link_info

print getdata()

