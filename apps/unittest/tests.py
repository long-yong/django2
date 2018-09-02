from django.test import TestCase
# run unittest: python manage.py test apps.unittest
# https://blog.csdn.net/hjd199464/article/details/71210255

def isPalindrome(str):
    L = len(str)
    for i in range(int(L / 2)):
        if str[i] != str[L - 1 - i]:
            return False
    return True

class isPalindromeTest(TestCase):
    def test01(self): return self.assertEqual(isPalindrome('racecar'), True)
    def test02(self): return self.assertEqual(isPalindrome('rabbit'),  False)
    def test03(self): return self.assertEqual(isPalindrome('abcde'),   False)
    def test04(self): return self.assertEqual(isPalindrome('abcba'),   True)
    def test05(self): return self.assertEqual(isPalindrome('abcd'),    False)
    def test06(self): return self.assertEqual(isPalindrome('abba'),    True)
    def test07(self): return self.assertEqual(isPalindrome('123'),     False)
    def test08(self): return self.assertEqual(isPalindrome('121'),     True)
    def test09(self): return self.assertEqual(isPalindrome('12'),      False)
    def test10(self): return self.assertEqual(isPalindrome('11'),      True)
    def test11(self): return self.assertEqual(isPalindrome('a'),       True)
    def test12(self): return self.assertEqual(isPalindrome(''),        True)
    def setUp(self): print("isPalindrome-setup")
    def tearDown(self): print("isPalindrome-teardown")
