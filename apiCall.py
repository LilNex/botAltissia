
from email.headerregistry import HeaderRegistry
from email.quoprimime import body_check
from lib2to3.pgen2 import driver
from time import time
from urllib import request
from gevent import idle
# from seleniumrequests import Chrome
import json
import requests
from typing import List
import time
from termcolor import colored
from classes import *



email = ''
password = ''


    # def addLesson(lessonID:str):
        # global lessons
        # lessons.append(lessonID)
        # lessons?





device_uuid = "3956abc8-97bd-d955-6f42-43a941c9df14"
userLevel = ''

authUrl = "https://app.ofppt-langues.ma/gw//api/authenticate"
learningPathUrl = 'https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/user-learning-paths/language/fr_FR'

def getActUrl(idLesson):
    return 'https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/lessons/'+idLesson+'/activities'

def bypassSecu(idLesson,idActivity):
    return 'https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/lessons/'+idLesson+'/activities/'+idActivity+'?translationLg=fr_FR'


# webdriver = Chrome()
altissiaToken = ''
header ={
        'Content-Type':'application/json',
        'x-device-uuid':device_uuid
        }


learningPaths=''
learnPathID = ''
missions = []

def formatActivitiesUrl(id):
    global learnPathID
    return 'https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/lessons/'+id+'?learningPathExternalId='+learnPathID




# resp =  webdriver.get("https://www.google.com")
# print(resp)


def login():   
    global altissiaToken
    global userLevel
    body = {
        "username": email,
        "password": password,
        "deviceName": "Chrome",
        "deviceExplicitName": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "platform": "DESKTOP"
    }  
    # webdriver.get('https://www.google.com')
    # res = webdriver.request('POST',authUrl,data=body)
    res = requests.post(authUrl, json=body,headers=header)
    jsonResponse = json.loads(str(res.content.decode('utf-8')))
    try:
        altissiaToken = res.headers['Authorization'].replace('Bearer ' ,'')
        header['x-altissia-token'] = altissiaToken
        print(colored('Token grabbed : ','green') + altissiaToken)
        reponse = requests.get('https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/user-learning-paths/language/fr_FR',headers=header)
        jsRep = json.loads(str(reponse.content.decode('utf-8')))
        for i in jsRep['levels']:
            if i['done'] < i['total']:
                userLevel = i['level']
                break
        # switch={
        #     'C1':'A1_MINUS',
        #     'A1':'A1',
        #     'A2':'A2',
        #     'B1':'B1',
        #     'B2':'B2',
        # }
        # userLevel = switch[jsRep['level']]
    except:
        try:
            print(bcolors.WARNING+'Login error message : '+bcolors.ENDC+ jsonResponse['message'])
        except e:
            print(bcolors.FAIL+'ERROR :'+bcolors.ENDC + str(e))


def getActivites(id):
    activities = []
    client=requests
    res = client.get(formatActivitiesUrl(id),headers=header)
    responseJson = json.loads(res.content.decode('utf-8'))
    for o in responseJson['activities']:
        activities.append(o['externalId'])

    return activities





def getLearningPaths():
    global learnPathID
    # global missionsID
    global missions
    client=requests
    res = client.get(learningPathUrl,headers=header)
    responseJson = json.loads(res.content.decode('utf-8'))
    learnPathID = responseJson['externalId']
    for item in responseJson['missions']:
        if item['level'] == userLevel and item['validated'] == False:
            m = mission(item['externalId'])
            for i in item['lessons']:
                l = lesson(i['externalId'])
                l.activities = getActivites(l.id)
                m.lessons.append(l)
                print('Lesson added : '+i['title'])
            # missionsID.append(item['externalId'])
            missions.append(m)
            # lessons
    # print(responseJson)

    # r = client.get(formatActivitiesUrl(missions[0].lessons[0]),headers=header)
    # print(r)
    # print(r)
    

# def 

def sendSuccess(m:mission):
    count = 0
    # m.lessons[0].activities[0].e
    client = requests
    for l in m.lessons:
        xxx = client.get(formatActivitiesUrl(l.id),headers=header)
        for a in l.activities:
            xxx = client.get(bypassSecu(l.id,a),headers=header)

            response = client.put(getActUrl(l.id),headers=header,
                json={
                    "externalActivityId": a,
                    "externalLessonId": l.id,
                    "externalMissionId": m.id,
                    "externalLearningPathId": learnPathID,
                    "score":100,
                    "status": "SUCCESS"
                }
            )
            count += 1
            if response.status_code == 200:
                print('SUCCESS id : ' + a)
            else:
                print (json.loads(response.content.decode('utf-8')))

            # print (json.loads(response.content.decode('utf-8')))
            # time.sleep(1)
        # if count > 5:
        #     break



login()
# print(res.request)
getLearningPaths()

print('Sending PUT success')

for m in missions:
    sendSuccess(m)
# json.decoder(res.request)
# print(webdriver.requests_session)

# print(res)


