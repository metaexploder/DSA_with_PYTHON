from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False # Keep JSON response order as defined

DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # This allows access to columns by name
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database when the app starts
with app.app_context():
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todos', methods=['GET'])
def get_todos():
    conn = get_db_connection()
    todos = conn.execute('SELECT * FROM todos ORDER BY id DESC').fetchall()
    conn.close()
    # Convert Row objects to dictionaries for JSON serialization
    todos_list = [dict(row) for row in todos]
    return jsonify(todos_list)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    todo_text = data['text'].strip()
    if not todo_text:
        return jsonify({"error": "Task text cannot be empty"}), 400

    conn = get_db_connection()
    cursor = conn.execute('INSERT INTO todos (text, completed) VALUES (?, ?)', (todo_text, 0))
    conn.commit()
    new_todo_id = cursor.lastrowid
    new_todo = conn.execute('SELECT * FROM todos WHERE id = ?', (new_todo_id,)).fetchone()
    conn.close()
    return jsonify(dict(new_todo)), 201 # 201 Created

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    conn = get_db_connection()
    todo = conn.execute('SELECT * FROM todos WHERE id = ?', (todo_id,)).fetchone()

    if todo is None:
        conn.close()
        return jsonify({"error": "Todo not found"}), 404

    # Allow partial updates: only 'text' or 'completed'
    updated_text = data.get('text', todo['text']).strip()
    updated_completed = data.get('completed', todo['completed'])

    if 'text' in data and not updated_text:
        return jsonify({"error": "Task text cannot be empty"}), 400

    conn.execute('UPDATE todos SET text = ?, completed = ? WHERE id = ?',
                 (updated_text, updated_completed, todo_id))
    conn.commit()
    updated_todo = conn.execute('SELECT * FROM todos WHERE id = ?', (todo_id,)).fetchone()
    conn.close()
    return jsonify(dict(updated_todo))

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    conn = get_db_connection()
    cursor = conn.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    if rows_affected == 0:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({"message": "Todo deleted successfully"}), 200 # 200 OK

if __name__ == '__main__':
    app.run(debug=True) # debug=True reloads the server on code changes