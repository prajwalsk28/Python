"""
Student Record Management & Marks Analysis System
--------------------------------------------------
A menu-driven mini-project using Core Python + NumPy.

Concepts demonstrated:
- OOP (Student class)
- File handling (JSON storage)
- Exception handling
- NumPy: sum, mean, median, std, min, max
- Broadcasting (grace marks)
- Matrix operations (transpose, matrix-vector multiply, correlation)
- Random dataset generation
- Boolean indexing (pass/fail, toppers)
"""

import json
import os
import random
import numpy as np

DATA_FILE = "students_data.json"
SUBJECTS = ["Maths", "Science", "English", "History", "Computer"]
PASS_MARK = 40


class Student:
    """Represents a single student record (OOP)."""

    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks  # list of ints, aligned with SUBJECTS

    def to_dict(self):
        """Convert Student object to a dictionary (for JSON storage)."""
        return {"roll_no": self.roll_no, "name": self.name, "marks": self.marks}

    @staticmethod
    def from_dict(d):
        """Rebuild a Student object from a dictionary (loaded from JSON)."""
        return Student(d["roll_no"], d["name"], d["marks"])

    def __str__(self):
        marks_str = ", ".join(f"{s}: {m}" for s, m in zip(SUBJECTS, self.marks))
        return f"Roll No: {self.roll_no} | Name: {self.name} | {marks_str}"


class StudentManager:
    """Handles all operations: add/view/search, file I/O, and NumPy analysis."""

    def __init__(self):
        self.students = []
        self.load_from_file()

    # ---------------- File Handling ----------------
    def load_from_file(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    data = json.load(f)
                self.students = [Student.from_dict(d) for d in data]
            except (json.JSONDecodeError, KeyError):
                print("Warning: data file is corrupted. Starting with empty records.")
                self.students = []
        else:
            self.students = []

    def save_to_file(self):
        with open(DATA_FILE, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    # ---------------- Add / View / Search ----------------
    def add_student(self):
        try:
            roll_no = input("Enter Roll No: ").strip()
            if not roll_no:
                raise ValueError("Roll number cannot be empty.")
            if any(s.roll_no == roll_no for s in self.students):
                print("Error: Roll number already exists.\n")
                return

            name = input("Enter Name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty.")

            marks = []
            for subject in SUBJECTS:
                m = int(input(f"Enter marks in {subject} (0-100): "))
                if m < 0 or m > 100:
                    raise ValueError(f"Marks for {subject} must be between 0 and 100.")
                marks.append(m)

            student = Student(roll_no, name, marks)
            self.students.append(student)
            self.save_to_file()
            print(f"Student '{name}' added successfully.\n")

        except ValueError as e:
            print(f"Invalid input: {e}\n")

    def view_students(self):
        if not self.students:
            print("No student records found.\n")
            return
        print("\n--- All Students ---")
        for s in self.students:
            print(s)
        print()

    def search_student(self):
        key = input("Enter Roll No or Name to search: ").strip().lower()
        results = [
            s for s in self.students
            if key == s.roll_no.lower() or key in s.name.lower()
        ]
        if results:
            print("\n--- Search Results ---")
            for s in results:
                print(s)
            print()
        else:
            print("No matching student found.\n")

    # ---------------- NumPy Helpers ----------------
    def get_marks_matrix(self):
        """Returns a 2D NumPy array: rows = students, cols = subjects."""
        if not self.students:
            return np.array([])
        return np.array([s.marks for s in self.students])

    def analyze_marks(self):
        matrix = self.get_marks_matrix()
        if matrix.size == 0:
            print("No data to analyze.\n")
            return

        print("\n--- Marks Analysis (per student) ---")
        totals = np.sum(matrix, axis=1)
        means = np.mean(matrix, axis=1)
        for s, total, mean in zip(self.students, totals, means):
            print(f"{s.name}: Total={total}, Average={mean:.2f}")

        print("\n--- Marks Analysis (per subject) ---")
        for i, subject in enumerate(SUBJECTS):
            col = matrix[:, i]
            print(
                f"{subject}: Mean={np.mean(col):.2f}, Median={np.median(col):.2f}, "
                f"Std={np.std(col):.2f}, Min={np.min(col)}, Max={np.max(col)}"
            )
        print()

    def apply_grace_marks(self):
        """Demonstrates NumPy broadcasting: adding a scalar to every element."""
        matrix = self.get_marks_matrix()
        if matrix.size == 0:
            print("No data available.\n")
            return
        try:
            grace = int(input("Enter grace marks to add to every subject: "))
        except ValueError:
            print("Invalid number.\n")
            return

        # Broadcasting: scalar 'grace' is added to every element of the matrix
        updated = matrix + grace
        updated = np.clip(updated, 0, 100)  # keep marks within valid range

        for s, new_marks in zip(self.students, updated):
            s.marks = new_marks.tolist()

        self.save_to_file()
        print(f"Grace marks of {grace} applied to all students (capped at 100).\n")

    def matrix_operations(self):
        matrix = self.get_marks_matrix()
        if matrix.size == 0:
            print("No data available.\n")
            return

        print("\n--- Matrix Operations ---")
        print("Original Marks Matrix (Students x Subjects):")
        print(matrix)

        print("\nTranspose (Subjects x Students):")
        print(matrix.T)

        # Matrix-vector multiplication: weighted total score per student
        weights = np.array([0.25, 0.25, 0.20, 0.15, 0.15])
        if len(weights) == matrix.shape[1]:
            weighted_scores = matrix.dot(weights)
            print("\nWeighted Scores (Matrix . Weight Vector):")
            for s, score in zip(self.students, weighted_scores):
                print(f"{s.name}: {score:.2f}")

        # Correlation matrix between subjects (needs at least 2 students)
        if matrix.shape[0] >= 2:
            print("\nCorrelation Matrix between Subjects:")
            corr = np.corrcoef(matrix, rowvar=False)
            print(np.round(corr, 2))
        else:
            print("\n(Need at least 2 students to compute a correlation matrix.)")
        print()

    def generate_random_students(self):
        """Generates a random dataset of students using NumPy's random module."""
        try:
            n = int(input("How many random students to generate? "))
            if n <= 0:
                raise ValueError("Number must be positive.")
        except ValueError as e:
            print(f"Invalid input: {e}\n")
            return

        existing_rolls = {s.roll_no for s in self.students}
        counter = len(self.students) + 1

        for _ in range(n):
            roll_no = f"R{counter:03d}"
            while roll_no in existing_rolls:
                counter += 1
                roll_no = f"R{counter:03d}"
            name = f"Student_{counter}"
            marks = np.random.randint(0, 101, size=len(SUBJECTS)).tolist()
            self.students.append(Student(roll_no, name, marks))
            existing_rolls.add(roll_no)
            counter += 1

        self.save_to_file()
        print(f"{n} random students generated successfully.\n")

    def filter_pass_fail(self):
        """Demonstrates Boolean indexing for pass/fail and topper detection."""
        matrix = self.get_marks_matrix()
        if matrix.size == 0:
            print("No data available.\n")
            return

        totals = np.sum(matrix, axis=1)
        # Boolean mask: True only if student cleared PASS_MARK in every subject
        pass_mask = np.all(matrix >= PASS_MARK, axis=1)

        print(f"\n--- Pass/Fail (Pass mark per subject = {PASS_MARK}) ---")

        print("\nPASSED Students:")
        passed = [s for s, p in zip(self.students, pass_mask) if p]
        print("\n".join(str(s) for s in passed) if passed else "None")

        print("\nFAILED Students:")
        failed = [s for s, p in zip(self.students, pass_mask) if not p]
        print("\n".join(str(s) for s in failed) if failed else "None")

        # Toppers: student(s) with the highest total marks
        max_total = np.max(totals)
        topper_mask = totals == max_total
        toppers = [s for s, t in zip(self.students, topper_mask) if t]
        print(f"\nTOPPER(S) (Total = {max_total}):")
        for s in toppers:
            print(s)
        print()


def print_menu():
    print("========= STUDENT RECORD MANAGEMENT SYSTEM =========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Analyze Marks (NumPy stats)")
    print("5. Apply Grace Marks (Broadcasting)")
    print("6. Matrix Operations")
    print("7. Generate Random Student Dataset")
    print("8. Filter Pass/Fail and Toppers")
    print("9. Exit")
    print("=====================================================")


def main():
    manager = StudentManager()
    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ").strip()
        try:
            if choice == "1":
                manager.add_student()
            elif choice == "2":
                manager.view_students()
            elif choice == "3":
                manager.search_student()
            elif choice == "4":
                manager.analyze_marks()
            elif choice == "5":
                manager.apply_grace_marks()
            elif choice == "6":
                manager.matrix_operations()
            elif choice == "7":
                manager.generate_random_students()
            elif choice == "8":
                manager.filter_pass_fail()
            elif choice == "9":
                print("Exiting... Data saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")


if __name__ == "__main__":
    main()