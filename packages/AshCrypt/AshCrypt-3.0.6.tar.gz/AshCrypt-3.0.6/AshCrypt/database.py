"""Module to interact with an SQLite database"""

from dataclasses import dataclass, field
from typing import Union, Generator
from datetime import datetime
import sqlite3
import os


@dataclass
class Database:
    """
    Represents a simple SQLite database wrapper with various methods to interact with the database.
    """
    dbname: str = field()
    tablename: str = field(default='Classified')
    conn: sqlite3.Connection = field(init=False, repr=False)
    c: sqlite3.Cursor = field(init=False, repr=False)

    def __post_init__(self):
        self.conn = sqlite3.connect(self.dbname)
        self.c = self.conn.cursor()

    @property
    def size(self) -> Union[int, tuple]:
        """Returns the database size in MB"""
        try:
            with self.conn:
                self.c.execute(
                    'SELECT page_count * page_size FROM pragma_page_count() , pragma_page_size')
                size_info = self.c.fetchone()
                size = size_info[0] / 1024 / 1024
                return size
        except sqlite3.Error as e:
            return -1, e

    @property
    def last_mod(self) -> Union[datetime, tuple]:
        """Returns the last time the Database has been altered with"""
        try:
            time_stat = datetime.fromtimestamp(os.stat(self.dbname).st_mtime)
            return time_stat

        except OSError as e:
            return 0, e

    @property
    def default_routing(self) -> str:
        """Get the default routing information of the Database class."""
        return f'DEFAULT ROUTING ALL METHODS TO "{self.tablename}"'

    def query(self, *querys: str) -> list:
        """Executes one or more SQL queries and return the results.
           Provides feedback on whether each given query ran successfully or not.
           Also provides where the Error has occurred and what type of Error it is."""
        result = []
        for i, query in enumerate(querys):
            if not isinstance(query, str):
                result.append({f'query {i}': (-1, TypeError)})
            try:
                with self.conn:
                    self.c.execute(query)
                    if self.c.rowcount == 1:
                        result.append(
                            {f'query {i}': ['SUCCESS', self.c.fetchone()]})
                    else:
                        result.append(
                            {f'query {i}': ['SUCCESS', self.c.fetchall()]})

            except sqlite3.Error as e:
                result.append({f'query {i}': ('FAILURE', e.__str__())})
        return result

    def addtable(self, optional_tablename=None) -> Union[int, tuple]:
        """Creates a new table in the database with the given table name.
        If the table name is not provided, it uses the default table name  : 'Classified'."""
        if optional_tablename is None:
            try:
                with self.conn:
                    self.c.execute(
                        f"CREATE TABLE IF NOT EXISTS {self.tablename} "
                        "(ID INTEGER PRIMARY KEY, Name Text , Content BLOB ,Key TEXT )")
                return 11
            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self.conn:
                    self.c.execute(
                        f"CREATE TABLE IF NOT EXISTS {optional_tablename} "
                        "(ID INTEGER PRIMARY KEY,"
                        "Name TEXT ,"
                        "Content BLOB ,"
                        "Key TEXT )")
                    self.tablename = optional_tablename
                return 1

            except sqlite3.Error as e:
                return 0, e

    def insert(self, name, content, key,
               optional_table_name=None) -> Union[int, tuple]:
        """Inserts a new row into the specified table or the default table."""
        if optional_table_name is None:
            try:
                with self.conn:
                    self.c.execute(
                        f"INSERT INTO {self.tablename} (Name , Content ,Key) VALUES (? , ? , ?) ",
                        (name,
                         content,
                         key))

                return 11
            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self.conn:
                    self.c.execute(
                        f"INSERT INTO {optional_table_name} (Name, Content ,Key) VALUES (? , ? , ?) ",
                        (name,
                         content,
                         key))
                return 1
            except sqlite3.Error as e:
                return 0, e

    def update(
            self,
            column_name: str,
            new_column_val: str,
            idd: int,
            optional_table_name=None) -> Union[int, tuple]:
        """Updates a specific column of a row based on the given ID in the specified table or the default table."""
        if optional_table_name is None:
            try:
                with self.conn:
                    self.c.execute(
                        f'UPDATE {self.tablename} SET {column_name} = ? WHERE ID = ? ',
                        (new_column_val,
                         idd))
                    return 11

            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self.conn:
                    self.c.execute(
                        f'UPDATE {optional_table_name} SET {column_name} = ? WHERE ID = ? ',
                        (new_column_val,
                         idd))
                    return 1

            except sqlite3.Error as e:
                return 0, e

    def content(self, optional_tablename=None) -> Union[Generator, tuple]:
        """Yields all rows from the specified table or the default table
         ( as a Generator object ) ."""
        if optional_tablename is None:
            try:
                with self.conn:
                    self.c.execute(f'SELECT * FROM {self.tablename} ')
                    for row in self.c.fetchall():
                        yield row

            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self.conn:
                    self.c.execute(f'SELECT * FROM {optional_tablename} ')
                    for row in self.c.fetchall():
                        yield row

            except sqlite3.Error as e:
                return 0, e

    def content_by_id(
            self, idd: int, optional_tablename=None) -> Union[Generator, tuple]:
        """Yields a specific row from the specified table or the default table based on a given ID.
        ( Generator object )"""
        if optional_tablename is None:
            try:
                with self.conn:
                    self.c.execute(
                        f'SELECT * FROM {self.tablename} WHERE ID = ? ', (idd,))
                    for row in self.c.fetchall():
                        yield row

            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self.conn:
                    self.c.execute(
                        f'SELECT * FROM {optional_tablename} WHERE ID = ? ', (idd,))
                    for row in self.c.fetchall():
                        yield row

            except sqlite3.Error as e:
                return 0, e

    def show_contents(self, *optional_tablenames) -> Union[Generator, tuple]:
        """Yields all rows from specified tables or the default table.
        ( Generator object )"""
        if optional_tablenames:
            try:
                for arg in optional_tablenames:
                    with self.conn:
                        self.c.execute(f'SELECT * FROM {arg} ')
                        for row in self.c.fetchall():
                            yield {arg: row}

            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self.conn:
                    self.c.execute(f'SELECT * FROM {self.tablename} ')
                    for row in self.c.fetchall():
                        yield {self.tablename: row}

            except sqlite3.Error as e:
                return 0, e

    def show_tables(self) -> Union[Generator, tuple]:
        """Yields the names of all tables in the Database. ( Generator object )"""
        try:
            with self.conn:
                self.c.execute(
                    "SELECT name FROM sqlite_master WHERE type= 'table' ")
                for row in self.c.fetchall():
                    yield row

        except sqlite3.Error as e:
            return 0, e

    def dropall(self) -> Union[int, tuple]:
        """Drops ALL tables in the Database."""
        try:
            with self.conn:
                self.c.execute(
                    "SELECT name FROM sqlite_master WHERE type= 'table' ")
                for table in self.c.fetchall():
                    self.c.execute(f'DROP TABLE {table[0]}')
                return 1

        except sqlite3.Error as e:
            return 0, e

    def drop_table(self, *table_names) -> Union[int, tuple]:
        """Drops a/many specific table(s) in the Database."""
        if table_names:
            try:
                for arg in table_names:
                    with self.conn:
                        self.c.execute(f"DROP TABLE {arg}")
                return 1
            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self.conn:
                    self.c.execute(f'DROP TABLE {self.tablename}')
                    return 1

            except sqlite3.Error as e:
                return 0, e

    def drop_content(self, idd, optional_table_name=None) -> Union[int, tuple]:
        """Deletes a row from the specified table or the default table based on the given ID."""
        if optional_table_name is None:
            try:
                with self.conn:
                    self.c.execute(
                        f'DELETE FROM {self.tablename} WHERE ID = {idd}')
                return 11

            except sqlite3.Error as e:
                return -1, e

        else:
            try:
                with self.conn:
                    self.c.execute(
                        f'DELETE FROM {optional_table_name} WHERE ID = {idd}')
                return 1

            except sqlite3.Error as e:
                return 0, e
