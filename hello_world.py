def print_welcome_message():
    """Displays the program's welcome banner and introduction with the author's name and program purpose."""
    print("=" * 50)
    print("Hello World!")
    print("=" * 50)
    print()
    print("My name is Kenneth Maberi.")
    print("I am a Computer Science Student at BYU-Pathway.")
    print("Welcome to my first CSE 310 project!")
    print()
    print("Let's have an amazing semester together!")
    print()


def get_nonnegative_integer(prompt):
    """Prompts until the user provides a whole number that is zero or greater."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a number that is zero or greater.")
                continue
            return value
        except ValueError:
            print("Please enter a valid whole number.")


def get_user_info():
    """Prompts the user to enter their name, age, and favorite color, then returns the data as a dictionary."""
    name = input("What is your name? ")
    age = get_nonnegative_integer("How old are you? ")
    favorite_color = input("What is your favorite color? ")
    return {"name": name, "age": age, "favorite_color": favorite_color}


def calculate_birth_year(current_year, age):
    """Calculates and returns the approximate birth year by subtracting age from the current year."""
    birth_year = current_year - age
    return birth_year


def display_personalized_greeting(user_info, birth_year):
    """Displays a personalized greeting using the user's name, birth year, and favorite color.
    Includes conditional messaging based on the user's age group."""
    print()
    print("-" * 50)
    print(f"Nice to meet you, {user_info['name']}!")
    print(f"You were born around the year {birth_year}.")
    print(f"Your favorite color is {user_info['favorite_color']}.")

    if user_info["age"] < 18:
        print("You are a minor. Enjoy your youth!")
    elif 18 <= user_info["age"] < 30:
        print("You are in your prime years. Great time to learn!")
    elif 30 <= user_info["age"] < 50:
        print("You are in your experienced years. Keep growing!")
    else:
        print("You have a wealth of wisdom to share!")
    print("-" * 50)
    print()


def count_to_number():
    """Prompts for a number and counts up to it with a FizzBuzz game:
    multiples of 3 show Fizz, multiples of 5 show Buzz, multiples of both show FizzBuzz."""
    max_count = get_nonnegative_integer("Enter a number to count up to: ")
    print(f"\nCounting from 1 to {max_count}:")
    for i in range(1, max_count + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} - FizzBuzz!")
        elif i % 3 == 0:
            print(f"{i} - Fizz")
        elif i % 5 == 0:
            print(f"{i} - Buzz")
        else:
            print(i)
    print()


def multiplication_table():
    """Generates and displays a multiplication table of a user-specified size using nested loops."""
    size = get_nonnegative_integer("Enter the size of multiplication table (e.g., 10): ")
    print(f"\nMultiplication Table ({size}x{size}):")
    for row in range(1, size + 1):
        row_values = []
        for col in range(1, size + 1):
            product = row * col
            row_values.append(f"{product:4d}")
        print(" ".join(row_values))
    print()


class Student:
    """Represents a university student with name, ID, major, enrolled courses, and course grades."""
    def __init__(self, name, student_id, major):
        """Initializes a Student object with name, ID, major, and empty course/grade collections."""
        self.name = name
        self.student_id = student_id
        self.major = major
        self.courses = []
        self.grades = {}

    def enroll_course(self, course_name):
        """Adds a course to the student's enrolled list if not already present."""
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"Successfully enrolled in {course_name}")
        else:
            print(f"Already enrolled in {course_name}")

    def assign_grade(self, course_name, grade):
        """Assigns a letter grade to a course if the student is enrolled in it."""
        if course_name in self.courses:
            self.grades[course_name] = grade
            print(f"Grade {grade} assigned to {course_name}")
        else:
            print(f"Cannot assign grade - not enrolled in {course_name}")

    def calculate_gpa(self):
        """Calculates and returns the grade point average on a 4.0 scale from stored letter grades."""
        if not self.grades:
            return 0.0
        total_points = 0
        grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
        for grade in self.grades.values():
            total_points += grade_points.get(grade.upper(), 0.0)
        return total_points / len(self.grades)

    def display_student_info(self):
        """Prints a formatted summary of the student's profile, courses, grades, and GPA."""
        print("\n" + "=" * 50)
        print("STUDENT INFORMATION")
        print("=" * 50)
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print(f"Enrolled Courses: {', '.join(self.courses) if self.courses else 'None'}")
        print(f"Grades: {self.grades if self.grades else 'No grades yet'}")
        gpa = self.calculate_gpa()
        print(f"Current GPA: {gpa:.2f}")
        print("=" * 50 + "\n")


def save_user_to_file(user_info, filename="user_data.txt"):
    """Writes the provided user information dictionary to a text file with a labeled log format.
    Handles IOError exceptions if the file cannot be written."""
    try:
        with open(filename, "w") as file:
            file.write("User Information Log\n")
            file.write("=" * 30 + "\n")
            for key, value in user_info.items():
                file.write(f"{key.capitalize()}: {value}\n")
            file.write("\n")
        print(f"User data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")


def read_user_from_file(filename="user_data.txt"):
    """Reads and prints the contents of a previously saved user data file.
    Handles both missing files and I/O errors gracefully."""
    try:
        with open(filename, "r") as file:
            content = file.read()
        print(f"\nReading from {filename}:")
        print(content)
    except FileNotFoundError:
        print(f"\nFile {filename} not found.")
    except IOError as e:
        print(f"Error reading file: {e}")


def show_menu():
    """Displays the main program menu with six options and returns the user's menu selection as a string."""
    print("\n" + "=" * 50)
    print("HELLO WORLD - MAIN MENU")
    print("=" * 50)
    print("1. Personalized Greeting")
    print("2. Counting Game (FizzBuzz)")
    print("3. Multiplication Table")
    print("4. Student Profile Demo")
    print("5. Save & Read User Data (File I/O)")
    print("6. Exit Program")
    print("=" * 50)
    choice = input("Enter your choice (1-6): ")
    return choice


def run_student_demo():
    """Runs a complete demonstration of the Student class: creates a student, enrolls in three
    courses, assigns grades, and displays the resulting student profile and GPA."""
    student = Student("Kenneth Maberi", "CSE2024001", "Computer Science")
    student.enroll_course("CSE 310 - Applied Programming")
    student.enroll_course("CSE 111 - Programming with Functions")
    student.enroll_course("CSE 210 - Programming with Classes")
    student.assign_grade("CSE 310 - Applied Programming", "A")
    student.assign_grade("CSE 111 - Programming with Functions", "A")
    student.assign_grade("CSE 210 - Programming with Classes", "B")
    student.display_student_info()


def main():
    """Entry point of the Hello World program. Displays the welcome message and loops
    through the menu system until the user chooses to exit (option 6)."""
    print_welcome_message()

    while True:
        choice = show_menu()

        if choice == "1":
            user_info = get_user_info()
            current_year = 2026
            birth_year = calculate_birth_year(current_year, user_info["age"])
            display_personalized_greeting(user_info, birth_year)

        elif choice == "2":
            count_to_number()

        elif choice == "3":
            multiplication_table()

        elif choice == "4":
            run_student_demo()

        elif choice == "5":
            user_info = get_user_info()
            save_user_to_file(user_info)
            read_user_from_file()

        elif choice == "6":
            print("\nThank you for using the Hello World program!")
            print("Goodbye and have a wonderful day!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
