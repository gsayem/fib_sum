import uuid
from abc import ABC, abstractmethod

import pyodbc

from utility.app_constant import DATABASE_SERVER, DATABASE_NAME


# Database base class
class DatabaseBase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get(self, fib: int):
        pass

    @abstractmethod
    def save(self, fib: int, combination: str):
        pass


# MS Sql Data base
class MSSqlDatabase(DatabaseBase):
    def __init__(self):
        super().__init__()

    def connect(self):
        conn = None
        try:
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + DATABASE_SERVER +
                                  ';DATABASE=' + DATABASE_NAME +
                                  ';Trusted_Connection=yes')
            print("Successfully connected to MSSQL database!")
        except Exception as e:
            print("Database not connected!")
            print(e)

        return conn

    def get_all(self):
        result = []
        try:
            conn = self.connect()
            cursor = conn.cursor()
            columns = ['id', 'fib', 'combination']
            data = cursor.execute('SELECT id, fib,combination FROM FibSumCombination').fetchall()
            for row in data:
                result.append(dict(zip(columns, row)))

        except Exception as e:
            print("Can't retrieve data")
            print(e)
        return result

    def get(self, fib: int):
        result = []
        try:
            conn = self.connect()
            cursor = conn.cursor()
            columns = ['id', 'fib', 'combination']
            data = cursor.execute('SELECT id, fib,combination FROM FibSumCombination WHERE fib=?', fib)

            for row in data:
                result.append(dict(zip(columns, row)))

        except Exception as e:
            print("Can't retrieve data")
            print(e)

        return result

    def save(self, fib: int, combination: str):
        # FibSumCombination
        try:
            conn = self.connect()
            cursor = conn.cursor()
            data = cursor.execute('SELECT * FROM FibSumCombination WHERE fib=?', fib).fetchone()
            if data is None:
                cursor.execute('INSERT INTO FibSumCombination VALUES (?,?,?)', (str(uuid.uuid4()), fib, combination))
                cursor.close()
                conn.commit()
                conn.close()
            else:
                print("Do not need to insert; Data found in DB")
        except pyodbc.Error as e:
            print("Can't insert data")
            print(e)
        except Exception as e:
            print("Can't insert data")
            print(e)
