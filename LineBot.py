# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 12:14:45 2022

@author: Phoenix
"""

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('pVqQlOC3JfOAV2UBlCZjqXzDRl6MRIut3oB22UOVwcz7/a4Wz9oc0nk+hlzLs7RzDvS9QYKCWPCSSSNJpyQR39Js7hbTUNENGnfNEys69OJIdhb9+pJQMTy3QfnwZIGBRTqQJ0FbzCiPbA2TZMar0AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9015e07eb414aee62893df4fca5e6f16')

def ptt(link):
    import urllib.request as req 
    import bs4
    end=''
    url=link
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("span",class_="push-tag")[-26:]
    comment=root.find_all("span",class_="f3 push-content")[-26:]
    user=root.find_all("span",class_="push-userid")[-26:]
    time=root.find_all("span",class_="push-ipdatetime")[-26:]
    for c,f,e,g in zip(titles,user,comment,time):
        dd=str(c.string) + str(f.string) + str(e.string) + str(g.string)
        end += dd
        end +="\n"

    return end

def holox(holo):
    
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.keys import Keys
    from bs4 import BeautifulSoup
    result=""
    

    driver = webdriver.Chrome(r'C:\Users\Phoenix\Desktop\chromedriver.exe')
    

    # options.add_argument("--headless")

    driver.get('https://www.google.com.tw/imghp?hl=zh-TW&authuser=0&ogbl')

    driver.find_element_by_name('q').send_keys(holo)
    driver.find_element_by_class_name('Tg7LZd').click()

    sleep(2)
    for i in range(0,5):
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        sleep(1)

    the_d=driver.find_elements_by_class_name('bRMDJf,islir')

    for d in the_d:
        
        d.click()
        
        sleep(5)
        # image=driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img')
        soup = BeautifulSoup(driver.page_source,'html.parser')
        website=soup.select('#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id > div > a > img[src^=http]')
        for i in website:
            website=i.get('src')
        result=('{}'.format(website))
        sleep(3)
        driver.quit()
        return result
        
    
    # url = soup.select('div.title a[href^="/bbs"]')
    
def lotto(y,m):
    import requests
    from bs4 import BeautifulSoup
    import re
    result=""

    my_header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}

    r = requests.get('https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx',headers = my_header)
    if r.status_code == 200:
        # print(r.text)
        soup = BeautifulSoup(r.text,'html.parser')
        __VIEWSTATE = soup.find('input',id="__VIEWSTATE").get('value')
        __VIEWSTATEGENERATOR = soup.find('input',id="__VIEWSTATEGENERATOR").get('value')
        __EVENTVALIDATION = soup.find('input',id="__EVENTVALIDATION").get('value')

    for year in range(103,int(y)+1):
        for month in range(1,int(m)+1):      
            my_data={'__VIEWSTATE': __VIEWSTATE,
                      '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
                      '__EVENTVALIDATION': __EVENTVALIDATION,
        
                      'forma': '請選擇遊戲',
                      'SuperLotto638Control_history1$txtNO': '',
                      'SuperLotto638Control_history1$chk': 'radYM',
                      'SuperLotto638Control_history1$dropYear': year,
                      'SuperLotto638Control_history1$dropMonth': month,
                      'SuperLotto638Control_history1$btnSubmit': '查詢',
            }
        
            r = requests.post('https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx',headers = my_header, data = my_data)
            if r.status_code == 200:
                # print(r.text)
                soup = BeautifulSoup(r.text,'html.parser')
                
                nums = soup.find_all('span', id = re.compile('SuperLotto638Control_history1_dlQuery_SNo\d_\d'))
                
                result += str(year) +" " + str(month) + "\n"
                for index,num in enumerate(nums):
                    # print(num.text,end=' ')
                    result += num.text +" "
                    if (index+1) % 7 ==0:
                        # print()
                        result +="\n"
                # print("--------------------------------------")
                result += "---------------------------------------" + "\n"
    return result  
def eat():
    result = '生魚片'
    return result 
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #print("Handle: reply_token: " + event.reply_token + ", message: " + event.message.text)
    # content = "{}: {}".format('Hello World', event.message.text)
    p=("{}".format(event.message.text))
    c=p.upper()
    if  "SEARCH"in c :
        holo=event.message.text.split("@")[1]
        content =holox(holo)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(original_content_url=content,
                             preview_image_url=content))
        
    elif 'HTTP' in c :
        link=event.message.text
        content = ptt(link)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
    elif '吃啥' in c :
        content =eat()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ.get('PORT', 5000))
    #9*9    
    #     a=event.message.text.split("@")[0]
    #     b=event.message.text.split("@")[1]
        
    #     content =""
    #     for r in range(1,int(a)+1):
    #         for c in range(1,int(b)+1):
    #             # print(str(r)+"*"+str(c)+"="+str(r*c))
    #             content += str(r) + "*" + str(c) +"=" +str(r*c)+" "
    #         content += "\n"
    
    #lotto
    # year=int(event.message.text.split("@")[0])
    # month=int(event.message.text.split("@")[1])    
    # content=lotto(year,month)