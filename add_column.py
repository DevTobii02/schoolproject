import sqlite3

conn = sqlite3.connect('My_School.db')
c = conn.cursor()

# Add addmission_number column if it doesn't exist
try:
    c.execute("ALTER TABLE student ADD COLUMN addmission_number TEXT UNIQUE")
    print("Column added successfully.")
except sqlite3.OperationalError as e:
    print(f"Error: {e}")

conn.commit()
conn.close()
