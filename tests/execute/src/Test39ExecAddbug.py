from selenium import selenium
import unittest, time, re

class Test039ExecAddbug(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://127.0.0.1:8000/")
        self.selenium.start()
    
    def test_039_exec_addbug(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        self.assertEqual("qualitio: requirements", sel.get_title())
        for i in range(60):
            try:
                if sel.is_text_present("qualitio requirements"): break
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
        for i in range(60):
            try:
                if sel.is_element_present("link=TestRun 2"): break
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
                if sel.is_text_present("full name: /TestRun directory/TestRun 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type_keys("//form[@id='testrun_form']/div[4]/div[2]/div/div/div[2]/div/input", "close navi")
        for i in range(60):
            try:
                if sel.is_element_present("link=Close navigation"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//input[@value='1']")
        for i in range(60):
            try:
                if sel.is_element_present("//a[@id='add-testcases-button']/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
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
                if sel.is_element_present("id_testrun-name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=a[href=\"#testrun/1/execute/\"]")
        for i in range(60):
            try:
                if sel.is_element_present("select-all"): break
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
                if sel.is_text_present("exact:Search:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("/MeeGo Netbook/MeeGo IVI BAT/"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("Close navigation"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("test run: TestRun 1"): break
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
                if sel.is_element_present("select-all"): break
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
                if sel.is_text_present("test case: Close navigation"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("test case: Close navigation"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_bugs", "1234")
        sel.click("css=input[value='add']")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs-0-DELETE"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=1234"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=1234"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("we need default style for the html 4 style tags"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("VERIFIED"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("FIXED"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_bugs", "1235")
        sel.click("css=input[value='add']")
        for i in range(60):
            try:
                if sel.is_text_present("id"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs-1-DELETE"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=1235"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=1235"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link={feature} we don"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("DUPLICATE"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=TestRun 2"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TestRun 2"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TestRun 2")
        for i in range(60):
            try:
                if sel.is_text_present("test run: TestRun 2"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("full name: /TestRun directory/TestRun 2"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type_keys("//form[@id='testrun_form']/div[4]/div[2]/div/div/div[2]/div/input", "close navigation")
        for i in range(60):
            try:
                if sel.is_element_present("link=/MeeGo Netbook/MeeGo IVI BAT/"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//form[@id='testrun_form']/div[4]/div[2]/div/div/div[1]/div[1]/div/table/thead/tr/th[1]/input")
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='1']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
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
                if sel.is_element_present("id_testrun-name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//div[@id='application-view-menu']/a[2]")
        for i in range(60):
            try:
                if sel.is_text_present("test run: TestRun 2"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("Close navigation"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("/MeeGo Netbook/MeeGo IVI BAT/"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Close navigation"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//tr[@id='testcaserun_2']/td[1]")
        for i in range(60):
            try:
                if sel.is_text_present("test case: Close navigation"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("origin test case:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=1234"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("we need default style for the html 4 style tags", sel.get_text("link=we need default style for the html 4 style tags"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("VERIFIED"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("FIXED"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("1235", sel.get_text("link=1235"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("{feature} we don", sel.get_text("link={feature} we don"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("DUPLICATE"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("2"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_bugs", "1236")
        sel.click("css=input[value='add']")
        for i in range(60):
            try:
                if sel.is_element_present("link=1236"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs-0-DELETE"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("1236", sel.get_text("link=1236"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id_bugs-0-DELETE")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs-0-DELETE"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=input[value='remove']")
        for i in range(60):
            try:
                if sel.is_text_present("No data available in table"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("No data available in table"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TestRun 1")
        for i in range(60):
            try:
                if sel.is_text_present("test run: TestRun 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("full name:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//div[@id='application-view-menu']/a[2]")
        for i in range(60):
            try:
                if sel.is_text_present("/MeeGo Netbook/MeeGo IVI BAT/"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("Close navigation"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("//div[@id='testcaserun-list']/div[2]/select"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("#1235"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("#1234"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//tr[@id='testcaserun_1']/td[1]")
        for i in range(60):
            try:
                if sel.is_text_present("test case: Close navigation"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("origin test case:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//form[@id='testcaserun-remove-bug-form']/div[2]/div[1]/div[1]/div/table/thead/tr/th[1]/input")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs-0-DELETE"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_bugs-1-DELETE"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=input[value='remove']")
        for i in range(60):
            try:
                if sel.is_element_present("//form[@id='testcaserun-remove-bug-form']/div[2]/div[1]/div[2]/table/tbody/tr/td"): break
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
                if sel.is_element_present("//form[@id='testcaserun-remove-bug-form']/div[2]/div[1]/div[1]/div/table/thead/tr/th[1]/input"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//form[@id='testcaserun-remove-bug-form']/div[2]/div[1]/div[2]/table/tbody/tr/td"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("No data available in table"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("off", sel.get_value("//input[@value='1']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='1']")
        try: self.failUnless(sel.is_element_present("//a[@id='remove-testcases-button']/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//a[@id='remove-testcases-button']/span")
        for i in range(60):
            try:
                if sel.is_text_present("No data available in table"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("Executed"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("Executed")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=details"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=details")
        for i in range(60):
            try:
                if sel.is_text_present("test run: TestRun 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("test cases:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TestRun 2"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TestRun 2"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TestRun 2")
        for i in range(60):
            try:
                if sel.is_element_present("link=edit"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("edit"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=edit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("select-all"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("select-all")
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='1']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//a[@id='remove-testcases-button']/span")
        for i in range(60):
            try:
                if sel.is_text_present("No data available in table"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("Executed"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("Executed")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_testrun-parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=details"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=details")
        for i in range(60):
            try:
                if sel.is_text_present("No data available in table"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("No data available in table"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//li[@id='1_testrundirectory']/ins")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
