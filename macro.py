from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Macro:
    mobile_emulation = {"deviceName": "iPhone 6"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument('--user-data-dir=C:\Programming\chromedriverSetting')
    prefs = {'profile.default_content_setting_values':
            {'cookies' : 1, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2,
            'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2,
            'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2,
            'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome("C:\Programming\chromedriver_win32\chromedriver", options=chrome_options)

    def loadUrl(self, url. siteName):
        Macro.driver.get(url)
        completeMsg("사이트 로드")

    # 엔터가 클릭보다 빠르다, 클릭으로 안되고 엔터만 되는 버튼도 있음
    def enterButtonNow(self, xpath, buttonName):
        button = Macro.driver.find_elements_by_xpath(xpath)
        if len(button) != 0:
            button[0].send_keys(Keys.ENTER)
            completeMsg(buttonName+" 클릭")

    def clickButtonNow(self, xpath, buttonName):
        button = Macro.driver.find_elements_by_xpath(xpath)
        if len(button) != 0:
            button[0].click
            completeMsg(buttonName+" 클릭")

    def waitNewPage(self, xpath):
        print("새로운 페이지 기다리는중...")
        Macro.driver.implicitly_wait(10)
        completeMsg("새 페이지 로드")
        
    def enterButtonAfterClickable(self, xpath, buttonName):
        print(buttonName + " 대기 중...")
        button = WebDriverWait(Macro.driver, 10).until(EC.element_to_be_clickable((By.XPATH,xpath)));
        button.send_keys(Keys.ENTER)
        completeMsg(buttonName+" 클릭")

    def waitAndenterButtonAfterClickable(self, xpath, buttonName, delay):
        waitMsg(buttonName+ " 탐색")
        button = WebDriverWait(Macro.driver, 10).until(EC.element_to_be_clickable((By.XPATH,xpath)));
        time.sleep(delay)
        button.send_keys(Keys.ENTER)
        completeMsg(buttonName+" 클릭")
        
    def waitMsg(work):
        print("기다리는 중 : "+ work)
    def completeMsg(work):
        print("완료함 : " + work)
        
    # 클릭 안되는 버튼은 iframe이 둘러싸고 있는지 확인하고,
    # 만약 그렇다면 iframe을 전환해줘야 한다.    
    def switchIframe(self, xpath):
        driver.switch_to.frame(driver.find_element_by_xpath(xpath))
        print("프레임 변경 완료")
        
    
