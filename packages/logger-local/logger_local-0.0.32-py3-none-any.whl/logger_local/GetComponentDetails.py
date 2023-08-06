import pymysql
import os
from dotenv import load_dotenv
load_dotenv()


class GetComponetDetails():
    @staticmethod
    def get_connection() -> pymysql.connections.Connection:
        return pymysql.connect(
            user=os.getenv('RDS_USERNAME'),
            password=os.getenv('RDS_PASSWORD'),
            host=os.getenv('RDS_HOSTNAME'),
        )

    @staticmethod
    def getComponentDetails(component_id):
        try:
            connection = GetComponetDetails.get_connection()
            cursor = connection.cursor()
            sql_query = "SELECT name, component_type, component_category, testing_framework, api_type FROM component.component_table WHERE id = %s"
            cursor.execute(sql_query, (component_id,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print("Exception catched " + str(e))
            return None
