/* eslint-disable */
export default function TodoItem({ todo, onToggle, onDelete }) {
    return (
      <li className="list-group-item d-flex justify-content-between align-items-center">
        <div>
          <input
            type="checkbox"
            className="form-check-input me-2"
            checked={todo.completed}
            onChange={() => onToggle(todo.id, !todo.completed)}
          />
          <span style={{ textDecoration: todo.completed ? "line-through" : "none" }}>
            {todo.task}
          </span>
        </div>
  
        <button className="btn btn-danger btn-sm" onClick={() => onDelete(todo.id)}>
          Delete
        </button>
      </li>
    );
  }
  