#!/usr/local/bin/python
# -*- coding: utf-8 -*- 

'''Testing the functionality of the db module.'''

import sqlite3
import unittest
from pyspend import db

DB = 'test.sqlite'

class TestDB(unittest.TestCase):
    def setUp(self):
        self.conn = db.PySpendDB(DB)
        
    def tearDown(self):
        self.conn.close()
        
    def test_categories(self):
        cats = ('Test1', 'Test2', 'Test3', 'Test4')
        for (id, cat), cat_test in zip(self.conn.categories(), cats):
            self.assertEqual(cat, cat_test)
            
    def test_category_exists(self):
        self.assertTrue(self.conn.category_exists('Test1'))
        
    def test_category_not_exists(self):
        self.assertFalse(self.conn.category_exists('Test12'))
            
    def test_category_used(self):
        self.assertTrue(self.conn.category_used(1))
        
    def test_category_not_used(self):
        self.assertFalse(self.conn.category_used(4))
        
    def test_get_catid(self):
        categories = (
            ('Test1', 1),
            ('Test2', 2),
            ('Test3', 3),
            ('Test4', 4),
        )
        for cat, id in categories:
            self.assertEqual(self.conn.get_catid(cat), id)

if __name__ == '__main__':
    unittest.main()