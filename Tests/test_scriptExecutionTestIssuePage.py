from Config.TestData import TestExecutionData, TestExecutionTestIssueKey
from Pages.DORPage import DOR
from Pages.TestExecutionTestIssuePage import TESTSCRIPTEEXECUTIONTESTISSUE
from Pages.TestScriptPage import TESTSCRIPT
from Tests.test_base import BaseTest
import pytest

class Test_testScipt(BaseTest):
    obj=TestExecutionTestIssueKey()


    """@pytest.fixture(params=obj.Links())
    def url(self, request):
        return request.param"""""


    def test_get_text1(self):
        self.testScript = TESTSCRIPTEEXECUTIONTESTISSUE(self.driver)
        l = list()
        l = self.obj.Links()
        for x in range(len(l)):
            self.testScript.run_tests(l[x])






