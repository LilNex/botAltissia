from asyncio.windows_events import NULL
from pydoc import text
from random import randint
from re import X
from sqlite3 import Timestamp
import sys
from typing import Any
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import *
from typing import List
import time
from selenium.common.exceptions import *
from classes import *
# browser  = webdriver.Chrome(ChromeDriverManager().install())
browser = webdriver.Chrome(executable_path='chromedriver.exe')
# browser = webdriver.Firefox(executable_path='geckodriver.exe')


# System.setProperty("webdriver.gecko.driver",Path_of_Firefox_Driver"); // Setting system properties of FirefoxDriver
# driver = webdriver.Firefox()()
# 


# ============= Setting =============
# 
email =''
password =''


emailXpath = '//*[@id="app-main-content"]/altissia-lc-reset-password-container/div/main/altissia-user-login/altissia-connection-form/form/div/altissia-input-label[1]/div/input'
passXpath ='//*[@id="app-main-content"]/altissia-lc-reset-password-container/div/main/altissia-user-login/altissia-connection-form/form/div/altissia-input-label[2]/div/div/input'

# l = []
l:List[Theme] = list()

# element =  browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-lc-reset-password-container/div/main/altissia-user-login/altissia-connection-form/form/div/altissia-main-button/button')
# element.click()

browser.find_elements_by_class_name('lesson-card-container')
# l.count

def getListeTheme():
    if browser.current_url.__contains__('learning-path'):
        listeTheme = browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-app-container/div/main/altissia-lc-learning-path/div/section/div/ol')
        listeTheme.find_elements_by_tag_name('li')[0].find_element_by_tag_name('h2').text
        l.clear()
        # browser
        # browser.find_element_by_class_name
        # browser.find_element_by_class_name
        for elem in listeTheme.find_elements_by_tag_name('li'):
            try:
                s = elem.find_element_by_tag_name('h2').text
                theme = Theme(s,elem)
                toggleTheme(elem)
                # theme = grabCards(theme)

                l.append(theme)
                print(theme.listCards[0].name)
            except:
                time.sleep(0)
        # getCountExCards(l[3])
        print(l)
    else:
        browser.get("https://app.ofppt-langues.ma/platform/#/learning-path?interfaceLg=fr_FR")
        time.sleep(2)
        getListeTheme()




def toggleTheme(elem):
    elem.find_element_by_tag_name('button').click()

def grabCards(e:Theme):
    # for e in l:
    toggleTheme(e.childs)
    e.listCards.clear()

    li = e.childs.find_elements_by_tag_name('li')
    for z in li:
        z:WebElement
        n = z.find_element_by_class_name('lesson-title').text
        c = z.find_element_by_tag_name('altissia-lesson-card')
        card = cardTheme(n,c)
        e.listCards.append(card)
        print(card.name)
    return e

def clickThemeCard(i : int):
    _l = browser.find_elements_by_css_selector('.mission-item')
    if i <= len(_l):
        while True:
            try:
                _l[i].click()
            except ElementClickInterceptedException:
                i=i+1
                continue
            break
            
        
        return True


def doExercice():
    btn = browser.find_element_by_css_selector('.footer-button-bar-btn')
    if len(browser.find_elements_by_css_selector('.exercise-activity-container')) > 0:
        progress = browser.find_element_by_css_selector('.progress-bar-numbers').text
        max = int()
        if len(progress) == 6 :
            max = int(progress[4]+progress[5])+1
        else:
            max = int(progress[4])+1

        i = int(progress[0])
        for x in range(i-1,max):
            if isIncorrect():
                btn.click()

            btn.click()
            q = question(X)
            addAnswer(q)
            q.reponses
            listAnswer.append(q)
        print('fin boucle')
        # btn.click()
        time.sleep(3)

        browser.find_element_by_css_selector('.btn-primary-ghost').click()
        time.sleep(0.5)

        btn = browser.find_element_by_css_selector('.footer-button-bar-btn')
        try:
            choiceList = browser.find_element_by_css_selector('.multiple-choice-buttons-list').find_elements_by_css_selector('button.multiple-choice-btn')
        except NoSuchElementException:
            choiceList=[]

        if len(choiceList) > 0:
            # for x in browser.find_element_by_css_selector('.multiple-choice-buttons-list').find_elements_by_css_selector('button.multiple-choice-btn'):
            for x in range(i-1,max-1):
                # x:WebElement
                for y in range(0,len(listAnswer[x].reponses)):
                    _l = browser.find_element_by_css_selector('.multiple-choice-buttons-list').find_elements_by_css_selector('button.multiple-choice-btn')
                    i=0
                    for r in _l :
                        r:WebElement
                        i=i+1
                        if(str.__contains__(r.text,listAnswer[x].reponses[y])):
                            print('reponse '+str(i))
                            r.click()
                            if y >= len(listAnswer[x].reponses)-1:
                                btn.click()
                                btn.click()
                                break            
            # print('r')
            time.sleep(0.5)
            while True:
                try:
                    browser.find_element_by_css_selector('button.btn-primary').click()
                    break
                except NoSuchElementException:
                    continue

            time.sleep(1)


        else:
            for x in range(i,max):
                try:
                    browser.find_element_by_tag_name('input').send_keys(listAnswer[x-1].reponses[0])
                except:
                    break
                btn.click()
                btn.click()

            print('fin boucle')
            time.sleep(0.5)
            while True:
                try:
                    browser.find_element_by_css_selector('button.btn-primary').click()
                    break
                except:
                    time.sleep(0.3)
                    try:
                        browser.find_element_by_css_selector('button.footer-button-bar-btn').click()
                    except:
                        browser.find_element_by_css_selector('button.btn-primary').click()


                    continue
            
            time.sleep(2)
        

def getCurrentCards():
    return browser.find_elements_by_css_selector('.lesson-card-container')

def getListLessonCards():
    return browser.find_elements_by_class_name('lesson-card-container')

def getListExCards():
    return browser.find_elements_by_class_name('activity-overview-card')

def getExCard():
    browser.find_element(By.CSS_SELECTOR,"p")
listAnswer = []

def getCountThemes():
    return len(browser.find_elements_by_css_selector('.mission-item'))

        
def addAnswer(q:question):
    if len(browser.find_elements_by_css_selector('span.input-answer.input-answer-is-correct')) > 0:
        for x in browser.find_elements_by_css_selector('span.input-answer.input-answer-is-correct'):
            answer = x.text
            q.reponses.append(answer)


        # listAnswer.append(answer)
        return True

    elif len(browser.find_elements_by_css_selector('.corrected-answer-is-correct'))> 0 and isIncorrect():
        answer = browser.find_element_by_css_selector('.corrected-answer-is-correct').text
        q.reponses.append(answer)

        return True


    elif len(browser.find_elements_by_css_selector('.input-answer')) > 0 or isIncorrect():
        answer = browser.find_element_by_css_selector('.multiple-choice-result-item-is-correct').text
        # listAnswer.append(answer)
        q.reponses.append(answer)

        return True
        
        
def isIncorrect():
    if len(browser.find_elements_by_css_selector('.correction-result-label-is-incorrect')) > 0:
        return True
    else:
        return False





    
    # # browser
    # for elem in listeTheme.find_elements_by_tag_name('li'):
    #     try:
    #         s = elem.find_element_by_tag_name('h2').text
    #         theme = Theme(s,elem)
    #         l.append(theme)
    #         print(theme.name)
    #     except:
    #         time.sleep(0)
    # print(l)
    # elem.



# =============================
# Open the Website
# browser.get('https://www.instagram.com/')

# print('nav to insta\n')
# click on Log in with Facebook



print('nav to altissia\n')

browser.get('https://app.ofppt-langues.ma/platform/#/login/');
time.sleep(1)

# browser.find_element_by_css_selector('#app-main-content > altissia-lc-reset-password-container > div > altissia-navigation-header > header > altissia-nav-bar > nav > div > ul > li:nth-child(2) > altissia-language-droplist > div > button').click
browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-lc-reset-password-container/div/altissia-navigation-header/header/altissia-nav-bar/nav/div/ul/li[2]/altissia-language-droplist/div/button').click()
time.sleep(1)
# browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-lc-reset-password-container/div/altissia-navigation-header/header/altissia-nav-bar/nav/div/ul/li[2]/altissia-language-droplist/div/ul/li[2]/button').click()
browser.find_element_by_css_selector('#app-main-content > altissia-lc-reset-password-container > div > altissia-navigation-header > header > altissia-nav-bar > nav > div > ul > li:nth-child(2) > altissia-language-droplist > div > ul > li:nth-child(2) > button').click()
# browser.find_element_by_css_selector('#app-main-content > altissia-lc-reset-password-container > div > altissia-navigation-header > header > altissia-nav-bar > nav > div > ul > li:nth-child(2) > altissia-language-droplist > div > button').click()
# time.sleep(1)


browser.find_element_by_xpath(emailXpath).send_keys(email)
if password == '':
    password = input('password : ')
browser.find_element_by_xpath(passXpath).send_keys(password)
print('logging in ...')
# time.sleep(1.5)
# browser.

browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-lc-reset-password-container/div/main/altissia-user-login/altissia-connection-form/form/div/altissia-main-button').click()
time.sleep(1.5)
getListeTheme()


i= randint(0,12)

for j in range(0,getCountThemes()):
    # toggleTheme(l[j].childs)
    clickThemeCard(j)
    time.sleep(1.5)
    listC = getListLessonCards()
    # l[7].listCards[1].click()

    for iC in range(0,len(getListLessonCards())):
        time.sleep(1.5)

        getListLessonCards()[iC].click()
        time.sleep(0.5)
        exDispo = False

        for i in range(0,len(getListExCards())):

            c:WebElement
            while True:
                try:
                    c = getListExCards()[i]
                    break
                except IndexError:
                    browser.get('https://app.ofppt-langues.ma/platform/#/learning-path')


            if  (str.__contains__(c.text,"Vocabulaire") or str.__contains__(c.text,"Score : 100")  or str.__contains__(c.text,"Vidéo"))  == False:
                if(str.__contains__(c.text,"Exercice")):
                    exDispo = True
                    c.click()

                    time.sleep(1.5)
                    doExercice()
                    time.sleep(0.3)


                    continue

            if i == len(getListExCards()):break
            # else:
            #     continue
            # if str.__contains__(c.text,"pratique") or str.__contains__(c.text,"Vidéo") == False:
                
            #     if (str.__contains__(c.text,"Vocabulaire") or str.__contains__(c.text,"Score : 100")  or str.__contains__(c.text,"Vidéo"))  == False:
                    
                        # c.click()
                        # break


        time.sleep(1.5)
        
        browser.find_element_by_css_selector('img.logo-image').click()
        time.sleep(0.5)

            # break


            # break


    

    



time.sleep(1.5)


print('fin prog')
