#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://pan.baidu.com/")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[6]/div/div[6]/div[2]/a").click()
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_4__userName']").send_keys(u"我只是小小的我")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_4__password']").send_keys("SUIBIAN")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_4__submit']").submit()
time.sleep(10)
driver.quit()


#作业：对某个网站自动注册账号
#     自动登录账号
#     自动发一个贴子
#     发完后自动截图一张
#     将截图发至自己的邮箱

