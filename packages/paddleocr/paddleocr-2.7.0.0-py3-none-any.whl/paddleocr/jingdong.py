from selenium import webdriver
import datetime
import time
from selenium.webdriver.common.by import By
# import win32com.client
import client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

times = '2023-07-10 22:13:00'

browser = webdriver.Chrome()
browser.get("https://jd.com")
time.sleep(2)

browser.find_element(By.LINK_TEXT,"你好，请登录").click()
print("请扫码")
time.sleep(8)

browser.get("https://cart.jd.com/cart_index")
time.sleep(5)

while True:
    # if browser.find_element_by_class_name("jdcheckbox"):
    #     browser.find_element_by_class_name("jdcheckbox").click()
    #     break
    if browser.find_element(By.CLASS_NAME, "jdcheckbox"):
        browser.find_element(By.CLASS_NAME, "jdcheckbox").click()
        break


while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now)
    time.sleep(1)  # Reduce CPU usage
    if now >= times:
        while True:
            try:
                if browser.find_element(By.LINK_TEXT,"去结算"):
                    print("here")
                    message = "主人，结算提交成功，我已帮你抢到商品，请及时支付订单"
                    print(message)
                    speaker.Speak(message)
                    break
            except:
                pass

            while True:
                try:
                    if browser.find_element(By.LINK_TEXT,"提交订单"):
                        browser.find_element(By.LINK_TEXT,"提交订单").click()
                        message = "抢购成功，请尽快付款"
                        print(message)
                        speaker.Speak(message)
                        break
                except:
                    break
            time.sleep(0.01)

