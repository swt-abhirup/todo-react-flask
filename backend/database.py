# database.py
import mariadb
from datetime import datetime

# --------------------------
# Database Connection Config
# --------------------------
DB_CONFIG = {
    "user": "root",
    "password": "root123",
    "host": "localhost",
    "port": 3306,
    "database": "todo_app"   # <-- change to your database name
}


def get_connection():
    """Create and return a new MariaDB database connection."""
    try:
        conn = mariadb.connect(**DB_CONFIG)
        return conn
    except mariadb.Error as e:
        print("Error connecting to MariaDB:", e)
        raise


# --------------------------
# Convert Row to Dictionary
# --------------------------
def row_to_dict(row, columns):
    """Convert a row tuple to a dictionary using column names."""
    return {columns[i]: row[i] for i in range(len(columns))}


# --------------------------
# CRUD OPERATIONS
# --------------------------

# Get all todos
def get_todos():
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT id, task, completed, created_at FROM todos ORDER BY id DESC"
    cursor.execute(query)

    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()

    conn.close()

    return [row_to_dict(r, columns) for r in rows]


# Add a new todo
def add_todo(task):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO todos (task, completed) VALUES (%s, %s)"
    cursor.execute(query, (task, 0))
    conn.commit()

    new_id = cursor.lastrowid
    conn.close()

    return new_id


# Update a todo (completed status or task text)
def update_todo(todo_id, task, completed):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE todos
        SET task = %s, completed = %s
        WHERE id = %s
    """
    cursor.execute(query, (task, completed, todo_id))
    conn.commit()

    conn.close()
    return cursor.rowcount > 0


# Delete a todo
def delete_todo(todo_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM todos WHERE id = %s"
    cursor.execute(query, (todo_id,))
    conn.commit()

    conn.close()
    return cursor.rowcount > 0


# Get single todo by ID
def get_todo_by_id(todo_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT id, task, completed, created_at FROM todos WHERE id = %s"
    cursor.execute(query, (todo_id,))

    columns = [col[0] for col in cursor.description]
    row = cursor.fetchone()

    conn.close()

    if row:
        return row_to_dict(row, columns)
    return None
