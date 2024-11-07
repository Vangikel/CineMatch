# neo4j_connection.py
from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]

# Substitua com as credenciais do seu Neo4j
neo4j_conn = Neo4jConnection(uri="neo4j+s://3922b8be.databases.neo4j.io", user="neo4j", password="ILqajvhiswIxT2TJbwT5ifoKdSBtDFnOrG35x4cJoSw")
