from Config.TestData import  TestScriptData
from Pages.DORPage import DOR
from Pages.TestScriptPage import TESTSCRIPT
from Tests.test_base import BaseTest
import pytest

class Test_testScipt(BaseTest):
    obj=TestScriptData()


    """@pytest.fixture(params=obj.Links())
    def url(self, request):
        return request.param"""""


    def test_get_text1(self):
        self.testScript = TESTSCRIPT(self.driver)
        l = list()
        l = self.obj.Links()
        for x in range(len(l)):
            self.testScript.run_tests(l[x])






