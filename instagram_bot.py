# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import time
import random

browser = webdriver.Chrome(executable_path='C:/Users/user/Desktop/chromedriver_win32//chromedriver.exe')
loginURL = "https://www.instagram.com/"
tagSearchURL = "https://www.instagram.com/explore/tags/{}/?hl=ja"
tagNameList1 = [ 'クリームソーダ', 'メロンソーダ', '純喫茶コレクション', 'プリン']
tagNameList2 = [ 'アート', 'illustration', 'イラスト', '色鉛筆'] 
WaitTime = [3,4,6,8]

loginPath = '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a'
usernamePath = '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/div[1]/input'
passwordPath = '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/div[1]/input'
notNowPath = '//*[@id="react-root"]/div/div[2]/a[2]'
mediaSelector = '//*[@id="react-root"]/section/main/article/div[2]/div/div[*]/div[*]/a/div/div[2]'
likeXpath = '/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span'
nextPageSelector = 'a.HBoOv.coreSpriteRightPaginationArrow'
timeXpath = '/html/body/div[3]/div[2]/div/article/div[2]/div[2]/a/time'
username1 = "terubon_illust"
password1 = "aceamnos3062"
username2 = "aiteru_illust"
password2 = "aceamnos1220"

mediaList = []
likedCounter = 0
if __name__ == '__main__':
    browser.get(loginURL)
    time.sleep(5)
    browser.find_element_by_xpath(loginPath).click()
    time.sleep(5)
    usernameField = browser.find_element_by_xpath(usernamePath)
    usernameField.send_keys(username2)
    passwordField = browser.find_element_by_xpath(passwordPath)
    passwordField.send_keys(password2)
    passwordField.send_keys(Keys.RETURN)
    time.sleep(5)
    encodedTag = urllib.parse.quote(tagNameList2[2])
    encodedURL = tagSearchURL.format(encodedTag)
    browser.get(encodedURL)
    time.sleep(3)
    browser.implicitly_wait(5)
    mediaList = browser.find_elements_by_xpath(mediaSelector)
    mediaCounter = len(mediaList)
    print("Found {} media".format(mediaCounter))
    for media in mediaList:
        media.click()
        while True:
            try:
                #if(timekeep.text == "1日前"):
                    #break
                iine = browser.find_element_by_xpath(likeXpath) #いいねオス
                if(iine.get_attribute("aria-label") == "いいね！"):
                    if(random.choice(WaitTime)%2 == 0):
                        time.sleep(random.choice(WaitTime))
                        timekeep = browser.find_element_by_xpath(timeXpath)
                        print(timekeep.text)
                        likedCounter += 1 #次の写真へ
                        print("liked {} of {}".format(likedCounter,mediaCounter)) #写真○○枚目
                        
                        browser.find_element_by_xpath(likeXpath).click() #いいねオス
                browser.implicitly_wait(10)
                browser.find_element_by_css_selector(nextPageSelector).click() #次のページへ
                if(likedCounter > 200):
                    break
            except:
                break
                        
    print("You liked {} media".format(likedCounter)) 
#browser.quit()
