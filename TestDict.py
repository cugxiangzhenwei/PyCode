#!/usr/bin/env pyhton
import unittest
class TestDict(unittest.TestCase):
    def setUp(self):
        print 'setUp...'
    def tearDown(self):
        print 'tearDown...'
    def test_init(self):
        self.assertTrue(isinstance(self, object))
    def test_key(self):
        self.assertTrue(isinstance('232', object))

if __name__ == '__main__':
    unittest.main()
