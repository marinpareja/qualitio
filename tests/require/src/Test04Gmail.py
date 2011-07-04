from selenium import selenium
import unittest, time, re

class Test04Gmail(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://127.0.0.1:8000/")
        self.selenium.start()
    
    def test_04_gmail(self):
        sel = self.selenium
        sel.open("/login/?next=/")
        self.assertEqual("qualitio: login", sel.get_title())
        sel.open("https://www.google.com/accounts/ServiceLogin?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Fui%3Dhtml%26zy%3Dl&bsv=llya694le36z&ss=1&scc=1&ltmpl=default&ltmplcache=2&hl=pl")
        for i in range(60):
            try:
                if "Gmail: innowacyjna poczta Google" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertEqual("Gmail: innowacyjna poczta Google", sel.get_title())
        for i in range(60):
            try:
                if sel.is_element_present("Email"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("Email", "qualitio1")
        sel.type("Passwd", "testqual")
        try: self.failUnless(sel.is_element_present("signIn"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("signIn")
        sel.wait_for_page_to_load("30000")
        sel.open("/login/?next=/")
        for i in range(60):
            try:
                if sel.is_text_present("qualitio"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//div[@id='openid']/div[2]/a[1]/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//div[@id='openid']/div[2]/a[1]/span")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "qualitio: requirements" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("requirements"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertEqual("qualitio: requirements", sel.get_title())
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
