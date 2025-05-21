import sqlite3

# Connect to your actual database file
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the 'users' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insert some sample data
cursor.executemany('''
    INSERT INTO users (username, email, password)
    VALUES (?, ?, ?)
''', [
    ("alice", "alice@example.com", "password123"),
    ("bob", "bob@example.com", "securepass"),
    ("charlie", "charlie@example.com", "admin123")
])

conn.commit()
conn.close()

print("Database initialized and sample users added.")
