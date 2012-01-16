#!/usr/local/bin/python
# -*- coding: utf-8 -*- 

from __future__ import division
import os
import sqlite3

#DB = 'pyspend.sqlite'

def connect(source):
    return PySpendDB(source)

class PySpendDB(object):
    def __init__(self, source):
        self.source = source
        self.conn = self._connect()

    def _connect(self):
        if os.path.exists(self.source):
            return sqlite3.connect(self.source)
        else:
            return self._make_db()

    def _make_db(self):
        conn = sqlite3.connect(self.source)
        categories = """CREATE TABLE categories (catID INTEGER PRIMARY KEY ASC,
                    name TEXT NOT NULL);"""
        items = """CREATE TABLE items (itemID INTEGER PRIMARY KEY ASC,
                    catID INTEGER NOT NULL, name TEXT NOT NULL, cost REAL,
                    costp INTEGER, purchase_date date,
                    FOREIGN KEY (catID) REFERENCES categories(catID));"""
        conn.execute(categories)
        conn.execute(items)
        conn.commit()
        return conn
        
    def categories(self):
        """Categories generator."""
        sql = 'SELECT catID, name FROM categories ORDER BY name'
        return self._select(sql)
        
    def new_category(self, name):
        sql = 'INSERT INTO categories (name) VALUES (?)'
        self._modify(sql, (name, ))
        
    def category_exists(self, name):
        sql = 'SELECT name FROM categories WHERE name = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (name, ))
        return cur.fetchone() is not None
        
    def category_used(self, cat_id):
        '''Is the category being used in a items record.'''
        sql = 'SELECT COUNT(*) FROM items WHERE catID = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (cat_id, ))
        return cur.fetchone()[0] != 0
        
    def delete_category(self, cat_id):
        sql = 'DELETE FROM categories WHERE catID = ?'
        self._modify(sql, (cat_id, ))
        
    def get_catid(self, category):
        sql = 'SELECT catID FROM categories WHERE name = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (category, ))
        return cur.fetchone()[0]
        
    def day_items(self, purchase_date):
        sql = '''SELECT itemID, categories.name, items.name, costp FROM items
                 LEFT JOIN categories ON items.catID = categories.catID
                 WHERE purchase_date = ?'''
        return self._select(sql, (purchase_date, ))
        
    def new_item(self, cat_id, name, cost, date):
        sql = '''INSERT INTO items (catID, name, cost, costp, purchase_date)
                 VALUES (?, ?, ?, ?, ?)'''
        self._modify(sql, (cat_id, name, cost/100, cost, date))
        
    def delete_item(self, item_id):
        sql = 'DELETE FROM items WHERE itemID = ?'
        self._modify(sql, (item_id, ))
            
    def year_months(self):
        """Generator for year-month data in format '2010-11', for all months
        in the database."""
        sql = """SELECT DISTINCT strftime('%Y-%m', purchase_date) AS year_month
                 FROM items
                 ORDER BY year_month ASC"""
        for year_month in self.conn.execute(sql):
            yield year_month[0]
            
    def new_record(self, data):
        """Add a new record to the database.
            data: a tuple (category, name, costp, purchase_date)"""
        sql = "SELECT catID FROM categories WHERE name = ?;"
        catID = self.conn.execute(sql, (data[0],)).fetchone()
        insert_data = catID + data[1:]
        sql = """INSERT INTO items (catID, name, cost, costp, purchase_date)
                VALUES (?, ?, ?, ?, ?);"""
        self.conn.execute(sql, insert_data)
        self.conn.commit()
        
    def _select(self, sql, params=()):
        for row in self.conn.execute(sql, params):
            yield row
            
    def _modify(self, sql, params=()):
        self.conn.execute(sql, params)
        self.conn.commit()