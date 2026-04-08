from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

# ✅ app must be defined BEFORE using @app
app = FastAPI()

class Task(BaseModel):
    title: str
    description: str
    status: str

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="task_db",
        user="postgres",
        password="P@ssw0rd"
    )

@app.post("/tasks")
def create_task(task: Task):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO tasks (title, description, status) VALUES (%s, %s, %s)",
            (task.title, task.description, task.status)
        )
        conn.commit()

        cur.close()
        conn.close()

        return {"message": "Task created successfully"}

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}
    
    # ✅ 👉 ADD THIS BELOW (new GET API)
@app.get("/tasks")
def get_tasks():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows