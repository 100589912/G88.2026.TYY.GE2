from unittest import TestCase

from uc3m_consulting import EnterpriseManager, EnterpriseManagementException

class TestRF1(TestCase):

    def test_TC1(self):
        o = EnterpriseManager()
        result = o.register_project('B12345678','PRO01','valid text','HR','18/02/2026',100000.00)
        print("TC1:", result)
        self.assertEqual(result, "")

    def test_TC2(self):
        o = EnterpriseManager()
        result = o.register_project('B12345678','PRO012','Valid project name is longerr','FINANCE','31/12/2025',999999.99)
        print("TC2:", result)
        self.assertEqual(result, "")

    def test_TC3(self):
        o = EnterpriseManager()
        result = o.register_project('B12345679','PRO012345','Valid project name is longerrr','LEGAL','30/11/2025',50000.00)
        print("TC3:", result)
        self.assertEqual(result, "")

    def test_TC4(self):
        o = EnterpriseManager()
        result = o.register_project('B12345680','PRO0123456','valid proje','LOGISTICS','02/01/2025',50000.01)
        print("TC4:", result)
        self.assertEqual(result, "")