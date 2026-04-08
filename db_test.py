import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="task_db",   # your DB name
        user="postgres",
        password="P@ssw0rd"   # your pgAdmin password
    )

    cur = conn.cursor()
    cur.execute(
    "INSERT INTO tasks (title, description, status) VALUES (%s, %s, %s)",
    ("Learn Kubernetes", "Day 1 completed", "pending")
    )
    conn.commit()

    cur.execute("SELECT * FROM tasks;")
    rows = cur.fetchall()

    print("Data from tasks table:")
    print(rows)

    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)