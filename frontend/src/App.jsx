/* eslint-disable */
import { useEffect, useState } from "react";
import TodoItem from "./components/TodoItem";
import { fetchTodos, addTodo, updateTodo, deleteTodo } from "./services/api";

export default function App() {
  const [todos, setTodos] = useState([]);
  const [task, setTask] = useState("");
  const [loading, setLoading] = useState(true);

  // load data
  useEffect(() => {
    loadTodos();
  }, []);

  async function loadTodos() {
    setLoading(true);
    const data = await fetchTodos();
    setTodos(data);
    setLoading(false);
  }

  async function handleAdd(e) {
    e.preventDefault();
    if (!task.trim()) return;

    await addTodo(task);
    setTask("");
    loadTodos();
  }

  async function toggleTodo(id, completed) {
    await updateTodo(id, { completed });
    loadTodos();
  }

  async function removeTodo(id) {
    await deleteTodo(id);
    loadTodos();
  }

  return (
    <div className="container py-5">
      <h2 className="text-center mb-4">Todo App</h2>

      {/* ADD FORM */}
      <form className="d-flex mb-4" onSubmit={handleAdd}>
        <input
          type="text"
          className="form-control me-2"
          placeholder="Add a new task..."
          value={task}
          onChange={(e) => setTask(e.target.value)}
        />
        <button className="btn btn-primary">Add</button>
      </form>

      {/* LOADING */}
      {loading ? (
        <p className="text-center">Loading...</p>
      ) : (
        <ul className="list-group">
          {todos.map((todo) => (
            <TodoItem
              key={todo.id}
              todo={todo}
              onToggle={toggleTodo}
              onDelete={removeTodo}
            />
          ))}
        </ul>
      )}
    </div>
  );
}
