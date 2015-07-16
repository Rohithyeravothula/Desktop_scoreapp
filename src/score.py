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
    for link in soup_second.find_all('td'):
        try:
            data.append(link.tr.string)
        except:
            continue
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
    score_list=["AUS","IND","NZ","WI","PAK","ZIM","SRI","ENG","BAN","RSA"]
    score_card = ""
    for item in final_data:
        try:
            if item[0:3] in score_list:
                score_card = item
        except:
            continue
    score = []
    score_split = score_card.split(" ")
    score.append(score_split[0])
    score_score = score_split[1].split("/")
    score.append(score_score[0])
    score.append(score_score[1])
    score.append(score_split[2][1:len(score_split[2])])
    return str(score[1]+"/"+score[2])



def getmatchstatus(link):
    r = requests.get('http://cricbuzz.com/')
    soup = BeautifulSoup(r.text)
    status="NIL"
    for data in soup.find_all("td", class_="status"):
        status_report = str(data.string)
        if status_report != "None":
            status = status_report
    if status=="NIL":
        return ["0"]  # match alive
    else:
        return status


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
        try:
            link_info[i].append(getscore(link_info[i][0]))
        except:
            link_info[i].append("None")

    updated_link=[]
    for i in range(0,link_length):
        if link_info[i][2]!="None":
            updated_link.append(link_info[i])
    return updated_link


#print getscore("http://www.cricbuzz.com/live-cricket-scores/13752/eng-vs-aus-2nd-test-the-ashes-2015")
#print getdata()