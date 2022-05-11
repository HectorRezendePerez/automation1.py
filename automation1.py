import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#find_by_xpath
def F_B_X (xpath, tempo, send_keys=False):
    if send_keys:
        rtn = navegador.find_element(by=By.XPATH, value=xpath).send_keys(send_keys)
        time.sleep(tempo)
        return 0
    navegador.find_element(by=By.XPATH, value=xpath).click()
    time.sleep(tempo)
    return 1

Email = input('qual o email, camarada?')
Senha = input('e a senha?')

navegador = webdriver.Chrome()
navegador.get('https://login.microsoftonline.com/')
time.sleep(3)

F_B_X('//*[@id="i0116"]', 2, Email)
F_B_X('//*[@id="idSIButton9"]',2,'')
F_B_X('//*[@id="i0118"]',1,Senha)
F_B_X('//*[@id="idSIButton9"]',1,'')
F_B_X('//*[@id="KmsiCheckboxField"]',1,'')
F_B_X('//*[@id="idBtn_Back"]',4,'')

pyautogui.click(x=1023, y=18)
print('foda né?')