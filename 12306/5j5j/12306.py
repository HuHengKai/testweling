import requests
import os
import base64
import re
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
driver.find_element_by_xpath('//*[@class="btn-search tb-bg"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@class="login-blocks sns-login-links"]/a[1]').click()
url=driver.find_element_by_xpath('//*[@class="inp verify"]/a/img')
>>> url=url.get_attribute("src")
>>> url
'https://login.sina.com.cn/cgi/pin.php?r=97398991&s=0&p=tc-b6b008d624581101c4ac8b1028c365e1dad6'
>>> def request_download():
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

>>> a=request_download()
>>> a
'u3b5z'
>>> url
os.makedirs('./image/', exist_ok=True)
IMAGE_URL = "https://login.sina.com.cn/cgi/pin.php?r=38567005&s=0&p=tc-3c5d26c1c71af46a8ef1be9dd474b26814d2"
def request_download():
    import requests
    r = requests.get(IMAGE_URL)
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
print(a)
