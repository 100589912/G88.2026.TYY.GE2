import unittest
from unittest import TestCase

from uc3m_consulting import EnterpriseManager, EnterpriseManagementException

class TestRF1(TestCase):

        def test_TC1(self):
            o = EnterpriseManager()
            result = o.register_project('B12345674', 'PRO01', 'valid proj', 'HR', '1/2/2026', 100000.00)
            print("TC1:", result)
            #self.assertEqual(result, "02c7ef9cceb0cb84004a45a5aa029c71")

        def test_TC2(self):
            o = EnterpriseManager()
            result = o.register_project('B12345674', 'PRO012', 'Valid project name is longerr', 'FINANCE', '31/12/2025',
                                        999999.99)
            print("TC2:", result)
            # self.assertEqual(result, "")

        def test_TC3(self):
            o = EnterpriseManager()
            result = o.register_project('B12345674', 'PRO012345', 'Valid project name is longerrr', 'LEGAL',
                                        '30/11/2025', 50000.00)
            print("TC3:", result)
            # self.assertEqual(result, "")

        def test_TC4(self):
            o = EnterpriseManager()
            result = o.register_project('B12345682', 'PRO0123456', 'valid proje', 'LOGISTICS', '2/1/2025', 50000.01)
            print("TC4:", result)
            # self.assertEqual(result, "")
        def test_TC5(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong CIF value"):
                o.register_project(987654321, 'PRO01', 'valid project name', 'HR', '18/2/2026', 100000.00)

        def test_TC6(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong CIF value"):
                o.register_project('A123654B', 'PRO01', 'valid project name', 'HR', '18/2/2026', 100000.00)

        def test_TC7(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong CIF value"):
                o.register_project('A12345690BC', 'PRO01', 'valid project name', 'HR', '18/2/2026', 100000.00)

        def test_TC8(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong CIF value"):
                o.register_project('11234567B', 'PROJ1', 'valid project name', 'HR', '18/2/2026', 100000.00)

        def test_TC9(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong CIF value"):
                o.register_project('A12X4567B', 'PROJ1', 'valid project name', 'HR', '18/2/2026', 100000.00)

        def test_TC10(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong CIF value"):
                o.register_project('A1234567Z', 'PROJ1', 'valid project name', 'HR', '18/2/2026', 100000.00)

        def test_TC11(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong CIF value"):
                o.register_project('B1234567A', 'PROJ1', 'valid project name', 'HR', '18/2/2026', 100000.00)

        def test_TC12(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong project acronym value"):
                o.register_project('B12345674', 12345, 'valid project name', 'HR', '18/2/2026', 100000.00)

        def test_TC13(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong project acronym value"):
                o.register_project('B12345674', 'ABC1', 'valid project name', 'HR', '18/2/2026', 100000.00)

        def test_TC14(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong project acronym value"):
                o.register_project('B12345674', 'ABCDE123456', 'valid project name', 'HR', '18/2/2026', 100000.00)

        def test_TC15(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong project acronym value"):
                o.register_project('B12345674', 'ABCDE123$%!', 'valid project name', 'HR', '18/2/2026', 100000.00)

        def test_TC16(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong operation name value"):
                o.register_project('B12345674', 'ABCDE12345', 90.9, 'HR', '18/2/2026', 100000.00)

        def test_TC17(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong operation name value"):
                o.register_project('B12345674', 'PRO01', 'sshorterr', 'HR', '18/2/2026', 100000.00)

        def test_TC18(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong operation name value"):
                o.register_project('B12345674', 'PRO01', 'descripti is longer than thirty', 'HR', '18/2/2026',
                                   100000.00)

        def test_TC19(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong department value"):
                o.register_project('B12345674', 'PRO01', 'valid project name', 123, '18/2/2026', 100000.00)

        def test_TC20(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong department value"):
                o.register_project('B12345674', 'PRO01', 'valid project name', 'OTHER', '18/2/2026', 100000.00)

        def test_TC21(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong date value"):
                o.register_project('B12345674', 'PRO01', 'valid project name', 'HR', 1922026, 100000.00)

        def test_TC22(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong date value"):
                o.register_project('B12345674', 'PRO02', 'valid project name', 'HR', '19/0/2026', 100000.00)

        def test_TC23(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong date value"):
                o.register_project('B12345674', 'PRO03', 'valid project name', 'HR', '19/-1/2027', 100000.00)

        def test_TC24(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong date value"):
                o.register_project('B12345674', 'PRO01', 'valid project name', 'HR', '32/01/2025', 100000.00)

        def test_TC25(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong date value"):
                o.register_project('B12345674', 'PRO01', 'valid project name', 'HR', '01/00/2025', 100000.00)

        def test_TC26(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong date value"):
                o.register_project('B12345674', 'PRO01', 'valid project name', 'HR', '01/-1/2026', 100000.01)

        def test_TC27(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong date value"):
                o.register_project('B12345674', 'PRO01', 'valid project name', 'HR', '01/13/2025', 100000.00)

        def test_TC28(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong date value"):
                o.register_project('B12345674', 'PRO01', 'valid project name', 'HR', '01/01/2027', 100000.00)

        def test_TC29(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong date value"):
                o.register_project('B12345674', 'PRO01', 'valid project name', 'HR', '01/01/2024', 100000.00)

        def test_TC30(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong date value"):
                o.register_project('B12345674', 'PRO01', 'valid project name', 'HR', '01/01/2028', 100000.00)

        def test_TC31(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong budget value"):
                o.register_project('B12345674', 'PRO01', 'valid project name', 'HR', '01/01/2025', 'abc')

        def test_TC32(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong budget value"):
                o.register_project('B12345674', 'PRO01', 'valid project name', 'HR', '01/01/2025', 100000)

        def test_TC33(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong budget value"):
                o.register_project('B12345674', 'PRO01', 'valid project name', 'HR', '01/01/2025', 49999.99)

        def test_TC34(self):
            o = EnterpriseManager()
            with self.assertRaisesRegex(EnterpriseManagementException, "Wrong budget value"):
                o.register_project('B12345674', 'PRO01', 'valid project name', 'HR', '01/01/2025', 1100000.00)

        def test_TC35(self):
            o = EnterpriseManager()
            result = o.register_project('B12345674', 'PRO01', 'valid project name', 'HR', '01/01/2025', 100000.00)
            self.assertIsInstance(result, str)
            self.assertRegex(result, r'^[a-f0-9]{32}$')

if __name__ == '__main__':
    unittest.main(verbosity=2)