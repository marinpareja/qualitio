from selenium import selenium
import unittest, time, re

class Test11Subrequir(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://127.0.0.1:8000/")
        self.selenium.start()
    
    def test_11_subrequir(self):
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
        sel.click("//li[@id='1_requirement']/ins")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if "requirement" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_name", "new requirement 8")
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#ui-datepicker-div div div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=1")
        sel.click("release_target_wrapper")
        for i in range(60):
            try:
                if sel.is_text_present("requirement"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("Executed")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 8"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=new requirement 8"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=new requirement 8")
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: new requirement 8"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirements:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("full name: /MeeGo/TV/new requirement 8"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if "requirement" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_name", "new subrequirement 8")
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#ui-datepicker-div div div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=1")
        sel.click("release_target_wrapper")
        for i in range(60):
            try:
                if sel.is_text_present("new requirement"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("Executed")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 8"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: new subrequirement 8"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=new subrequirement 8")
        for i in range(60):
            try:
                if sel.is_text_present("full name: /MeeGo/TV/new requirement 8/new subrequirement 8"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("directory: /MeeGo/TV/new requirement 8/"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=new requirement 8"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("exact:requirement: new subrequirement 8"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("full name: /MeeGo/TV/new requirement 8/new subrequirement 8"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("directory: /MeeGo/TV/new requirement 8/"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//div[@id='application-view-footer']/div/a/span")
        for i in range(60):
            try:
                if "requirement" == sel.get_text("css=div#application-view-header h1"): break
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
        for i in range(60):
            try:
                if sel.is_element_present("id_release_target"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_name"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_name", "new sub2requirement 8")
        sel.select("id_parent", "label=29: /MeeGo/TV/new requirement 8")
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#ui-datepicker-div div div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=1")
        sel.click("release_target_wrapper")
        for i in range(60):
            try:
                if sel.is_text_present("new requirement"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("Executed"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("Executed"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("Executed")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: new sub2requirement 8"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 8"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("exact:requirement: new sub2requirement 8"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=new requirement 8"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=details")
        for i in range(60):
            try:
                if sel.is_text_present("exact:directory:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("directory: /MeeGo/TV/new requirement 8/"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("requirements:"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("No data available in table"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Showing 0 to 0 of 0 entries"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("full name: /MeeGo/TV/new requirement 8/new sub2requirement 8"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("directory: /MeeGo/TV/new requirement 8/"))
        except AssertionError, e: self.verificationErrors.append(str(e))

        # <tr>
        # 	<td>click</td>
        # 	<td>//div[@id='application-view-footer']/div/a/span</td>
        # 	<td></td>
        # </tr>
        # <tr>
        # 	<td>click</td>
        # 	<td>//li[@id='28_requirement']/ins</td>
        # 	<td></td>
        # </tr>
        # <tr>
        # 	<td>clic</td>
        # 	<td>link=new requirement 8</td>
        # 	<td></td>
        # </tr>
        # <tr>
        # 	<td>waitForTextPresent</td>
        # 	<td>exact:requirement: new requirement 8</td>
        # 	<td></td>
        # </tr>
        # <tr>
        # 	<td>waitForTextPresent</td>
        # 	<td>exact:requirements:</td>
        # 	<td></td>
        # </tr>
        # <tr>
        # 	<td>waitForTextPresent</td>
        # 	<td>testcases</td>
        # 	<td></td>
        # </tr>
        # <tr>
        # 	<td>verifyTextPresent</td>
        # 	<td>full name: /MeeGo/TV/new requirement 8</td>
        # 	<td></td>
        # </tr>
        # <tr>
        # 	<td>verifyTextPresent</td>
        # 	<td>new subrequirement 8</td>
        # 	<td></td>
        # </tr>
        # <tr>
        # 	<td>verifyTextPresent</td>
        # 	<td>new sub2requirement 8</td>
        # 	<td></td>
        # </tr>
        # <tr>
        # 	<td>verifyElementPresent</td>
        # 	<td>//div[@id='application-view']/div[4]/div/div[1]/div[2]/table/tbody/tr[1]/td[3]/a</td>
        # 	<td></td>
        # </tr>
        # <tr>
        # 	<td>verifyElementPresent</td>
        # 	<td>//div[@id='application-view']/div[4]/div/div[1]/div[2]/table/tbody/tr[2]/td[3]/a</td>
        # 	<td></td>
        # </tr>


        try: self.failUnless(sel.is_element_present("link=new requirement 8"))

        except AssertionError, e: self.verificationErrors.append(str(e))

        try: self.failUnless(sel.is_element_present("link=new sub2requirement 8"))

        except AssertionError, e: self.verificationErrors.append(str(e))

        try: self.failUnless(sel.is_element_present("link=new subrequirement 8"))

        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
