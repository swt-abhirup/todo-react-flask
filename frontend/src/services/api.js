const API = import.meta.env.VITE_API_URL;

export async function fetchTodos() {
  const res = await fetch(`${API}/todos`);
  return res.json();
}

export async function addTodo(task) {
  const res = await fetch(`${API}/todos`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ task }),
  });
  return res.json();
}

export async function updateTodo(id, data) {
  const res = await fetch(`${API}/todos/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function deleteTodo(id) {
  const res = await fetch(`${API}/todos/${id}`, { method: "DELETE" });
  return res.json();
}
