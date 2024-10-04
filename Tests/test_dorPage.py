from Config.TestData import TestData
from Pages.DORPage import DOR
from Tests.test_base import BaseTest
import pytest

class Test_dor(BaseTest):
    obj=TestData()
    x=obj.Links()
    print(x)



    """@pytest.fixture(params=obj.Links())
    def url(self, request):
        return request.param"""

    """def test_get_text1(self, obj, url):
        self.dor = DOR(self.driver)
        self.dor.run_tests(url)"""

    def test_get_text1(self):
        self.dor = DOR(self.driver)
        l = list()
        l = self.obj.Links()
        print("data",l)
        print("len" ,len(l))
        for x in range(len(l)):
            self.dor.run_tests(l[x])






