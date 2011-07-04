from selenium import selenium
import unittest, time, re

class Test30ExecTestdirectCreate(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://127.0.0.1:8000/")
        self.selenium.start()
    
    def test_30_exec_testdirect_create(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        self.assertEqual("qualitio: requirements", sel.get_title())
        for i in range(60):
            try:
                if sel.is_element_present("link=execute"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "execute" == sel.get_text("link=execute"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=execute")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("qualitio: execute", sel.get_title())
        for i in range(60):
            try:
                if sel.is_element_present("link=TestRun directory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=TestRun directory")
        for i in range(60):
            try:
                if sel.is_text_present("test run directory: TestRun directory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("test run directory: TestRun directory"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=div#application-view-footer div a:nth-child(2)")
        for i in range(60):
            try:
                if sel.is_text_present("test run directory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_name", "testrun subdirectory")
        try: self.failUnless(sel.is_text_present("Description"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_description", "Description\ndescription")
        sel.click("css=input[name='Executed'][value='Save']")
        for i in range(60):
            try:
                if sel.is_element_present("link=details"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("test run directory : testrun subdirectory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("test run directory : testrun subdirectory"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=details")
        for i in range(60):
            try:
                if sel.is_text_present("test run directory: testrun subdirectory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("full name: /TestRun directory/testrun subdirectory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("full name: /TestRun directory/testrun subdirectory"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Description\ndescription"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TestRun directory")
        for i in range(60):
            try:
                if sel.is_text_present("test run directory: TestRun directory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//div[@id='application-view']/div[3]/div[4]/div[1]/div[2]/table/tbody/tr[1]/td[4]/a"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("testrun subdirectory", sel.get_text("//div[@id='application-view']/div[3]/div[4]/div[1]/div[2]/table/tbody/tr[1]/td[4]/a"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("TestRun 1", sel.get_text("//div[@id='application-view']/div[3]/div[4]/div[1]/div[2]/table/tbody/tr[2]/td[4]/a"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("TestRun 2", sel.get_text("//div[@id='application-view']/div[3]/div[4]/div[1]/div[2]/table/tbody/tr[3]/td[4]/a"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//div[@id='application-view']/div[3]/div[4]/div[1]/div[2]/table/tbody/tr[1]/td[4]/a")
        for i in range(60):
            try:
                if sel.is_text_present("test run directory: testrun subdirectory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("testrun subdirectory", sel.get_value("id_name"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Description description", sel.get_text("id_description"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=history"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=history")
        for i in range(60):
            try:
                if sel.is_text_present("date"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("user"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("comment"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("Changed name, changed parent and changed description."))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
