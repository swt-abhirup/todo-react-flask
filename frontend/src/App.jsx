/* eslint-disable */
import { useEffect, useState } from "react";
import TodoItem from "./components/TodoItem";
import { fetchTodos, addTodo, updateTodo, deleteTodo } from "./services/api";
import "./theme.css"; // <-- add this

export default function App() {
  const [todos, setTodos] = useState([]);
  const [task, setTask] = useState("");
  const [loading, setLoading] = useState(true);
  const [theme, setTheme] = useState(() => {
    return localStorage.getItem("theme") ||
      (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  });

  // Update HTML attribute when theme changes
  useEffect(() => {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
  }, [theme]);

  // function toggleTheme() {
  //   setTheme(theme === "light" ? "dark" : "light");
  // }
    function toggleTheme() {
      // Add rotation class
      const icon = document.querySelector(".theme-toggle-icon");
      icon.classList.add("rotate");
    
      // Remove rotation class after animation ends
      setTimeout(() => icon.classList.remove("rotate"), 400);
    
      setTheme(theme === "light" ? "dark" : "light");
    }
  
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
    <div className="container py-5 fade-theme">
      {/* HEADER WITH THEME TOGGLE */}
      <div className="d-flex justify-content-between align-items-center mb-4">
      <h2 className="text-center mb-4">Todo App</h2>

        <button className="btn btn-secondary" onClick={toggleTheme}>
          {theme === "light" ? "🌙 Dark Mode" : "☀️ Light Mode"}
        </button>
      </div>

      {/* ADD FORM */}
      <form className="d-flex mb-4" onSubmit={handleAdd}>
        <input
          type="text"
          className="form-control me-2"
          placeholder="Add a new task..."
          value={task}
          onChange={(e) => setTask(e.target.value)}
        />
        <button
          className="theme-btn"
          onClick={toggleTheme}
          aria-label="Toggle theme"
        >
          <span className={`theme-toggle-icon ${theme === "dark" ? "rotate" : ""}`}>
            {theme === "light" ? (
              /* Sun Icon */
              <svg width="24" height="24" viewBox="0 0 24 24" fill="orange">
                <circle cx="12" cy="12" r="5"></circle>
                <g stroke="orange" strokeWidth="2">
                  <line x1="12" y1="1" x2="12" y2="4"></line>
                  <line x1="12" y1="20" x2="12" y2="23"></line>
                  <line x1="4" y1="12" x2="1" y2="12"></line>
                  <line x1="23" y1="12" x2="20" y2="12"></line>
                  <line x1="5" y1="5" x2="3" y2="3"></line>
                  <line x1="19" y1="19" x2="21" y2="21"></line>
                  <line x1="5" y1="19" x2="3" y2="21"></line>
                  <line x1="19" y1="5" x2="21" y2="3"></line>
                </g>
              </svg>
            ) : (
              /* Moon Icon */
              <svg width="24" height="24" viewBox="0 0 24 24" fill="yellow">
                <path d="M21 12.79A9 9 0 1111.21 3a7 7 0 109.79 9.79z"></path>
              </svg>
            )}
          </span>
        </button>
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
