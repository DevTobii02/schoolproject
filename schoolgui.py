#iconphoto only support png and gif
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import schooldb
class SchoolManager:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("900x500")
        self.root.configure(background="purple")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        school_image =  Image.open("download (15).jpg")
        school_image = school_image.resize((50, 50))
        self.school_image = ImageTk.PhotoImage(school_image)

        tk.Label(root, text="School Management System", image=self.school_image, compound="left", bg="yellow",fg="black", font=("Times New Roman", 18, "bold"), padx=10, pady=10).grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)

        # Centered buttons in the main window for better layout
        tk.Button(self.root, text="New Student", command=self.new_student,  font=("Times New Roman", 18, "bold")).grid(row=2, column=0, pady=5, padx=3, ipady=7, ipadx=7, sticky="ew")
        tk.Button(self.root, text="Returning Student",  command=self.returning_student, font=("Times New Roman", 18, "bold")).grid(row=2, column=1, pady=5, padx=5, ipady=7, ipadx=7, sticky="ew")



    def new_student(self):
        print("New Student")
        new_student_window = tk.Toplevel(self.root)
        new_student_window.title("New Student Registration Window")
        new_student_window.geometry("900x500")
        new_student_window.configure(background="purple")
        new_student_window.grid_columnconfigure(0, weight=1)
        new_student_window.grid_columnconfigure(1, weight=1)

        new_student_image = Image.open("New students blog photo.png")
        new_student_image = new_student_image.resize((50, 50))
        self.new_student_image = ImageTk.PhotoImage(new_student_image)

        tk.Label(new_student_window, text="New Student Registration", image=self.new_student_image, compound="left", bg="yellow", fg="black", font=("Times New Roman", 18, "bold"), padx=10, pady=10).grid(row=0, column=0, columnspan=2, sticky="ew", pady=10, ipady=5, ipadx=5)

        #First Name Label and Entry
        tk.Label(new_student_window,  text="Last Name : ", font=("Times New Roman", 18, "bold")).grid(row=1, column=0, columnspan=2, padx=7, pady=7, ipady=5, ipadx=5, sticky="w")
        self.last_name_entry = tk.Entry(new_student_window, width=30)
        self.last_name_entry.grid(row=1, column=1, columnspan=2, sticky="w")

        tk.Label(new_student_window, text="First Name : ", font=("Times New Roman", 18, "bold")).grid(row=2, column=0, columnspan=2, padx=7, pady=7,ipady=5, ipadx=5,sticky="w")
        self.first_name_entry = tk.Entry(new_student_window, width=30)
        self.first_name_entry.grid(row=2, column=1, columnspan=2, sticky="w")

        tk.Label(new_student_window, text="Middle Name : ", font=("Times New Roman", 18, "bold")).grid(row=3, column=0, columnspan=2,padx=7, pady=7,ipady=5, ipadx=5,sticky="w")
        self.middle_name_entry = tk.Entry(new_student_window, width=30)
        self.middle_name_entry.grid(row=3, column=1, columnspan=2, sticky="w")

        tk.Label(new_student_window, text="Gender : ", font=("Times New Roman", 18, "bold")).grid(row=4, column=0,columnspan=2, padx=7, pady=7,ipady=5,ipadx=5,sticky="w")
        self.gender_entry = tk.Entry(new_student_window, width=30)
        self.gender_entry.grid(row=4, column=1, columnspan=2, sticky="w")

        tk.Label(new_student_window, text="Date Of Birth : ", font=("Times New Roman", 18, "bold")).grid(row=5, column=0,columnspan=2,padx=7, pady=7,ipady=5, ipadx=5,sticky="w")
        self.DOB_entry = tk.Entry(new_student_window, width=30)
        self.DOB_entry.grid(row=5, column=1, columnspan=2, sticky="w")

        tk.Label(new_student_window, text="Nationality: ", font=("Times New Roman", 18, "bold")).grid(row=6, column=0,columnspan=2,padx=7, pady=7,ipady=5, ipadx=5,sticky="w")
        self.Nationality_entry = tk.Entry(new_student_window, width=30)
        self.Nationality_entry.grid(row=6, column=1, columnspan=2, sticky="w")

        tk.Label(new_student_window, text="State Of Origin : ", font=("Times New Roman", 18, "bold")).grid(row=7, column=0, columnspan=2,padx=7, pady=7,ipady=5, ipadx=5,sticky="w")
        self.SOO_entry = tk.Entry(new_student_window, width=30)
        self.SOO_entry.grid(row=7, column=1, columnspan=2, sticky="w")

        tk.Label(new_student_window, text="Email :", font=("Times New Roman", 18, "bold")).grid(row=8, column=0, columnspan=2, padx=7, pady=7,ipady=5, ipadx=5,sticky="w")
        self.email_entry = tk.Entry(new_student_window, width=30)
        self.email_entry.grid(row=8, column=1, columnspan=2, sticky="w")

        tk.Label(new_student_window, text="Password :", font=("Times New Roman", 18, "bold")).grid(row=9, column=0, columnspan=2, padx=7, pady=7,ipady=5, ipadx=5,sticky="w")
        self.password_entry = tk.Entry(new_student_window, width=30)
        self.password_entry.grid(row=9, column=1, columnspan=2, sticky="w")

        tk.Button(new_student_window, text="Submit", command=self.submit_student_details, font=("Times New Roman", 18, "bold")).grid(row=10, column=1, padx=7, pady=7,ipady=5, ipadx=5,sticky="w")


    def submit_student_details(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        gender = self.gender_entry.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "Please enter both email and password")
            return
        messagebox.showinfo("Success", "Student details confirmed. Proceeding to academic registration.")
        self.academic_registration()

        if gender not in ["Male", "Female"]:
            tk.messagebox.showerror("Error", "Gender must be Male/Female.")
            return


        #tk.Label(submit_student_details_window, text="Collecting Student Details", bg="yellow", fg="black",font=("Times New Roman", 18, "bold")).grid(row=0, column=0, padx=7, pady=7,ipady=5, ipadx=5,sticky="ew")
        # Gets Value From Submit New Student Registration Window



    def academic_registration(self):
        print("Academic Registration For New Student")
        academic_registration_window = tk.Toplevel()
        academic_registration_window.title("Academic Registration")
        academic_registration_window.geometry("900x500")
        academic_registration_window.configure(bg="purple")
        academic_registration_window.grid_columnconfigure(0, weight=1)
        academic_registration_window.grid_columnconfigure(1, weight=1)

        academic_registration_image = Image.open("1693370792780.png")
        academic_registration_image = academic_registration_image.resize((50, 50))
        self.academic_registration_image = ImageTk.PhotoImage(academic_registration_image)

        tk.Label(academic_registration_window, image= self.academic_registration_image, compound="left",  text="Academic Registration", bg="yellow", fg="black", font=("Times New Roman", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=10, ipady=5, ipadx=5, sticky="ew")
        tk.Label(academic_registration_window, text="First Name : ", font=("Times New Roman", 18, "bold")).grid(row=1, column=0, columnspan=2, padx=7, pady=7, ipady=5, ipadx=5,sticky="w")
        self.first_name_entry = tk.Entry(academic_registration_window, width=30)
        self.first_name_entry.grid(row=1, column=1, columnspan=2, sticky="w")

        tk.Label(academic_registration_window, text="Class  :", font=("Times New Roman", 18, "bold")).grid(row=2, column=0, columnspan=2, padx=7, pady=7, ipady=5, ipadx=5,sticky="w")
        self.class_entry = tk.Entry(academic_registration_window, width=30)
        self.class_entry.grid(row=2, column=1, columnspan=2, sticky="w")

        tk.Label(academic_registration_window, text="Subjects :", font=("Times New Roman", 18, "bold")).grid(row=3, column=0, columnspan=2, padx=7, pady=7, ipady=5, ipadx=5,sticky="w")
        self.subjects_listbox = tk.Listbox(academic_registration_window, selectmode=tk.MULTIPLE, height=4, width=30)
        self.subjects_listbox.grid(row=3, column=1, columnspan=2, sticky="w")

        tk.Label(academic_registration_window, text="Department :", font=("Times New Roman", 18, "bold")).grid(row=4, column=0, columnspan=2, padx=7, pady=7, ipady=5, ipadx=5,sticky="w")
        self.department_entry = tk.Entry(academic_registration_window, width=30)
        self.department_entry.grid(row=4, column=1, columnspan=2, sticky="w")
        self.department_entry.bind('<KeyRelease>', self.update_subjects)

        tk.Button(academic_registration_window, text="Submit", command=self.submit_academic_registration, font=("Times New Roman", 18, "bold")).grid(row=6, column=1, padx=7, pady=7, ipady=5, ipadx=5, sticky="w")

    def update_subjects(self, event=None):
        department = self.department_entry.get().strip()
        subjects = schooldb.get_subjects_by_department(department)
        self.subjects_listbox.delete(0, tk.END)
        for subject in subjects:
            self.subjects_listbox.insert(tk.END, subject)

    def submit_academic_registration(self):
        selected_indices = self.subjects_listbox.curselection()
        department = self.department_entry.get().strip()

        if not department:
            messagebox.showerror("Error", "Please select a department")
            return
        if not selected_indices:
            messagebox.showerror("Error", "Please select subjects")
            return
        subjects = [self.subjects_listbox.get(i) for i in selected_indices]
        messagebox.showinfo("Success", "Academic registration successful. Opening student dashboard.")
        self.open_student_dashboard()


    def returning_student(self):
        print("Returning Student")
        returning_window = tk.Toplevel(self.root)
        returning_window.title("Returning Student Window")
        returning_window.geometry("900x500")
        returning_window.configure(background="purple")
        returning_window.grid_columnconfigure(0, weight=1)
        returning_window.grid_columnconfigure(1, weight=1)

        returning_student_image = Image.open("images (2).png")
        returning_student_image = returning_student_image.resize((50, 50))
        self.returning_student_image = ImageTk.PhotoImage(returning_student_image)
        # Adjusted title label padding to match Academic Registration window
        tk.Label(returning_window, text="Returning Student", image=  self.returning_student_image, compound="left" , font=("Times New Roman", 18, "bold"), bg="yellow", fg="black").grid(row=0, column=0, columnspan=2, sticky="ew", pady=10, ipady=5, ipadx=5)


        tk.Label(returning_window, text="Email :", font=("Times New Roman", 18, "bold")).grid(row=1, column=0, columnspan=2, padx=7, pady=7, ipady=5, ipadx=5,sticky="w")
        self.email_entry = tk.Entry(returning_window, width=30)
        self.email_entry.grid(row=1, column=1, columnspan=2, sticky="w")


        tk.Label(returning_window, text="Password :", font=("Times New Roman", 18, "bold")).grid(row=2, column=0, columnspan=2, padx=7, pady=7, ipady=5, ipadx=5,sticky="w")
        self.password_entry = tk.Entry(returning_window, width=30)
        self.password_entry.grid(row=2, column=1, columnspan=2, sticky="w")

        # Adjusted submit button padding and removed columnspan to match Academic Registration
        tk.Button(returning_window, text="Submit", command=self.validate_returning_student_details, font=("Times New Roman", 18, "bold")).grid(row=4, column=1, padx=7, pady=7, ipady=5, ipadx=5, sticky="w")
    def validate_returning_student_details(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "Please enter both email and password")
            return
        messagebox.showinfo("Success", "Login successful. Proceeding to academic registration.")
        self.academic_registration()

    def open_student_dashboard(self):
        # Create a new top-level window for the student dashboard
        student_dashboard_window = tk.Toplevel(self.root)
        # Set the title of the dashboard window
        student_dashboard_window.title("Student Dashboard Window")
        # Set the size of the window
        student_dashboard_window.geometry("900x600")
        # Configure the background color
        student_dashboard_window.configure(background="purple")
        # Configure grid columns to distribute space evenly
        for i in range(4):
            student_dashboard_window.grid_columnconfigure(i, weight=1)

        # Add a welcome label at the top of the dashboard
        tk.Label(student_dashboard_window, text="Welcome Student To Your Dashboard", bg="yellow", fg="black", font=("Times New Roman", 18, "bold"), padx=5, pady=10).grid(row=0, column=0, columnspan=4, sticky="ew", pady=10, ipady=5, ipadx=5)

        # Define a 2D list of activities for the buttons, organized in a 4x4 grid
        activities = [
            ["View Profile", "Update Profile", "Register Courses", "View Grades"],
            ["Submit Assignment", "View Assignments", "Check Attendance", "View Timetable"],
            ["Access Library", "View Fees", "Pay Fees", "Contact Teacher"],
            ["View Announcements", "Download Resources", "Change Password", "Logout"]
        ]

        # Loop through each row and column to create buttons for each activity
        for row in range(4):
            for col in range(4):
                # Get the activity name for the current position
                activity = activities[row][col]
                # Create a button with the activity name, set font, and command to print the activity when clicked
                tk.Button(student_dashboard_window, text=activity, font=("Times New Roman", 14, "bold"), command=lambda a=activity: print(f"Clicked: {a}")).grid(row=row+1, column=col, padx=5, pady=5, sticky="nsew")

if __name__ == "__main__":
    root = tk.Tk()
    school_icon = Image.open("download (15).jpg")
    school_icon = school_icon.resize((30, 30))
    school_icon = ImageTk.PhotoImage(school_icon)
    root.iconphoto(True, school_icon)
    school_app = SchoolManager(root)
    root.mainloop()