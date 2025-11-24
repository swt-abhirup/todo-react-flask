from database import get_connection


# -----------------------------
# Convert DB row → Python dict
# -----------------------------
def row_to_dict(row) -> dict:
    return {
        "id": row["id"],
        "task": row["task"],
        "completed": bool(row["completed"]),
        "created_at": row["created_at"].isoformat() if row["created_at"] else None
    }


# -----------------------------
# Fetch all todos
# -----------------------------
def fetch_all_todos():
    db = get_connection()
    cur = db.cursor(dictionary=True)
    cur.execute("""
        SELECT id, task, completed, created_at 
        FROM todos 
        ORDER BY id DESC
    """)
    rows = cur.fetchall()
    return [row_to_dict(r) for r in rows]


# -----------------------------
# Add a todo
# -----------------------------
def add_todo(task: str):
    db = get_connection()
    cur = db.cursor()
    cur.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
    db.commit()
    return cur.lastrowid


# -----------------------------
# Update a todo
# -----------------------------
def update_todo(id: int, completed=None, task=None):
    db = get_connection()
    cur = db.cursor()

    updates = []
    values = []

    if completed is not None:
        updates.append("completed = %s")
        values.append(int(bool(completed)))

    if task is not None:
        updates.append("task = %s")
        values.append(task)

    if not updates:
        return False  # No fields provided

    values.append(id)

    sql = f"UPDATE todos SET {', '.join(updates)} WHERE id = %s"
    cur.execute(sql, values)
    db.commit()

    return cur.rowcount > 0


# -----------------------------
# Delete a todo
# -----------------------------
def delete_todo(id: int):
    db = get_connection()
    cur = db.cursor()
    cur.execute("DELETE FROM todos WHERE id = %s", (id,))
    db.commit()
    return cur.rowcount > 0


# -----------------------------
# Fetch a single todo
# -----------------------------
def fetch_todo(id: int):
    db = get_connection()
    cur = db.cursor(dictionary=True)
    cur.execute("""
        SELECT id, task, completed, created_at 
        FROM todos 
        WHERE id = %s
    """, (id,))
    row = cur.fetchone()
    return row_to_dict(row) if row else None
