#!/usr/local/bin/python
# -*- coding: utf-8 -*-

'''Testing the functionality of the db module.'''

import os
import sqlite3
import unittest
from pyspend import db

DB = 'test.sqlite'

SQL = '''
CREATE TABLE categories (catID INTEGER PRIMARY KEY ASC, name TEXT NOT NULL);
CREATE TABLE items (itemID INTEGER PRIMARY KEY ASC,
    catID INTEGER NOT NULL, name TEXT NOT NULL, cost REAL, costp INTEGER,
    purchase_date date, FOREIGN KEY (catID) REFERENCES categories(catID));
'''

INSERT_CATS = 'INSERT INTO categories (name) VALUES (?)'

INSERT_ITEMS = '''
INSERT INTO items (catID, name, cost, costp, purchase_date)
VALUES (?, ?, ?, ?, ?)
'''

CATEGORIES = (
    (1, 'Sport'),
    (2, 'Food'),
    (3, 'Utilities'),
    (4, 'Misc'),
)

SORTED_CATS = sorted(CATEGORIES, key=lambda x: x[1])

ITEMS = (
    (1, 'swim', 3.00, 300, '2012-01-12'),
    (1, 'swim', 3.00, 300, '2012-01-12'),
)

def create_db():
    try:
        os.remove(DB)
    except OSError:
        pass
    conn = sqlite3.connect(DB)
    conn.executescript(SQL)
    conn.commit()
    conn.executemany(INSERT_CATS, [(cat[1], ) for cat in CATEGORIES])
    conn.commit()
    conn.executemany(INSERT_ITEMS, ITEMS)
    conn.commit()
    conn.close()

class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.conn = db.PySpendDB(DB)

    def tearDown(self):
        self.conn.close()

class TestDB(TestTemplate):
    def test_categories(self):
        for (id, cat), (id_test, cat_test) in zip(self.conn.categories(), SORTED_CATS):
            self.assertEqual(cat, cat_test)

    def test_category_exists(self):
        cat = CATEGORIES[0][1]
        self.assertTrue(self.conn.category_exists(cat))

    def test_category_not_exists(self):
        self.assertFalse(self.conn.category_exists('Test12'))

    def test_category_used(self):
        self.assertTrue(self.conn.category_used(1))

    def test_category_not_used(self):
        self.assertFalse(self.conn.category_used(4))

    def test_get_catid(self):
        for id, cat in CATEGORIES:
            self.assertEqual(self.conn.get_catid(cat), id)

    def test_cat_objects(self):
        for (id, name), cat_obj in zip(SORTED_CATS, self.conn.category_objects()):
            self.assertEqual(id, cat_obj.id)
            self.assertEqual(name, cat_obj.name)

class TestDelete(TestTemplate):
    def test_delete_category(self):
        # delete (4, 'Misc') category
        self.conn.delete_category(4)
        self.assertFalse(self.conn.category_exists('Misc'))

if __name__ == '__main__':
    create_db()
    tests = (TestDB, TestDelete)
    loader = unittest.TestLoader()
    suites = unittest.TestSuite([loader.loadTestsFromTestCase(s) for s in tests])
    unittest.TextTestRunner(verbosity=2).run(suites)