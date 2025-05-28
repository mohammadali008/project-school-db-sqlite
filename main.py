import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("school.db")

# Enable foreign key constraints
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

# Create teachers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    phone TEXT
)
""")

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    phone TEXT
)
""")

# Create courses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        ON DELETE SET NULL ON UPDATE CASCADE
)
""")

# Create student_courses table (many-to-many relation)
cursor.execute("""
CREATE TABLE IF NOT EXISTS student_courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id)
        ON DELETE CASCADE ON UPDATE CASCADE
)
""")

# Commit and close connection
conn.commit()
conn.close()

print("Database and tables created successfully.")
### --- Test --- #
import sqlite3

# Connect to the database
conn = sqlite3.connect("school.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

# Sample teachers
teachers = [
    ("رضا احمدی", "09120000001"),
    ("مینا کریمی", "09120000002"),
    ("کامران مرادی", "09120000003"),
]
cursor.executemany("INSERT INTO teachers (full_name, phone) VALUES (?, ?)", teachers)

# Sample students
students = [
    ("علی رضایی", "09121000001"),
    ("نگار محمدی", "09121000002"),
    ("سارا صادقی", "09121000003"),
    ("امیر حسینی", "09121000004"),
]
cursor.executemany("INSERT INTO students (full_name, phone) VALUES (?, ?)", students)

# Sample courses
courses = [
    ("ریاضی پایه", 1),
    ("علوم تجربی", 2),
    ("زبان انگلیسی", 3),
    ("فیزیک مقدماتی", 1),
]
cursor.executemany("INSERT INTO courses (title, teacher_id) VALUES (?, ?)", courses)

# Sample enrollments
student_courses = [
    (1, 1),
    (1, 3),
    (2, 1),
    (2, 2),
    (3, 4),
    (4, 1),
    (4, 2),
    (4, 3),
]
cursor.executemany("INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)", student_courses)

# Commit and close
conn.commit()
conn.close()

print("Sample data inserted successfully.")
