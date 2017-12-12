import time
from selenium import webdriver
driver=webdriver.Chrome()
#driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
driver.find_element_by_xpath('//*[@id="kw"]').send_keys("selenium")
print(driver.find_element_by_css_selector('html body div#wrapper div#head div.head_wrapper div.s_form div.s_form_wrapper.soutu-env-mac.soutu-env-index form#form.fm span.bg.s_btn_wr input#su.bg.s_btn').text)
driver.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(5)
driver.save_screenshot("picture.png")
driver.quit()