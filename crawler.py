# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, codecs,os

class Crawler(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.base_url = "http://mabhoomi.telangana.gov.in/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_crawler(self):
        driver = self.driver
        f = open("options/17.txt")
        for line in f.readlines():
            print line
            try:
                village = line.split(",")[1].split("\n")[0]
                mnd = line.split(",")[0]
                driver.get(self.base_url + "/Pahaani.aspx?v="+village)
                path = "options/17/"+mnd+"/"+village
                if not os.path.exists(path):
                    os.makedirs(path)
                    f = codecs.open(path+"/1.html","w","utf-8")
                    f.write(driver.page_source)
                    for i in range(2,15):
                        driver.find_element_by_xpath("//select[@id='ddlPageNumbers']/option["+str(i)+"]").click()
                        time.sleep(1)
                        f = codecs.open("options/17/"+mnd+"/"+village+"/"+str(i)+".html","w","utf-8")
                        f.write(driver.page_source)
            except:
                pass

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
