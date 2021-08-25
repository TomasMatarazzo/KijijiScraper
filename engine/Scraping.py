
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import datetime
import os
import time
import random
import pandas as pd
from engine.const import *
from pathlib import Path
import re

#Remember in case there is no category
class Scraping:

    def __init__(self):
        self.url_excel = ""


    def FindPage(self, arg1, arg2, state, city):

        try:
            marketplace = 'https://www.kijiji.ca/'

            #Starting safari driver
            driver = webdriver.Safari()

            #Later we will check with mobile-facebook

            driver.get(marketplace)
            driver.maximize_window()

        except :
            print("Error1")


        try:
            #Founding the kijiji searches

            driver.get(marketplace)
            #Temporary values 

            i = str(arg1)
            j = str(arg2)


            # Selection of the location

            address_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.location-wrapper ul li:nth-child('+ i +')')))
            address_box.click()
            level2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.location-wrapper ul:nth-child(2) li:nth-child('+ j +')')))
            level2.click()
            send = driver.find_element(By.ID,'LocUpdate')
            send.click()

            #Selection of the filters

            time.sleep(4)
            button =  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.label-1952128162')))
            button.click()
            time.sleep(5)
            category = driver.find_element(By.ID,'SearchCategorySelector-item-3')
            category.click()
            time.sleep(2)
            search = driver.find_element(By.ID, 'SearchKeyword')
            search.send_keys('Wanted Office Space')
            time.sleep(2)
            send = driver.find_element(By.NAME,'SearchSubmit')
            send.click()
            time.sleep(2)
            rent = driver.find_element(By.CSS_SELECTOR,'.link-1494669714')
            rent.click()
            time.sleep(2)
            commerce = driver.find_element(By.CSS_SELECTOR, '.arrowRightContainer-1684363492')
            commerce.click()
            time.sleep(2)
            commerce = driver.find_element(By.CSS_SELECTOR, '.slider-2889926755 a:nth-child(6)')
            time.sleep(5)
            commerce.click()


            time.sleep(3)
            commerce = driver.find_element(By.CSS_SELECTOR, '.addFiltersText-2852895903')
            commerce.click()

            for i in range(3):
                driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            commerce = driver.find_element(By.CSS_SELECTOR, '.form-3964758212  div:nth-child(2) div:nth-child(19) div div div:nth-child(3)')
            commerce.click()
            try:
                button = driver.find_element(By.CSS_SELECTOR, '.footer-2611485020 button')
                button.click()
            except:
                print("error")

            a = datetime.datetime.now()
            url2 = str(a.strftime('%y-%m-%d-%H:%M:%S'))
            url_excel = state + '/' + city +'/'+url2
            url_excel = url_excel.replace('/', '-')
            url_excel = url_excel.replace(':', '-')
            url_excel= '/city-' + url_excel
            self.url_excel = url_excel

        except:
            print('e')



        # Searching all the elements and saving it on a list
        time.sleep(random.randint(1, 3))
        urls = []
        info = []

        MorePages = True
        while ( MorePages):
            n_scrolls = 2

            for n in range(1,n_scrolls):
                driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(5)
                elements = driver.find_elements(By.CSS_SELECTOR, ".title:nth-child(1)")
                elements = [x.get_attribute('href') for x in elements ]
                elements = list(set(elements))
            for e in elements:
                urls.append(e)

            try:
                next_page = driver.find_element(By.CSS_SELECTOR,"a[title = 'Next']")
                next_page.click()
            except:
                MorePages = False

        i = 0
        for e in urls:
                i = i + 1
                info.append(self.Extract(e,driver))
        return info

    def Extract( self, url , driver):

            driver.get(url)
            information = {
                'Page Link': url,
                'Date':'-',
                'Unique Id':'-',
                'Title': '-',
                'Description': '-',
                'Address': '-',
                'Phone': '-',
            }
            # Searching the information for each item of the dic
            #Finding id

            id = [int(s) for s in re.findall(r'-?\d+\.?\d*',url )][0]
            information['Unique Id'] = id

            # Finding the Title

            title = driver.find_element(By.CSS_SELECTOR,
                                            "h1[class = 'title-2323565163'] ")
            information['Title'] = title.text


            # Finding the description

            des = driver.find_element(By.CSS_SELECTOR,
                                            "p").text

            number = [s for s in re.findall(r'\d\d\d.\d\d\d.\d\d\d\d',des)]

            information['Description'] = des
            try:
                information['Phone'] = number[0]
            except:
                information['Phone'] = '-'

            #Finding the date

            enter = False

            try:
                enter = True
                date = driver.find_element(By.CSS_SELECTOR,
                                            ".datePosted-383942873 time")
                date = date.get_attribute('datetime')

                date = date.split('T')

                date = date[0]

                information['Date'] = date

            except:
                try:
                    date = driver.find_element(By.CSS_SELECTOR,
                                            ".datePosted-383942873 span")
                    date = date.get_attribute('title')

                    information['Date'] = date
                except:
                    print('error')



        #Address

            try:
                address = driver.find_element(By.CSS_SELECTOR,
                                            ".address-3617944557").text
                information['Address'] = address
            except:
                print("no address")

            return information

    def createExcel(self,info):

            df = pd.DataFrame(info)
            temp = str(Path(__file__).parent.parent.absolute())
            temp = temp + '/Data'
            df.to_excel(temp + self.url_excel +'.xlsx')