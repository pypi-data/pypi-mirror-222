# -*- coding: utf-8 -*-
"""
Test queries.
"""

import unittest

import pytest

from .helpers import pymssqlconn, drop_table


@pytest.mark.mssql_server_required
class TestQueryParameters(unittest.TestCase):

    table_name = 'testtab'

    @classmethod
    def setup_class(cls):
        cls.conn = pymssqlconn(encryption='as')
        drop_table(cls.conn, cls.table_name)
        cls.createTestTable()

    @classmethod
    def teardown_class(cls):
        drop_table(cls.conn, cls.table_name)
        cls.conn.close()

    @classmethod
    def createTestTable(cls):
        query = f"INSERT INTO {cls.table_name} (int_col, text_col) VALUES (%d, %s);"
        with cls.conn.cursor() as c:
            c.execute("""
                CREATE TABLE testtab (
                    int_col int,
                    text_col text
                )""")
            for x in range(10):
                c.execute(query, (x, f"Column {x}"))


    def test_609(self):
        with self.conn.cursor() as c:
            #c.execute('SELECT * FROM testtab WHERE int_col=%d', (1,))
            c.execute(f'SELECT * FROM {self.table_name} WHERE int_col=%d', (0, ))
            rows = c.fetchall()
            print(f"AAAAAAAAAAAAAAAAAAA: {rows}")
            self.assertEqual(len(rows), 1)
