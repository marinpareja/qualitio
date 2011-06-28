# -*- coding: utf-8 -*-
from selenium import selenium
from config import settings
import unittest, time, base64

class BaseSeleniumTestCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 
                                 4444, 
                                 "*%s" % settings['browser'], 
                                 settings['hostname'])
        
        if settings['username']:
            self.selenium.addCustomRequestHeader("Authorization", "Basic %s" % 
                                                 base64.b64encode("%s:%s" % (settings['username'], settings['password'])).strip())
        self.selenium.start()

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

    def login(self):
        sel = self.selenium
        sel.open("/store/#testcasedirectory/1/details/")
        self.assertEqual("qualitio: login", sel.get_title())
        try: self.failUnless(sel.is_text_present("qualitio"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_username"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id_password")
        sel.type_keys("id_password", "admin")
        try: self.failUnless(sel.is_element_present("id_username"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id_username")
        sel.type_keys("id_username", "admin")
        try: self.assertEqual("admin", sel.get_value("id_username"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_password"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//input[@value='login']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='login']")
        for i in range(60):
            try:
                if sel.is_text_present("qualitio store"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=store"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=filter")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if sel.is_element_present("id_username"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("id_username")
        sel.type("id_username", "admin")
        sel.click("id_password")
        sel.type("id_password", "admin")
        sel.click("//input[@value='login']")
        sel.wait_for_page_to_load("30000")


class Test01Loginreport(BaseSeleniumTestCase):
    
    def test_01_loginreport(self):
        sel = self.selenium
        sel.open("/report/")
        self.assertEqual("qualitio: login", sel.get_title())
        for i in range(60):
            try:
                if sel.is_text_present("qualitio"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("qualitio"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id_username")
        sel.type("id_username", "admin")
        sel.click("id_password")
        sel.type("id_password", "admin")
        sel.click("css=div.right")
        try: self.failUnless(sel.is_element_present("//input[@value='login']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='login']")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("qualitio: report", sel.get_title())
        for i in range(60):
            try:
                if sel.is_text_present("qualitio report"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("qualitio report"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Welcome, admin"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=Log out"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=Log out")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("qualitio: login", sel.get_title())
        try: self.failUnless(sel.is_text_present("qualitio"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id_username")
        sel.type("id_username", "admin")
        sel.click("id_password")
        sel.type("id_password", "admin")
        sel.click("css=div.right")
        sel.click("//input[@value='login']")
        sel.wait_for_page_to_load("30000")


class Test43ReportRepdirectCreate(BaseSeleniumTestCase):
    
    def test_43_report_repdirect_create(self):
        self.login()
        sel = self.selenium
        sel.open("/require/")
        self.assertEqual("qualitio: requirements", sel.get_title())
        for i in range(60):
            try:
                if sel.is_element_present("link=report"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=report"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=report")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if sel.is_text_present("qualitio report"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "qualitio: report" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertEqual("qualitio: report", sel.get_title())
        try: self.failUnless(sel.is_text_present("qualitio report"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=BigProject"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=BigProject"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=BigProject")
        for i in range(60):
            try:
                if sel.is_element_present("//div[@id='application-view-footer']/div/a[2]/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//div[@id='application-view-footer']/div/a[2]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//div[@id='application-view-footer']/div/a[2]/span")
        for i in range(60):
            try:
                if sel.is_text_present("report directory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("report directory"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("new"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_name", "Report directory")
        sel.select("id_parent", "label=---------")
        sel.type("id_description", "Description\nDescription")
        for i in range(60):
            try:
                if sel.is_element_present("Reportd"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("Reportd"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("Reportd")
        for i in range(60):
            try:
                if sel.is_element_present("link=Report directory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Report directory"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=Report directory")
        for i in range(60):
            try:
                if sel.is_text_present("report directory: Report directory"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("full name:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("report directory: Report directory"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("full name: /Report directory"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("description"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Description\nDescription"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("children:"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("id"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("path"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("name"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("modified"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("created"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("No data available in table"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("exact:Search:"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//input[@type='text']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//div[@id='application-view-footer']/div/a[1]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test44ReportReportCreate(BaseSeleniumTestCase):
    
    def test_44_report_report_create(self):
        self.login()
        sel = self.selenium
        sel.open("/require/")
        self.assertEqual("qualitio: requirements", sel.get_title())
        for i in range(60):
            try:
                if sel.is_element_present("link=report"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=report"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=report")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if sel.is_text_present("qualitio report"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "qualitio: report" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertEqual("qualitio: report", sel.get_title())
        try: self.failUnless(sel.is_text_present("qualitio report"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=BigProject"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=BigProject"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=BigProject")
        for i in range(60):
            try:
                if sel.is_element_present("//div[@id='application-view-footer']/div/a[2]/span"): break
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
                if sel.is_text_present("report directory: BigProject"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//div[@id='application-view-footer']/div/a[2]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//div[@id='application-view-footer']/div/a[1]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//div[@id='application-view-footer']/div/a[1]/span")
        for i in range(60):
            try:
                if sel.is_text_present("report"): break
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
        try: self.failUnless(sel.is_text_present("report"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("new"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_name", "report testcases")
        sel.type("id_context-0-name", "TESTCASES")
        sel.type("id_context-0-query", "TestCase.all()")
        sel.type("id_template", "<h1>Testcases</h1> <br/> {% for testcase in TESTCASES %} <h2>{{testcase.name}}</h2> <ul>     <li><b>name</b>: {{testcase.name}}</li>     <li><b>path</b>: {{testcase.path}}</li>     <li><b>requirement</b>: {{testcase.requirement.name|default:'empty'}}</li> </ul> <hr/> <br/> {% endfor %}")
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='Save']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='Save']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='Save']")
        for i in range(60):
            try:
                if sel.is_element_present("//li[@id='1_reportdirectory']/ins"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=report testcases"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("report testcases"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=report testcases")
        for i in range(60):
            try:
                if sel.is_text_present("exact:report: report testcases"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("path: /BigProject/"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("name: report testcases"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("exact:report: report testcases"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("path: /BigProject/"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("name: report testcases"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("format: text/html"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("link: http://"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("public: no"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Testcases"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Close navigation"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Open navigation"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase10"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase11"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase12"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase13"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase14"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase2"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase3"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase4"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase5"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase6"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase7"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase8"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("TestCase9"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test45ReportCreatedandDeleted(BaseSeleniumTestCase):

    
    def test_45_report_createdand_deleted(self):
        self.login()
        sel = self.selenium
        sel.open("/require/")
        sel.click("link=report")
        sel.wait_for_page_to_load("30000")
        sel.click("link=BigProject")
        for i in range(60):
            try:
                if sel.is_element_present("css=h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("create report"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=span.ui-button-text")
        for i in range(60):
            try:
                if sel.is_element_present("css=h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("css=h1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("report"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("id_parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_parent"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("--------- 1: /BigProject 2: /Report directory"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Name"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='report_form']/div[2]/div[2]/label"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_name"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Format"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='report_form']/div[2]/div[3]/label"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("html xml json plain"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Link"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_link"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Public"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//form[@id='report_form']/div[2]/div[5]/label"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", sel.get_value("id_public"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=#template > label"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Template"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div.ace_layer.ace_gutter-layer"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("exact:Context:"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=#context > label"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_context-0-name"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("//input[@id='id_name']", "Test Selenium")
        sel.type("id_template", "<ul> {%for require in allrequires%}     <li> {{require.name}} </li> {% endfor %} </ul>")
        sel.type("id_context-0-name", "allrequires")
        sel.type("id_context-0-query", "Requirement.all()")
        sel.click("//input[@value='Save']")
        for i in range(60):
            try:
                if sel.is_element_present("link=Test Selenium"): break
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
                if sel.is_element_present("css=span.name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("details"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("edit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=edit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=span.active"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("exact:path:"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("/BigProject/"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("exact:name:"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("List of Requirement"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("exact:format:"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("text/html"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("exact:link:"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("exact:public:"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("no"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div.content > ul > li"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div.content > ul > li:nth(1)"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Notebook"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div.content > ul > li:nth(2)"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("IVI"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=admin")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Reports")
        sel.wait_for_page_to_load("30000")
        sel.click("//input[@name='_selected_action' and @value='5']")
        sel.select("action", "label=Delete selected reports")
        sel.click("index")
        sel.wait_for_page_to_load("30000")
        sel.click("css=input[type=submit]")
        sel.wait_for_page_to_load("30000")


if __name__ == "__main__":
    unittest.main()
