import os
from promptflow.connections import CustomConnection
from oracle.tools.query import run_query
from dotenv import load_dotenv
load_dotenv()

def test_run_single_query():
    con = CustomConnection(
        {
            "user": os.environ.get('ORACLE_USER'),
            "password": os.environ.get('ORACLE_PASSWORD'),
            "dsn": os.environ.get('ORACLE_CONNECT_STRING')
        }
    )
    result = run_query(con, query="SELECT * FROM CUSTOMERS WHERE CUSTOMER_ID = :id", 
                       params={ "id": 6 })
    
    assert len(result) == 1

def test_run_multiple_query():
    con = CustomConnection(
        {
            "user": os.environ.get('ORACLE_USER'),
            "password": os.environ.get('ORACLE_PASSWORD'),
            "dsn": os.environ.get('ORACLE_CONNECT_STRING')
        }
    )
    result = run_query(con, query="SELECT * FROM CUSTOMERS WHERE MEMBERSHIP = :membership", 
                       params={ "membership": "Base" })
    
    assert len(result) == 6