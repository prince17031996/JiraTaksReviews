from Config.TestData import TestData, TestDataTestScript, TestDataBug
from Pages.BugPage import BUG
from Pages.DORPage import DOR
from Tests.test_base import BaseTest
import pytest


# Test_Script class is inheriting the BaseTest class
class Test_Bug(BaseTest):
    obj = TestDataBug()


#TestScript is a class from TestScriptPage and we are creating instance for it to call the methods run_tests
    def test_get_text1(self):
        self.bug = BUG(self.driver)
        l = list()
        l = self.obj.Links()
        for x in range(len(l)):
            self.bug.run_tests(l[x])







