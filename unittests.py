from check_mail import check_email
import unittest

class TestMyFunc(unittest.TestCase):
    def testMailMethod(self):
        self.assertTrue(check_email('vasya@yandex'))
        self.assertTrue(check_email('vasya123@yan-dex'))
        self.assertTrue(check_email('123va32ysa@_yan3-31ex'))
        self.assertTrue(check_email('va"!"y.sa@12yandex'))
        self.assertTrue(check_email('va.ysa@yande-x'))
        self.assertTrue(check_email('vay"!,:"sa@_yandex'))
        self.assertTrue(check_email('vay":,!"sa@yande-x'))

if __name__=='__main__':
    unittest.main(exit=False)
