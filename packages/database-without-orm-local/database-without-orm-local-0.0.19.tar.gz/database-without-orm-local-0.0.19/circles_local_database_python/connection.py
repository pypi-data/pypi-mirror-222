import os
import mysql.connector
import sys
from dotenv import load_dotenv
load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, '..','circles_local_database_python')
sys.path.append(src_path)

from connection_cursor import DatabaseCursor
from logger_local.LoggerLocal import logger_local

class DatabaseFunctions:

    def __init__(self, database, arg1=None, arg2=None, arg3=None):
        self.host = arg1 if arg1 is not None else os.getenv("RDS_HOSTNAME")
        self.database = database
        self.user = arg2 if arg2 is not None else os.getenv("RDS_USERNAME")
        self.password = arg3 if arg3 is not None else os.getenv("RDS_PASSWORD")
        self.connection = None
        self.cursor = None
        self.stored_query = None

    def connect(self):
        try:
            logger_local.start("database-without-orm-local-python-package database.connect_to_database() " +
                               "host= " + self.host + " user= " + self.user)
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            self.cursor = DatabaseCursor(self.connection)
            logger_local.info(f"Successfully connected to the database for RDS_HOSTNAME={self.host} "
                              f"RDS_USERNAME={self.user}")
            logger_local.end(
                "database-without-orm-local-python-package database.connect_to_database()")
            return self.connection
        except Exception as e:
            st = str(os.getenv("RDS_HOSTNAME") + " " + os.getenv("RDS_USERNAME"))
            logger_local.exception(st, object=e)
            return None



    def execute(self, query):
        try:
            logger_local.start("database-without-orm-local-python-package database_functions.execute() "+"host= "+self.host+" user= "+self.user+" query="+query)
            if not self.connection or not self.connection.is_connected():
                self.connect()  # Connect if not already connected

            self.cursor.execute(query)
            result = self.cursor.fetchall() #for logger info
            self.stored_query = query
            logger_local.info(f"Query executed successfully for RDS_HOSTNAME={self.host} "
                        f"RDS_USERNAME={self.user} Query={query} Result={result}")
            return result
        except Exception as e:
            st = str(os.getenv("RDS_HOSTNAME") + " " + os.getenv("RDS_USERNAME"))
            logger_local.exception(st, object=e)
            return None  # Return None for result in case of an error
        finally:
            logger_local.end("database-without-orm-local-python-package database_functions.execute()")



    def fetchall(self):
        try:

            if self.stored_query is None:  # Check if the stored_query is valid
                raise ValueError("No query stored. Please execute a query before calling fetchall.")

            logger_local.start("database-without-orm-local-python-package database_functions.fetchall() "+"host= "+self.host+" user= "+self.user+" query="+self.stored_query)

            if not self.connection or not self.connection.is_connected():
                self.connect()  # Connect if not already connected

            self.cursor.execute(self.stored_query)
            result = self.cursor.fetchall()
            logger_local.info(f"Query fetched successfully for RDS_HOSTNAME={self.host} "
                        f"RDS_USERNAME={self.user}")
            logger_local.info("Result:")
            for row in result:
                logger_local.info(row)  # Log each row of the result
            return result
        except Exception as e:
            st = str(os.getenv("RDS_HOSTNAME") + " " + os.getenv("RDS_USERNAME"))
            logger_local.exception(st, object=e)
        finally:
            logger_local.end("database-without-orm-local-python-package database_functions.fetchall()")

    def fetchone(self):
        try:
            if self.stored_query is None:  # Check if the stored_query is valid
                raise ValueError("No query stored. Please execute a query before calling fetchone.")

            logger_local.start("database-without-orm-local-python-package database_functions.fetchone() "+"host= "+self.host+" user= "+self.user+" query="+self.stored_query)
            if not self.connection or not self.connection.is_connected():
                self.connect()  # Connect if not already connected

            self.cursor.execute(self.stored_query)
            result = self.cursor.fetchone()
            logger_local.info(f"Query fetched successfully for RDS_HOSTNAME={self.host} "
                        f"RDS_USERNAME={self.user}")
            logger_local.info("Result:")
            logger_local.info(result)  
            return result
        except Exception as e:
            st = str(os.getenv("RDS_HOSTNAME") + " " + os.getenv("RDS_USERNAME"))
            logger_local.exception(st, object=e)
        finally:
            logger_local.end("database-without-orm-local-python-package database_functions.fetchone()")


    def close(self):
        try:
            logger_local.start("database-without-orm-local-python-package database_functions.close() "+"host= "+self.host+" user= "+self.user)

            if self.connection:
                if self.connection.is_connected():
                    self.cursor.close()  # Close the cursor
                    self.connection.close()
                    logger_local.info(f"Connection closed successfully for "
                                f"RDS_HOSTNAME={self.host} RDS_USERNAME={self.user}")
                    # Set attributes to None after closing the connection
                    self.connection = None
                    self.cursor = None
                else:
                    logger_local.error(f"Connection is not connected for RDS_HOSTNAME={self.host}"
                                 f" RDS_USERNAME={self.user}")
            else:
                logger_local.error(f"No connection object found for RDS_HOSTNAME={self.host}"
                             f" RDS_USERNAME={self.user}")

        except Exception as e:
            st = str(os.getenv("RDS_HOSTNAME") + " " + os.getenv("RDS_USERNAME"))
            logger_local.exception(st, object=e)
        finally:
            logger_local.end("database-without-orm-local-python-package database_functions.close()")