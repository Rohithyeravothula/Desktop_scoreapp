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

def getscore(link):
    r = requests.get(link)
    soup_second = BeautifulSoup(r.text)
    data = []
    for link in soup_second.find_all('tr'):
        data.append(link.td.string)
    data2=[]
    l=len(data)
    for i in range(0,l):
        try:
            data2.append(str(data[i]))
        except:
            continue
    final_data=[]
    l=len(data2)
    for i in range(0,l):
        if data2[i]!="None":
            final_data.append(data2[i])
    final_data=list(set(final_data))

    score = "NULL"
    score_list=["AUS","IND","NZ","WI","PAK","ZIM","SRI","ENG","BAN","RSA"]
    for string in final_data:
        try:
            if string[0:3] in score_list and len(string)>8:
                score = string[4:9]
        except:
            continue
    return score

def formatscore(score):
    l=len(score)
    for i in range(0,l):
        if score[i]=='/':
            break
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
    link_length=len(link_info)
    for i in range(0,link_length):
        link_info[i].append(getscore(link_info[i][0]))
    return link_info


