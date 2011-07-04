from selenium import selenium
import unittest, time, re

class Test14TestcasesVerify(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://127.0.0.1:8000/")
        self.selenium.start()
    
    def test_14_testcases_verify(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if "requirement: MeeGo" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=test cases"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.failUnless(sel.is_element_present("css=div#application-view-header h1"))
        sel.click("link=test cases")
        for i in range(60):
            try:
                if sel.is_element_present("//form[@id='testcases_connect_form']/div[2]/div/div/div[1]/div[1]/div/table/thead/tr/th[1]/div[1]/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//form[@id='testcases_connect_form']/div[3]/div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[2]/div/div/div[1]/div[1]/div/table/thead/tr/th[1]/div[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[3]/div/div/div[1]/div[1]/div/table/thead/tr/th[1]/div[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[3]/div"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[2]/div/div/div[1]/div[1]/div/table/thead/tr/th[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=a#remove-testcases-button span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=a#add-testcases-button span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Search:"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=input[type='text']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("Executed"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=input[value='1']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("id"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("path"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("name"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("modified"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[2]/div/div/div[1]/div[1]/div/table/thead/tr/th[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[2]/div/div/div[1]/div[1]/div/table/thead/tr/th[3]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[2]/div/div/div[1]/div[1]/div/table/thead/tr/th[4]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[3]/div/div/div[1]/div[1]/div/table/thead/tr/th[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[3]/div/div/div[1]/div[1]/div/table/thead/tr/th[3]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[3]/div/div/div[1]/div[1]/div/table/thead/tr/th[4]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[3]/div/div/div[1]/div[1]/div/table/thead/tr/th[5]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[3]/div/div/div[1]/div[2]/table/tbody"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//form[@id='testcases_connect_form']/div[2]/div/div/div[1]/div[1]/div/table/thead/tr/th[1]/div[1]/span")
        for i in range(60):
            try:
                if sel.is_element_present("//div[@name='all']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//div[@name='all']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//div[@name='none']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//div[@name='invert']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//form[@id='testcases_connect_form']/div[3]/div/div/div[1]/div[1]/div/table/thead/tr/th[1]/div[1]")
        for i in range(60):
            try:
                if sel.is_element_present("//form[@id='testcases_connect_form']/div[3]/div/div/div[1]/div[1]/div/table/thead/tr/th[1]/div[2]/div[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[3]/div/div/div[1]/div[1]/div/table/thead/tr/th[1]/div[2]/div[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[3]/div/div/div[1]/div[1]/div/table/thead/tr/th[1]/div[2]/div[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcases_connect_form']/div[3]/div/div/div[1]/div[1]/div/table/thead/tr/th[1]/div[2]/div[3]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
