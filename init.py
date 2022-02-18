from asyncio.windows_events import NULL
import sys
from typing import Any
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.by import By
import time
from classes import *
# browser  = webdriver.Chrome(ChromeDriverManager().install())
browser = webdriver.Chrome(executable_path='chromedriver.exe')
# ======= Setting =============
# 

email = "chaiq.ismail@ofppt-edu.ma"
password='Lilnex123@'

emailXpath = '//*[@id="app-main-content"]/altissia-lc-reset-password-container/div/main/altissia-user-login/altissia-connection-form/form/div/altissia-input-label[1]/div/input'
passXpath ='//*[@id="app-main-content"]/altissia-lc-reset-password-container/div/main/altissia-user-login/altissia-connection-form/form/div/altissia-input-label[2]/div/div/input'

l = []
# l.count

def getListeTheme():
    if browser.current_url.__contains__('https://app.ofppt-langues.ma/platform/#/learning-path?interfaceLg=fr_FR'):
        listeTheme = browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-app-container/div/main/altissia-lc-learning-path/div/section/div/ol')
        listeTheme.find_elements_by_tag_name('li')[0].find_element_by_tag_name('h2').text
        l.clear()
        # browser
        browser.find_element_by_class_name
        # browser.find_element_by_class_name
        for elem in listeTheme.find_elements_by_tag_name('li'):
            try:
                s = elem.find_element_by_tag_name('h2').text
                theme = Theme(s,elem)
                l.append(theme)
                print(theme.name)
                grabCards()
            except:
                time.sleep(0)
        getCountExCards(l[3])
        print(l)
    else:
        browser.get("https://app.ofppt-langues.ma/platform/#/learning-path?interfaceLg=fr_FR")
        time.sleep(2)
        getListeTheme()

def getCountExCards(theme:Theme):
    return len(theme.childs.find_elements_by_class_name('mission-lesson-item'))


def toggleTheme(elem):
    elem.find_element_by_tag_name('svg').click()

def grabCards():
    for e in l:
        toggleTheme(e.childs)
        li = e.childs.find_elements_by_tag_name('li')
        for z in li:
            n = z.find_element_by_class_name('lesson-title').text
            c = z.find_element_by_class_name('lesson-title')
            card = cardTheme(n,c)
            e.listCards.append(card)
            print(card.name)

def getExCard():
    browser.find_element(By.CSS_SELECTOR,"p")

        
        
        





    
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
time.sleep(1.5)
# browser.

browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-lc-reset-password-container/div/main/altissia-user-login/altissia-connection-form/form/div/altissia-main-button').click()
# browser.find_element_by_css_selector('#app-main-content > altissia-lc-reset-password-container > div > main > altissia-user-login > altissia-connection-form > form > div > altissia-main-button > button').click()
# browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-lc-reset-password-container/div/main/altissia-user-login/altissia-connection-form/form/div/altissia-main-button/button').click()
time.sleep(1.5)
# browser.find_element_by_class_name('KPnG0').click();
# browser.find_element_by_css_selector('#app-main-content > altissia-lc-reset-password-container > div > main > altissia-user-login > altissia-connection-form > form > div > altissia-main-button > button').click()
getListeTheme()

l[3].listCards[1].click()

time.sleep(1.5)
# input('test')

browser.find_element_by_xpath('//*[@id="FAIRE_UNE_PRESENTATION_2"]/button').click()
time.sleep(0.5)


browser.find_element_by_xpath('//*[@id="FAIRE_UNE_PRESENTATION_2"]/ul/li[1]/altissia-lesson-card/a').click()
time.sleep(1.5)

# for x in range(0,25):
#     print('boucle x : '+str(x))

#     print('Choosing the video')
#     browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-app-container/div/main/altissia-app-lesson-menu/div/ul/li[1]/altissia-activity-overview-card/a').click()
#     time.sleep(1)

#     print('playing the video')
#     browser.find_element_by_css_selector('#app-main-content > altissia-app-container > div > main > altissia-app-video-activity > div > div > altissia-media-player > div > div > plyr > div > div.plyr__controls > div.plyr__controls__item.plyr__volume > button').click()
#     browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-app-container/div/main/altissia-app-video-activity/div/div/altissia-media-player/div/div/plyr/div/button').click()
#     time.sleep(0.5)
#     # browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-app-container/div/main/altissia-app-video-activity/div/div/altissia-media-player/div/div/plyr/div/div[1]/div[3]/button').click()
#     # browser.find_element_by_css_selector('//*[@id="app-main-content"]/altissia-app-container/div/main/altissia-app-video-activity/div/div/altissia-media-player/div/div/plyr/div/div[2]/div').se
    
#     for i in range(0,4):
#         time.sleep(50)
#         print('sleep n°'+str(i))

#     # =============================
#     print('click btn Continu')

#     browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-app-container/div/main/altissia-activity-result/div/div/altissia-main-button/button').click()
#     time.sleep(5)
#     print('fin tour boucle')


print('fin prog')



# Filling in the Facebook Credentials
# browser.find_elements_by_xpath('//*[@id="i0116"]')[0].send_keys(email)