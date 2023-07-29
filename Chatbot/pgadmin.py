import psycopg2


def getting_data(id):
    conn = psycopg2.connect(database="QA",
                        host="localhost",
                        user="postgres",
                        password="Aegon070",
                        port="5432")
    cursor = conn.cursor()
    query = "SELECT * FROM qaad WHERE id = %s;"
    cursor.execute(query, (id,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def add_user(id:str, username:str, password:str, qanda:str, email:str):
    conn = psycopg2.connect(database="QA",
                        host="localhost",
                        user="postgres",
                        password="Aegon070",
                        port="5432")
    cursor = conn.cursor()
    insert_query = "INSERT INTO qaad (id, Username, password, qanda, email) VALUES (%s, %s, %s, %s, %s);"
    cursor.execute(insert_query, (id, username, password, qanda, email))
    conn.commit()
    cursor.close()
    conn.close()


def add_data(qanda:str, id:str):
    conn = psycopg2.connect(database="QA",
                        host="localhost",
                        user="postgres",
                        password="Aegon070",
                        port="5432")
    cursor = conn.cursor()
    insert_query = "UPDATE qaad SET qanda = %s WHERE id = %s;"
    cursor.execute(insert_query, (qanda, id))
    conn.commit()
    cursor.close()
    conn.close()


def add_data2(qanda:str, id:str):
    conn = psycopg2.connect(database="QA",
                        host="localhost",
                        user="postgres",
                        password="Aegon070",
                        port="5432")
    cursor = conn.cursor()
    insert_query = "UPDATE qaad SET responses = %s WHERE id = %s;"
    cursor.execute(insert_query, (qanda, id))
    conn.commit()
    cursor.close()
    conn.close()