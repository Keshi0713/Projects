import datetime
import os

class AttendanceSystem:
    def __init__(self):
        self.attendance_record = {}

    def mark_attendance(self, student_id, status, course):
        if student_id in self.attendance_record:
            print("Attendance already marked for this student.")
        else:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.attendance_record[student_id] = {'status': status, 'course': course, 'time': current_time}
            print("Attendance marked successfully.")

    def remove_attendance(self, student_id):
        if student_id in self.attendance_record:
            del self.attendance_record[student_id]
            print(f"The attendance {student_id} has been successfully removed")
        else:
            print("Unable to find Student, Make sure you input the right student id")

    def view_attendance(self):
        print("Attendance Report:")
        for student_id, data in self.attendance_record.items():
            status = data['status']
            course = data['course']
            time = data['time']
            print(f"Student ID: {student_id} - Status: {status} - Course: {course} - Time: {time}")

        self.write_attendance_to_file()

    def write_attendance_to_file(self):
        try:
            # Get the directory of the script file
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, 'attendance_report.txt')
            
            with open(file_path, 'w') as file:
                file.write("Attendance Report:\n")
                for student_id, data in self.attendance_record.items():
                    status = data['status']
                    course = data['course']
                    time = data['time']
                    file.write(f"Student ID: {student_id} - Status: {status} - Course: {course} - Time: {time}\n")
            print("Attendance report written to file successfully.")
        except Exception as e:
            print("An error occurred while writing the attendance report to file:", e)

    def display_attendance_from_file(self):
        try:
            with open('attendance_report.txt', 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("Attendance report file not found.")
def main():
    attendance_system = AttendanceSystem()
    
    while True:
        print("\n1. Mark Attendance")
        print("2. Remove an Attendee")
        print("3. View Attendance Report")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            student_id = input("Enter student ID: ")
            status = input("Enter status (regular/irregular): ")
            course = input("Enter your course: ")
            attendance_system.mark_attendance(student_id, status, course)
        elif choice == '2':
            student_id = input("Enter Student ID you want to remove: ")
            attendance_system.remove_attendance(student_id)
        elif choice == '3':
            attendance_system.view_attendance()  # Ensure this is called on the attendance_system instance
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()