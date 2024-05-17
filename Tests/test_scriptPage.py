from Config.TestData import TestData, TestDataTestScript
from Pages.DORPage import DOR
from Pages.TestScriptPage import TestScript
from Tests.test_base import BaseTest
import pytest

class Test_Script(BaseTest):
    obj=TestDataTestScript()


    @pytest.fixture(params=obj.Links())
    def url(self, request):
        return request.param


    def test_get_text1(self):
        self.testScript = TestScript(self.driver)
        l = list()
        l = self.obj.Links()
        for x in range(len(l)):
            self.testScript.run_tests(l[x])






