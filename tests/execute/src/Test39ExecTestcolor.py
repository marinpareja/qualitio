from selenium import selenium
import unittest, time, re

class Test39ExecTestcolor(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://127.0.0.1:8000/")
        self.selenium.start()
    
    def test_39_exec_testcolor(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        self.assertEqual("qualitio: requirements", sel.get_title())
        for i in range(60):
            try:
                if sel.is_text_present("qualitio requirements"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=require"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=store"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=execute"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=execute"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=execute")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if sel.is_text_present("qualitio execute"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertEqual("qualitio: execute", sel.get_title())
        for i in range(60):
            try:
                if sel.is_element_present("//li[@id='1_testrundirectory']/ins"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//li[@id='1_testrundirectory']/ins"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//li[@id='1_testrundirectory']/ins")
        for i in range(60):
            try:
                if sel.is_element_present("link=TestRun 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TestRun 2"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TestRun 1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TestRun 1")
        for i in range(60):
            try:
                if sel.is_element_present("//div[@id='application-view-header']/h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("test run: TestRun 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("test run: TestRun 1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=edit"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=edit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type_keys("//form[@id='testrun_form']/div[4]/div[2]/div/div/div[2]/div/input", "Case1")
        for i in range(60):
            try:
                if sel.is_element_present("link=TestCase1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TestCase10"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='4']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='4']")
        try: self.failUnless(sel.is_element_present("//a[@id='add-testcases-button']/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='4']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//a[@id='add-testcases-button']/span")
        try: self.failUnless(sel.is_element_present("Executed"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("Executed")
        for i in range(60):
            try:
                if sel.is_text_present("test run : TestRun 1"): break
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
                if sel.is_element_present("id_parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//div[@id='application-view-menu']/a[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//div[@id='application-view-menu']/a[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//div[@id='application-view-menu']/a[2]")
        for i in range(60):
            try:
                if sel.is_text_present("id"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("path"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//tr[@id='testcaserun_6']/td[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//tr[@id='testcaserun_6']/td[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//tr[@id='testcaserun_6']/td[2]")
        for i in range(60):
            try:
                if sel.is_text_present("test case: TestCase1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("parent: /MeeGo Netbook/MeeGo IVI BAT"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("origin test case: /MeeGo Netbook/MeeGo IVI BAT/TestCase1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//form[@id='testcaserun-status-form']/label[1]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcaserun-status-form']/label[2]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testcaserun-status-form']/label[3]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("IDLE"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("PASSED"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("FAILED"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("FAILED", sel.get_text("//form[@id='testcaserun-status-form']/label[3]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("PASSED", sel.get_text("//form[@id='testcaserun-status-form']/label[2]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("IDLE", sel.get_text("//form[@id='testcaserun-status-form']/label[1]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//form[@id='testcaserun-status-form']/label[2]/span")
        sel.click("id_status_1")
        for i in range(60):
            try:
                if sel.is_element_present("//tr[@style=\"background: none repeat scroll 0% 0% rgb(136, 187, 102);\"]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//tr[@style=\"background: none repeat scroll 0% 0% rgb(136, 187, 102);\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//form[@id='testcaserun-status-form']/label[3]/span")
        sel.click("id_status_2")
        for i in range(60):
            try:
                if sel.is_element_present("//tr[@style=\"background: none repeat scroll 0% 0% red;\"]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//tr[@style=\"background: none repeat scroll 0% 0% red;\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//form[@id='testcaserun-status-form']/label[4]/span")
        sel.click("id_status_3")
        for i in range(60):
            try:
                if sel.is_element_present("//tr[@style=\"background: none repeat scroll 0% 0% red;\"]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//tr[@style=\"background: none repeat scroll 0% 0% red;\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//form[@id='testcaserun-status-form']/label[4]/span")
        sel.click("//form[@id='testcaserun-status-form']/label[1]/span")
        sel.click("id_status_0")
        for i in range(60):
            try:
                if sel.is_element_present("//tr[@style=\"background: none repeat scroll 0% 0% rgb(204, 238, 238);\"]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//tr[@style=\"background: none repeat scroll 0% 0% rgb(204, 238, 238);\"]"))
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
        try: self.failUnless(sel.is_text_present("Test case run: 6: Changed status to 'passed'."))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Test case run: 6: Changed status to 'failed'."))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Test case run: 6: Changed status to 'n/a'."))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Test case run: 6: Changed status to 'idle'."))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=edit"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=edit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//input[@value='4']")
        for i in range(60):
            try:
                if sel.is_element_present("//a[@id='remove-testcases-button']/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//a[@id='remove-testcases-button']/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//a[@id='remove-testcases-button']/span")
        for i in range(60):
            try:
                if sel.is_element_present("//div[@id='application-view-footer']/div/input"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//div[@id='application-view-footer']/div/input")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
