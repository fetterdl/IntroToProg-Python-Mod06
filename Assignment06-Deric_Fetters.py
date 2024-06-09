# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   DFetters,5/30/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json
import io

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str = ""  # Hold the choice made by the user.

# Processing ----------------------------------------------#
class ProcessFileData:
    """
    This class is a collection of processing functions that work with json files

    Change Log: (Who, When, What)
    DFetters, 05/30/2024, Created Class
        Added read_data_from_file
        Added function to write_data_to_file functions

    """
    @staticmethod
    def read_data_from_file(file_name: str, students: list):
        """ This function reads the data from the Enrollments.json file and returns list students

        Change Log: (Who, When, What)
        DFetters, 05/30/2024, created function

        """

        try:
            file = io.TextIOWrapper
            file = open(file_name, "r")
            students = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages(message="Text file must exist before running this script", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        finally:
            if file.closed == False:
                 file.close()
        return students

    @staticmethod
    def write_data_to_file(file_name: str, students: list):
        """ This function writes the data to the Enrollments.json file

        Change Log: (Who, When, What)
        DFetters, 05/30/2024, created function

        """
        try:
            file = open(file_name, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()

            IO.output_error_messages(message="Error: There was a problem with writing to the file. \n"
                                 "Please check that the file is not open by another program.", error=e)

# Presentation --------------------------------------------#
class IO:
    """
    This class is a collection of functions that manage user input and output

    Change log: (Who, When, What)
    DFetters, 05.030.2024, Created Class,
        Added functions to display custom error messages,
        Added function to display the option menu,
        Added function to input menu choice
        Added function to input student data
        Added function to output

    """
    @staticmethod
    def output_error_messages (message: str, error: Exception = None):
        """ This function displays a custom error messages to the user
        
            NOTE: Error messages can be customized
        
        Change Log: (Who, When What)
        DFetters, 05.30.2024, Created function
        
        return: None

        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error.__str__(), error.__doc__, type(error), sep='\n\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function outputs the option menu to the user

        Change Log: (Who, When, What)
        DFetters, 05.30.2024, Created function

        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """ This function inputs the menu option from the user

        Change Log: (Who, When, What)
        DFetters, 05.30.2024, Created function

        """

        menu_choice: str = input("What would you like to do?: ")
        return menu_choice

    @staticmethod
    def output_student_courses(students: list):
        """ This function outputs current data to the screen

        Change Log: (Who, When, What)
        DFetters, 05.30.2024, Created function

        """

        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(students: list):
        """ This function inputs student data from the user

        Change Log: (Who, When, What)
        DFetters, 05.30.2024, Created function

        """

        try:
            student_first_name = input("\n Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("\nThe last name should not contain numbers.")
            student_last_name = input("\n Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("\nThe last name should not contain numbers.")
            course_name = input("\n Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            # adds new data to students list
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return students

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

students = ProcessFileData.read_data_from_file(file_name= FILE_NAME, students=students)

while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    # Request menu input from the user
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!

         students = IO.input_student_data(students=students)
         continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        ProcessFileData.write_data_to_file("FILE_NAME", students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
