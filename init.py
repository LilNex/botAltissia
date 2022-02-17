import sys
from selenium import webdriver
import time
# browser  = webdriver.Chrome(ChromeDriverManager().install())
browser = webdriver.Chrome(executable_path='chromedriver.exe')
# ======= Setting =============
# 

email = "chaiq.ismail@ofppt-edu.ma"


emailXpath = '//*[@id="app-main-content"]/altissia-lc-reset-password-container/div/main/altissia-user-login/altissia-connection-form/form/div/altissia-input-label[1]/div/input'
passXpath ='//*[@id="app-main-content"]/altissia-lc-reset-password-container/div/main/altissia-user-login/altissia-connection-form/form/div/altissia-input-label[2]/div/div/input'


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

time.sleep(1.5)
# input('test')

browser.find_element_by_xpath('//*[@id="FAIRE_UNE_PRESENTATION_2"]/button').click()
time.sleep(0.5)


browser.find_element_by_xpath('//*[@id="FAIRE_UNE_PRESENTATION_2"]/ul/li[1]/altissia-lesson-card/a').click()
time.sleep(1.5)

for x in range(0,10):
    print('Choosing the video')
    browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-app-container/div/main/altissia-app-lesson-menu/div/ul/li[1]/altissia-activity-overview-card/a').click()
    time.sleep(1)

    print('playing the video')
    browser.find_element_by_css_selector('#app-main-content > altissia-app-container > div > main > altissia-app-video-activity > div > div > altissia-media-player > div > div > plyr > div > div.plyr__controls > div.plyr__controls__item.plyr__volume > button').click()
    browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-app-container/div/main/altissia-app-video-activity/div/div/altissia-media-player/div/div/plyr/div/button').click()
    time.sleep(0.5)
    # browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-app-container/div/main/altissia-app-video-activity/div/div/altissia-media-player/div/div/plyr/div/div[1]/div[3]/button').click()
    # browser.find_element_by_css_selector('//*[@id="app-main-content"]/altissia-app-container/div/main/altissia-app-video-activity/div/div/altissia-media-player/div/div/plyr/div/div[2]/div').se
    
    for i in range(0,4):
        time.sleep(50)
        print('sleep n°'+str(i))

    # =============================
    input('click btn Continu')

    browser.find_element_by_xpath('//*[@id="app-main-content"]/altissia-app-container/div/main/altissia-activity-result/div/div/altissia-main-button/button').click()
    time.sleep(5)
    input('fin tour boucle')


input('fin prog')



# Filling in the Facebook Credentials
# browser.find_elements_by_xpath('//*[@id="i0116"]')[0].send_keys(email)