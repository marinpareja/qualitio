from selenium import selenium
import unittest, time, re

class Test46ExecRepeatedBugs(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://127.0.0.1:8000/")
        self.selenium.start()
    
    def test_46_exec_repeated_bugs(self):
        sel = self.selenium
        sel.open("/require/")
        for i in range(60):
            try:
                if "qualitio: requirements" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertEqual("qualitio: requirements", sel.get_title())
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
        for i in range(60):
            try:
                if "qualitio: execute" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertEqual("qualitio: execute", sel.get_title())
        try: self.failUnless(sel.is_element_present("link=TestRun directory"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TestRun directory")
        for i in range(60):
            try:
                if sel.is_text_present("test run directory: TestRun directory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=edit"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#application-view-footer div a span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("create test run"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if sel.is_text_present("test run"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_name"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_name", "testrun1")
        try: self.failUnless(sel.is_element_present("//form[@id='testrun_form']/div[4]/div[2]/div/div/div[2]/div/input"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("//form[@id='testrun_form']/div[4]/div[2]/div/div/div[2]/div/input", "TestCase")
        try: self.failUnless(sel.is_element_present("css=input[value='3']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=input[value='3']")
        for i in range(60):
            try:
                if sel.is_element_present("css=a#add-testcases-button span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("css=a#add-testcases-button span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=a#add-testcases-button span")
        for i in range(60):
            try:
                if sel.is_element_present("css=input[value='3']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TestCase"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("css=tr.disable"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#application-view-footer div input"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=div#application-view-footer div input")
        for i in range(60):
            try:
                if sel.is_text_present("test run : testrun1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("1: /TestRun directory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TestCase"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TestCase"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//div[@id='application-view-menu']/a[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//div[@id='application-view-menu']/a[2]")
        for i in range(60):
            try:
                if sel.is_element_present("//div[@id='testcaserun-list']/div[1]/div[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
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
        try: self.failUnless(sel.is_element_present("//tr[@id='testcaserun_3']/td[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//tr[@id='testcaserun_3']/td[2]")
        for i in range(60):
            try:
                if sel.is_text_present("test case: TestCase"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("origin test case: /MeeGo Netbook/TestCase"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_bugs"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_bugs", "112")
        try: self.failUnless(sel.is_element_present("css=input[value='add']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=input[value='add']")
        for i in range(60):
            try:
                if sel.is_element_present("link=112"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("VERIFIED"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("#112"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TestRun directory"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TestRun directory")
        for i in range(60):
            try:
                if sel.is_text_present("test run directory: TestRun directory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("full name:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#application-view-footer div a span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if sel.is_text_present("test run"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_name"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_name", "testrun2")
        try: self.failUnless(sel.is_element_present("//form[@id='testrun_form']/div[4]/div[2]/div/div/div[2]/div/input"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("//form[@id='testrun_form']/div[4]/div[2]/div/div/div[2]/div/input", "TestCase")
        try: self.failUnless(sel.is_element_present("css=input[value='3']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=input[value='3']")
        for i in range(60):
            try:
                if sel.is_element_present("css=a#add-testcases-button span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("css=a#add-testcases-button span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=a#add-testcases-button span")
        for i in range(60):
            try:
                if sel.is_element_present("css=input[value='3']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TestCase"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TestCase"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//div[@id='application-view-footer']/div/input"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//div[@id='application-view-footer']/div/input")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("test run : testrun2"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("1: /TestRun directory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("testrun2"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TestCase"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TestCase"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("execute"))
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
                if sel.is_text_present("3"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//tr[@id='testcaserun_4']/td[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//tr[@id='testcaserun_4']/td[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//tr[@id='testcaserun_4']/td[2]")
        for i in range(60):
            try:
                if sel.is_text_present("test case: TestCase"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("exact:parent:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("origin test case:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=112"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("make crashes when building zlib looking for PR3240.LIB", sel.get_text("link=make crashes when building zlib looking for PR3240.LIB"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("VERIFIED"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("INVALID"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_bugs", "112")
        try: self.failUnless(sel.is_element_present("//input[@value='add']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='add']")
        for i in range(60):
            try:
                if sel.is_element_present("link=112"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("VERIFIED"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//div[@id='testcaserun-details']/div[3]/div[2]/div/div/div/div[2]/table/tbody/tr/td[2]/a"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TestRun directory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TestRun directory"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TestRun directory")
        for i in range(60):
            try:
                if sel.is_text_present("test run directory: TestRun directory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("full name:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("description"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//div[@id='application-view-footer']/div/a[1]/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//div[@id='application-view-footer']/div/a[1]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//div[@id='application-view-footer']/div/a[1]/span")
        for i in range(60):
            try:
                if sel.is_text_present("test run"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_name"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_name", "testrun3")
        try: self.failUnless(sel.is_element_present("//form[@id='testrun_form']/div[4]/div[2]/div/div/div[2]/div/input"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("//form[@id='testrun_form']/div[4]/div[2]/div/div/div[2]/div/input", "TestCase")
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='3']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//input[@value='3']")
        for i in range(60):
            try:
                if sel.is_element_present("//a[@id='add-testcases-button']/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//a[@id='add-testcases-button']/span")
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='3']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TestCase"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//div[@id='application-view-footer']/div/input"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//div[@id='application-view-footer']/div/input")
        for i in range(60):
            try:
                if sel.is_element_present("link=details"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("test run : testrun3"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=details")
        for i in range(60):
            try:
                if sel.is_text_present("full name: /TestRun directory/testrun3"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("full name: /TestRun directory/testrun3"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TestCase"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TestCase"))
        except AssertionError, e: self.verificationErrors.append(str(e))
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
                if sel.is_text_present("TestCase"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//tr[@id='testcaserun_5']/td[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//tr[@id='testcaserun_5']/td[2]")
        for i in range(60):
            try:
                if sel.is_text_present("test case: TestCase"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("origin test case: /MeeGo Netbook/TestCase"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("origin test case: /MeeGo Netbook/TestCase"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=112"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=112"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("make crashes when building zlib looking for PR3240.LIB", sel.get_text("link=make crashes when building zlib looking for PR3240.LIB"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_bugs"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_bugs", "112")
        try: self.failUnless(sel.is_element_present("//input[@value='add']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='add']")
        for i in range(60):
            try:
                if sel.is_element_present("link=112"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("VERIFIED"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=112"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=make crashes when building zlib looking for PR3240.LIB"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//div[@id='testcaserun-details']/div[3]/div[2]/div/div/div/div[2]/table/tbody/tr/td[2]/a"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//div[@id='testcaserun-details']/div[3]/div[2]/div/div/div/div[2]/table/tbody/tr/td[3]/a"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
