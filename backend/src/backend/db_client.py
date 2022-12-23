"""
Client to access a MySQL database.
"""

import os
from pathlib import Path
from typing import List

import mysql.connector
from backend.dataclasses import User, Measurement
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).parent.parent.parent.parent / '.env')


class DbClient(object):

    def __init__(self,
                 db_host: str = os.getenv('MYSQL_HOSTNAME'),
                 db_port: str = os.getenv('MYSQL_PORT'),
                 db_user: str = os.getenv('MYSQL_ROOT_USER'),
                 db_password: str = os.getenv('MYSQL_ROOT_PASSWORD'),
                 db_schema: str = os.getenv('MYSQL_DATABASE')):
        """
        Returns a new Score & Protect database client instance.

        Args:
            db_host (str): MySQL database hostname. If None, use MYSQL_HOSTNAME environment variable is used.
            db_port (str): MySQL database port. If None, use MYSQL_PORT environment variable is used.
            db_user (str): MySQL user name. If None, use MYSQL_ROOT_USER environment variable is used.
            db_password (str): MySQL user password. If None, use MYSQL_ROOT_PASSWORD environment variable is used.
            db_schema (str): MySQL database schema. If None, use MYSQL_DATABASE environment variable is used.

        Returns: ('DbClient') a new client instance.
        """
        self.cnx = mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_schema,
            port=db_port
        )
        self.cnx.ping()

    def _execute_select_query(self, query: str) -> List[dict]:
        """
        Executes a SELECT query and returns the result as a pandas DataFrame.

        Args:
            query (str): MySQL SELECT query

        Returns: (List[NamedTuple]) query result
        """
        cursor = self.cnx.cursor()
        cursor.execute(query)
        output = [
            {col: value for col, value in zip(cursor.column_names, row)}
            for row in cursor
        ]
        cursor.close()
        return output

    def fetch_users(self) -> List[User]:
        """
        Fetch users from database.

        Returns: (List[User]) a list of users
        """
        query = \
            """
            SELECT 
                U.id AS user_id,  
                U.username AS user_name 
            FROM users AS U 
            ORDER BY user_id
            """

        return [User(**item) for item in self._execute_select_query(query=query)]

    def fetch_user_measurements(self, user_id: int) -> List[Measurement]:
        """
        Fetch some measurements for a given user.

        Args:
            user_id (str): user id

        Returns: (List[Measurement]) a list of measurements
        """

        query = \
            f"""
            SELECT
                M.id as measurement_id,
                M.type as measurement_type,
                M.value as measurement_value
            FROM measurements AS M
            WHERE M.user_id={user_id}
            """

        return [Measurement(**item) for item in self._execute_select_query(query=query)]
