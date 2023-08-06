from threading import local
from dotenv import load_dotenv
load_dotenv()
from circles_local_database_python.database import database 
from logger_local.LoggerLocal import logger_local
import random 
import sys

class NumberGenerator:
    
    def __init__(self, schema, table):
        self.schema = schema
        self.table = table

    def db_connection(self):
        # Connect to the MySQL database
        database_conn = database()
        db = database_conn.connect_to_database()
        db.database = self.schema 
        return db

    def get_random_number(self):
        logger_local.init(object = {"component_name": "database-infrastructure-local-python-package"})
        
        logger_local.info("Starting random number generator...")
        conn = self.db_connection()
        cursor = conn.cursor()

        successful = False

        while not successful:
            number = random.randint(1, sys.maxsize)
            logger_local.info(object = {"Random number generated": str(number)})

            cursor.execute("SELECT id FROM %s WHERE `number` = %s" % (self.table, number))
            if cursor.fetchone() == None:
                successful = True
                logger_local.info("Number does not already exist in database")

        return number 
