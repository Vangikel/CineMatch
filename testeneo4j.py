from neo4j import GraphDatabase

uri = "neo4j+s://3922b8be.databases.neo4j.io"  # Ou use a URL correta
user = "neo4j"
password = "ILqajvhiswIxT2TJbwT5ifoKdSBtDFnOrG35x4cJoSw"

def test_connection(uri, user, password):
    try:
        driver = GraphDatabase.driver(uri, auth=(user, password))
        with driver.session() as session:
            result = session.run("RETURN 'Conexão bem-sucedida' AS message")
            for record in result:
                print(record["message"])
        driver.close()
    except Exception as e:
        print(f"Erro: {e}")

test_connection(uri, user, password)
