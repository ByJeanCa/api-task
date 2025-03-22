from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route("/tasks", methods=["POST"])
def create_task():
    task_id = request.args.get("task_id")
    description = request.args.get("description")
    if not task_id or not description:
        return jsonify({"error": "Missing task_id or description"}), 400
    r.set(task_id, description)
    return jsonify({"task_id": task_id, "description": description, "instance": os.getenv("HOSTNAME", "unknown")})

@app.route("/tasks/<task_id>", methods=["GET"])
def get_task(task_id):
    description = r.get(task_id)
    if description is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"task_id": task_id, "description": description, "instance": os.getenv("HOSTNAME", "unknown")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)