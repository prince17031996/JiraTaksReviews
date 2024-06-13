from Config.TestData import TestData
from Pages.DORPage import DOR
from Tests.test_base import BaseTest
import pytest

class Test_dor(BaseTest):
    obj=TestData()


    """@pytest.fixture(params=obj.Links())
    def url(self, request):
        return request.param"""""


    def test_get_text1(self):
        self.dor = DOR(self.driver)
        l = list()
        l = self.obj.Links()
        for x in range(len(l)):
            self.dor.run_tests(l[x])






