from selenium import selenium
import unittest, time, re

class Test040ExecAddbug(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://127.0.0.1:8000/")
        self.selenium.start()
    
    def test_040_exec_addbug(self):
        sel = self.selenium
        sel.open("/require/#requirement/9/details/")
        self.assertEqual("qualitio: requirements", sel.get_title())
        for i in range(60):
            try:
                if sel.is_element_present("link=execute"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=execute")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("qualitio: execute", sel.get_title())
        for i in range(60):
            try:
                if sel.is_text_present("qualitio execute"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TestRun directory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=li#1_testrundirectory ins")
        for i in range(60):
            try:
                if sel.is_element_present("link=TestRun 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=TestRun 1")
        for i in range(60):
            try:
                if sel.is_text_present("test run: TestRun 1"): break
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
                if sel.is_element_present("css=div#application-view-menu a:nth-child(2)"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=notes"): break
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
        for i in range(60):
            try:
                if sel.is_element_present("id_parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='1' and @type='checkbox']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='1' and @type='checkbox']")
        try: self.failUnless(sel.is_element_present("//a[@id='add-testcases-button']/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//a[@id='add-testcases-button']/span")
        for i in range(60):
            try:
                if sel.is_element_present("link=Close navigation"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Close navigation"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='testrun_form']/div[4]/div[2]/div/div/div[1]/div[2]/table/tbody"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("Executed")
        for i in range(60):
            try:
                if sel.is_element_present("link=details"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=notes"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.refresh()
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if sel.is_element_present("link=details"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#application-view-menu a:nth-child(3)"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-menu a:nth-child(3)")
        for i in range(60):
            try:
                if sel.is_element_present("css=div.select-btn"): break
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
        for i in range(60):
            try:
                if sel.is_text_present("name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("css=tr#testcaserun_1 td:nth-child(4)"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("css=tr#testcaserun_1 td:nth-child(4)"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=div#header div")
        sel.click("css=tr#testcaserun_1 td:nth-child(4)")
        for i in range(60):
            try:
                if sel.is_text_present("test case: Close navigation"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("precondition"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("test case: Close navigation"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_bugs"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_bugs", "1234,1235,1236")
        sel.click("css=input[value='add']")
        for i in range(60):
            try:
                if sel.is_element_present("link=1234"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=1235"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=1236"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("VERIFIED"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_bugs-0-DELETE"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_bugs-1-DELETE"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_bugs-2-DELETE"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=1234"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=1235"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=1236"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("we need default style for the html 4 style tags", sel.get_text("link=we need default style for the html 4 style tags"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("VERIFIED"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("DUPLICATE"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("FIXED"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("INVALID"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("#1234 #1235 #1236"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id_bugs-0-DELETE")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs-0-DELETE"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("id_bugs-1-DELETE")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs-1-DELETE"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("id_bugs-2-DELETE")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs-2-DELETE"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='remove']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//input[@value='remove']")
        for i in range(60):
            try:
                if sel.is_element_present("//form[@id='testcaserun-remove-bug-form']/div[2]/div/div[2]/table/tbody/tr/td"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("No data available in table"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='remove']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("Bugs"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=details")
        for i in range(60):
            try:
                if sel.is_text_present("test run: TestRun 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("full name: /TestRun directory/TestRun 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//div[@id='application-view-menu']/a[2]")
        for i in range(60):
            try:
                if sel.is_element_present("css=div.select-btn"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//tr[@id='testcaserun_1']/td[1]/input"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//tr[@id='testcaserun_1']/td[1]")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("test case: Close navigation"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_bugs"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_bugs", "1237 , 1238 , 1239")
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='add']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("1237 , 1238 , 1239", sel.get_value("id_bugs"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_bugs"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='add']")
        for i in range(60):
            try:
                if sel.is_element_present("link=1237"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=1238"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=1239"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=1237"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=1238"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=1239"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("#1237 #1238 #1239"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id_bugs-0-DELETE")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs-0-DELETE"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("id_bugs-1-DELETE")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs-1-DELETE"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("id_bugs-2-DELETE")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs-2-DELETE"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='remove']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//input[@value='remove']")
        for i in range(60):
            try:
                if sel.is_element_present("//form[@id='testcaserun-remove-bug-form']/div[2]/div/div[2]/table/tbody/tr/td"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("No data available in table"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//form[@id='testcaserun-remove-bug-form']/div[2]/div/div[2]/table/tbody/tr/td"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=details")
        for i in range(60):
            try:
                if sel.is_text_present("test run: TestRun 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=Close navigation"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//div[@id='application-view-menu']/a[2]")
        for i in range(60):
            try:
                if sel.is_element_present("css=div.select-btn"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//tr[@id='testcaserun_1']/td[1]/input"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//tr[@id='testcaserun_1']/td[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//tr[@id='testcaserun_1']/td[1]")
        for i in range(60):
            try:
                if sel.is_text_present("test case: Close navigation"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("Bugs"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='add']"): break
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
        sel.type("id_bugs", "1231, 1232, 1233, 1234")
        try: self.assertEqual("1231, 1232, 1233, 1234", sel.get_value("id_bugs"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='add']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//input[@value='add']")
        for i in range(60):
            try:
                if sel.is_element_present("link=1231"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=1232"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=1231"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=1232"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=1233"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=1234"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("#1231 #1232 #1233 #1234"))
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
        try: self.failUnless(sel.is_element_present("//input[@value='1' and @type='checkbox']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='1' and @type='checkbox']")
        try: self.failUnless(sel.is_element_present("//a[@id='remove-testcases-button']/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//a[@id='remove-testcases-button']/span")
        for i in range(60):
            try:
                if sel.is_element_present("link=Close navigation"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
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
                if sel.is_element_present("link=details"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.refresh()
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if sel.is_element_present("link=details"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=details")
        for i in range(60):
            try:
                if sel.is_text_present("test run: TestRun 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("full name: /TestRun directory/TestRun 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("No data available in table"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("test run: TestRun 1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("full name: /TestRun directory/TestRun 1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
