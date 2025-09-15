import sqlite3

conn = sqlite3.connect('My_School.db')
c = conn.cursor()

# Step 1: Rename existing table
c.execute("ALTER TABLE Students RENAME TO Students_old")

# Step 2: Create new table with admission_number
c.execute("""
CREATE TABLE Students(
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    gender TEXT NOT NULL CHECK (gender IN ('Male', 'Female')),
    date_of_birth DATE,
    email TEXT UNIQUE,
    address TEXT,
    admission_number TEXT UNIQUE
);
""")

# Step 3: Copy data from old table to new table
c.execute("""
INSERT INTO Students (StudentID, first_name, last_name, gender, date_of_birth, email, address, admission_number)
SELECT StudentID, first_name, last_name, gender, date_of_birth, email, address, NULL
FROM Students_old
""")

# Step 4: Drop old table
c.execute("DROP TABLE Students_old")

conn.commit()
conn.close()

print("Migration completed successfully.")
