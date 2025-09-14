import  sqlite3
#connect to database
conn = sqlite3.connect('My_School.db') #establosh
c = conn.cursor()  #Connection Object

#for every column represented in the table there is a label and an entry widget

c.execute("""
CREATE TABLE IF NOT EXISTS Students(
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    gender TEXT NOT NULL CHECK (gender IN ('Male', 'Female')),
    date_of_birth DATE,
    email TEXT UNIQUE,
    address TEXT
    );
    """)

#Academic Registration Table
c.execute("""
CREATE TABLE IF NOT EXISTS AcademicRegistration(
    first_name TEXT,
    last_name TEXT,
    department_id INTEGER,
    department_name TEXT
     );
    """)

#Returning Student Validation Table
c.execute(""" 
CREATE TABLE IF NOT EXISTS ReturningStudents(
    StudentID INTEGER,
    first_name TEXT,
    last_name TEXT
    );
    """)

c.execute("""
CREATE TABLE IF NOT EXISTS StudentDashboard( 
          StudentID INTEGER,
          activity TEXT,
          activity_date
          );
          """)

#Student Related Functions
def insert_student(first_name, last_name, gender, date_of_birth, email, address):
    conn = sqlite3.connect('My_School.db')
    c = conn.cursor()
    c.execute("""INSERT INTO STUDENTS (first_name, last_name, gender, date_of_birth, email, address)
              VALUES (?, ?, ?, ?, ?, ?)""", (first_name, last_name, gender, date_of_birth, email, address)) #Question Marks As Placeholders For Parameters
    conn.commit()
    conn.close()

def get_student():
    conn = sqlite3.connect('My_School.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM STUDENTS""")
    rows = c.fetchall()
    conn.close()
    return rows

#Academic Registration Function
def insert_academic_registration(StudentID, department, session, level):
    conn = sqlite3.connect('My_School.db')
    c = conn.cursor()
    c.execute("""INSERT INTO AcademicRegistration (StudentID, department, session, level)   
        VALUES(?, ?, ?, ?)""", (StudentID, department, session, level)) #Question Marks As Placeholders For Parameters
    conn.commit()
    conn.close()

    def check():
        pass

# Dictionary mapping departments to subjects
DEPARTMENT_SUBJECTS = {
    "Science": ["Mathematics", "Physics", "Chemistry", "Biology"],
    "Arts": ["English", "History", "Geography", "Literature"],
    "Commerce": ["Accounting", "Economics", "Business Studies", "Statistics"],
    "Engineering": ["Mathematics", "Physics", "Computer Science", "Engineering Drawing"]
}

def get_subjects_by_department(department):
    """Return list of subjects for the given department."""
    return DEPARTMENT_SUBJECTS.get(department, [])
