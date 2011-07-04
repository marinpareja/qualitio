from selenium import selenium
import unittest, time, re

class Test18StoreTestcaseCreate(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://127.0.0.1:8000/")
        self.selenium.start()
    
    def test_18_store_testcase_create(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "store" == sel.get_text("link=store"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=store")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if sel.is_text_present("MeeGo Netbook"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("qualitio: store", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo Netbook")
        for i in range(60):
            try:
                if sel.is_text_present("create test case"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("create test case"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=div#application-view-footer div a")
        for i in range(60):
            try:
                if sel.is_text_present("test case"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("test case"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#application-view-menu span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("new", sel.get_text("css=div#application-view-menu span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Parent"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_parent"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_parent", "label=2: /MeeGo Handset bat")
        try: self.failUnless(sel.is_element_present("id_name"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_name", "test case 1")
        try: self.failUnless(sel.is_element_present("id_requirement"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_requirement", "label=1: /MeeGo")
        try: self.failUnless(sel.is_element_present("id_status"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_status", "label=Proposed")
        for i in range(60):
            try:
                if sel.is_element_present("id_description"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_description", "desription\ndesription")
        try: self.failUnless(sel.is_element_present("id_precondition"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_precondition", "precondition\nprecondition")
        try: self.failUnless(sel.is_element_present("css=a#add-step-0 span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("add step", sel.get_text("css=a#add-step-0 span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=a#add-step-0 span")
        for i in range(60):
            try:
                if sel.is_text_present("Step 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_steps-0-description"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_steps-0-expected"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_steps-0-description", "Description 1\nDescription 1")
        sel.type("id_steps-0-expected", "Expected 1\nExpected 1")
        try: self.failUnless(sel.is_element_present("//form[@id='testcase_form']/div[3]/div[2]/div[1]/a/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//form[@id='testcase_form']/div[3]/div[2]/div[1]/a/span")
        for i in range(60):
            try:
                if sel.is_text_present("Step 2"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_steps-1-description"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_steps-1-expected"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_steps-1-description", "Description 2\nDescription 2")
        sel.type("id_steps-1-expected", "Expected 2\nExpected 2")
        try: self.failUnless(sel.is_element_present("css=input.ui-button[value=\"Save\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=input.ui-button[value=\"Save\"]")
        for i in range(60):
            try:
                if sel.is_element_present("link=MeeGo Netbook"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "MeeGo Netbook" == sel.get_text("link=MeeGo Netbook"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=MeeGo Netbook"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("MeeGo Netbook"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=test case 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=test case 1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "test case 1" == sel.get_text("link=test case 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("test case 1", sel.get_text("link=test case 1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=test case 1")
        for i in range(60):
            try:
                if sel.is_text_present("test case: test case 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("full name: /MeeGo Handset bat/test case 1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("parent: /MeeGo Handset bat/"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("status: Proposed"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=exact:1: /MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("1: /MeeGo", sel.get_text("link=exact:1: /MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("desription\ndesription"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("precondition"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("precondition\nprecondition"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=div#application-view div:nth-child(3)")
        try: self.failUnless(sel.is_text_present("step 1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("step 2"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Description 1\nDescription 1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Expected 1\nExpected 1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Description 2\nDescription 2"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Expected 2\nExpected 2"))
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
        try: self.failUnless(sel.is_text_present("Changed name, changed requirement, changed description, changed precondition and changed parent. Added step \"1\" and added step \"2\"."))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
