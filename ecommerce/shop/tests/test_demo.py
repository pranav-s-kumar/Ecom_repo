from django.test import TestCase

def demo(str1, str2):
    return str1 + str2

class TestStr(TestCase):
    def test_concatenate(self):
        self.assertEqual(demo('hello','world'),'helloworld')
