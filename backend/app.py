from flask import Flask, request, jsonify
from flask_cors import CORS
import database
import models


def create_app():
    app = Flask(__name__)
    CORS(app)

    # -----------------------------
    # Health Check
    # -----------------------------
    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    # -----------------------------
    # List all todos
    # -----------------------------
    @app.get("/todos")
    def list_todos():
        todos = models.fetch_all_todos()
        return jsonify(todos), 200

    # -----------------------------
    # Create a new todo
    # -----------------------------
    @app.post("/todos")
    def create_todo():
        if not request.is_json:
            return jsonify({"error": "Expected JSON body"}), 400

        data = request.get_json()
        task = str(data.get("task", "")).strip()

        if not task:
            return jsonify({"error": "Missing or empty 'task' field"}), 400

        new_id = models.add_todo(task)
        return jsonify({"message": "Task added", "id": new_id}), 201

    # -----------------------------
    # Get a todo by ID
    # -----------------------------
    @app.get("/todos/<int:id>")
    def get_todo(id):
        todo = models.fetch_todo(id)
        if todo is None:
            return jsonify({"error": "Todo not found"}), 404
        return jsonify(todo), 200

    # -----------------------------
    # Update todo (task and/or completed)
    # -----------------------------
    @app.put("/todos/<int:id>")
    def put_todo(id):
        if not request.is_json:
            return jsonify({"error": "Expected JSON body"}), 400

        data = request.get_json()

        # Extract fields
        task = data.get("task")
        completed = data.get("completed")

        # Validate task
        if task is not None:
            task = str(task).strip()
            if task == "":
                return jsonify({"error": "'task' cannot be empty"}), 400

        # Normalize completed
        if completed is not None:
            if isinstance(completed, (int, bool)):
                completed = int(bool(completed))
            else:
                return jsonify({"error": "Invalid 'completed' value"}), 400

        updated = models.update_todo(id, task=task, completed=completed)
        if not updated:
            return jsonify({"error": "Todo not found or no valid fields"}), 404

        return jsonify({"message": "Updated"}), 200

    # -----------------------------
    # Delete todo
    # -----------------------------
    @app.delete("/todos/<int:id>")
    def delete_todo(id):
        deleted = models.delete_todo(id)
        if not deleted:
            return jsonify({"error": "Todo not found"}), 404
        return jsonify({"message": "Deleted"}), 200

    # -----------------------------
    # Error Handlers
    # -----------------------------
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({"error": "Method not allowed"}), 405

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({"error": "Internal server error"}), 500

    return app


# ------------------------------------
# Local Development Server
# ------------------------------------
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
