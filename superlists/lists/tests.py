from django.test import TestCase

class SmokeTest(TestCase):

    def test_dad_maths(self):
        self.assertEqual(1 + 1, 3)