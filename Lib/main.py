from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from tkinter import messagebox

import selenium.common.exceptions as exc
import os
import time
#------------------------ FUNCTIONS ------------------------

def wait_five(driver):
    driver.implicitly_wait(5)

def wait_ten(driver):
    driver.implicitly_wait(10)

def open_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    return driver

def login(driver):
    email = os.environ.get("USERNAME")
    pw = os.environ.get("PASSWORD")
    driver.get("https://instagram.com")
    facebook_button = driver.find_element(
        By.CSS_SELECTOR, value='._ab37')
    facebook_button.click()
    username_input = driver.find_element(By.ID, value='email')
    pw_input = driver.find_element(By.ID, value='pass')
    login_button = driver.find_element(By.ID, value="loginbutton")
    username_input.send_keys(email)
    pw_input.send_keys(pw)
    login_button.click()


def search_account(driver, account):
    not_now = driver.find_element(
        By.XPATH, value='/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')

    not_now.click()
    buttons = driver.find_elements(By.CSS_SELECTOR, value=".xo237n4.xo237n4")
    search_button = buttons[2]
    action = ActionChains(driver)
    action.move_to_element(search_button).click().perform()
    search_input = driver.find_element(By.TAG_NAME, value="input")
    search_input.send_keys(account)
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

def select(driver):
    time.sleep(3)
    results = driver.find_elements(
        By.XPATH,
        value="//a[@class='x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 "
              "x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985"
              " xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm"
              " xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd "
              "x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o "
              "x1lku1pv x1a2a7pz x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3']")

    desired_account = results[0]
    desired_account.click()

def follow_followers(driver):
    followers = driver.find_element(
        By.XPATH,
        value="//a[@class='x1i10hfl xjbqb8w x1ejq31n"
              " xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l"
              " x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2"
              " xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu"
              " x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq"
              " x1a2a7pz _alvs _a6hd']")

    followers.click()
    wait_five(driver)
    buttons = driver.find_elements(By.CSS_SELECTOR,
                                   value="._acas:not(._acao), a._acas:not(._acao), a._acas:not(._acao):visited")

    execute_function = [button.click() for button in buttons]

#------------------------ MAIN OPERATION ------------------------

try:
    account_to_search = os.environ.get("SOME_ACCOUNT")
    my_driver = open_browser()
    wait_five(my_driver)
    login(my_driver)
    wait_ten(my_driver)
    search_account(my_driver, account_to_search)
    select(my_driver)
    follow_followers(my_driver)

except exc.NoSuchElementException as err:
    messagebox.showerror(message=err.msg)

except IndexError as err:
    messagebox.showerror(message=err.msg)
