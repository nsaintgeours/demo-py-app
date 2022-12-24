"""
Demo script for DbClient class.
"""
from backend.db_client import DbClient

# Connect to MySQL sample database
db_client = DbClient()
print(db_client.fetch_users())
print(db_client.fetch_user_measurements(user_id=1))
db_client.cnx.close()
