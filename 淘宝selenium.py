from selenium import webdriver
import time
import os
import base64
import re
url="https://www.taobao.com"
driver =webdriver.Chrome()
driver.get(url)
driver.find_element_by_name('q').send_keys('美食')
time.sleep(3)
driver.find_element_by_xpath('//*[@class="login-blocks sns-login-links"]/a[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="J_OtherLogin"]/a[1]').click()
time.sleep(3)
driver.find_element_by_name("username").send_keys("2810390731@qq.com")
time.sleep(1)
driver.find_element_by_name('password').send_keys("123456hkf")
time.sleep(1)
url=driver.find_element_by_xpath('//*[@class="inp verify"]/a/img')
url=url.get_attribute("src")
def request_download():
    import requests
    r = requests.get(url)
    with open('./image/img3.png', 'wb') as f:
        f.write(r.content)
    with open("./image/img3.png", "rb") as f:
        img = f.read()
    ret = requests.post('http://127.0.0.1:8820', data={"img": base64.b64encode(img)})
    str1 = ret.text
    str2 = str.split(str1, " ")[0]
    yzm = re.split("：", str2)[1]
    return yzm
a=request_download()
"""
#获取验证码ull
#import requests,os
#os.makedirs("./image/",exist_ok=True)
#r=requests.get(url)
#with open("./image/img2.png",'wb') as f:
#	f.write(r.content)
#with open("./image/img2.png","rb") as f:
#img=f.read()
#ret= requests.post('http://127.0.0.1:8820', data={"img": base64.b64encode(img)})
#ret.text()
#获取识别后得验证码'识别结果：qnpsu  耗时：47ms'
#import base64
#获取验证码图片
str1=ret.text
str2=str.split(str1," ")[0]
验证码=re.split("：",str2)[1]
driver.find_element_by_name('verifycode').send_keys("5z776")
driver.find_element_by_xpath('//*[@id="pl_login_logged"]/div/div[7]/div[1]/a').click()
"""
