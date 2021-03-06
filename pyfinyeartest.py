import unittest
import datetime
import pyfinyear

class MyTestCase(unittest.TestCase):
    def test_fin_year_before_and_after_newyear(self):
        inst= datetime.date( day=1, month=3, year=2016)
        newYearIsFeb=2
        newYearIsApril=4
        self.assertEqual(1, inst.day)
        self.assertEqual("15/16", pyfinyear.finyear(newYearIsApril, inst))
        self.assertEqual("16/17", pyfinyear.finyear(newYearIsFeb, inst))

if __name__ == '__main__':
    unittest.main()
