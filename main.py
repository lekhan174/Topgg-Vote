import time
import pyautogui
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("test-type")
options.add_argument("--start-maximized")
options.add_argument("--disable-web-security")
options.add_argument("--allow-running-insecure-content")


def getScript(token):
    script = '''function login(token) {
    setInterval(() => {
      document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
      location.reload();
    }, 2500);
  }'''
    script += f'\nlogin("{token}");'
    return script


def vote(token, url):
    driver = webdriver.Chrome(executable_path="C:/Users/Administrator/.wdm/drivers/chromedriver/win32/96.0.4664.45"
                                              "/chromedriver.exe", options=options)
    driver.get("https://discord.com/login")
    driver.execute_script(script=getScript(token))
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="chakra-modal-20"]/footer/a[1]/button').click()
    time.sleep(5)
    pyautogui.click(x=1114, y=959)
    time.sleep(20)
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[2]/div/div[2]/div/div[1]/main/div[1]/div/div[2]/button').click()
    driver.close()

raw_info = [
  {
    "sites" : [
      "https://top.gg/bot/646937666251915264/vote",
      "https://top.gg/bot/270904126974590976/vote"
    ]
  },
  {
    "token": [
      "NzkyNjc1NTYwMDU2NDIyNDEw.Yb7-tg.leGFLZsSsOW5-3VzIf9ZtjYnC74",
      "ODIyMTM1MDQ4NzE4Nzc4Mzk4.Yb7_LA.pVueklf6CgAousryx3ggz1VRlwg",
      "OTE5MjI3Nzc1ODY3NTcyMjc1.Yb7_ew.jA1Jg2WlqiGl3WQy2PQxBJjsazo"
    ]
  }
]

data = raw_info[0]['sites'][:]
tokens = raw_info[1]['token'][:]
for site in data:
    for token in tokens:
        vote(token=token, url=site)
        time.sleep(2)
        print("Voted!")
