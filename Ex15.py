class Node:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
        self.status = "Not Marked"
        self.next = None


class StudentAttendanceSystem:
    def __init__(self):
        self.head = None

    def add_student(self, sid, name):
        if self.search_student(sid):
            print("Student ID already exists")
            return

        new_node = Node(sid, name)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print("Student added successfully")

    def search_student(self, sid):
        temp = self.head

        while temp:
            if temp.sid == sid:
                return temp
            temp = temp.next

        return None

    def mark_attendance(self, sid, status):
        student = self.search_student(sid)

        if student:
            student.status = status
            print("Attendance updated successfully")
        else:
            print("Student not found")

    def delete_student(self, sid):
        temp = self.head
        prev = None

        while temp:
            if temp.sid == sid:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next

                print("Student deleted successfully")
                return

            prev = temp
            temp = temp.next

        print("Student not found")

    def display_report(self):
        temp = self.head
        present = absent = unmarked = total = 0

        print("\nSTUDENT ATTENDANCE REPORT")
        print("-" * 45)

        while temp:
            print(temp.sid, temp.name, temp.status)

            total += 1

            if temp.status == "Present":
                present += 1
            elif temp.status == "Absent":
                absent += 1
            else:
                unmarked += 1

            temp = temp.next

        print("-" * 45)
        print("Total Students:", total)
        print("Present:", present)
        print("Absent:", absent)
        print("Not Marked:", unmarked)


system = StudentAttendanceSystem()

while True:
    print("\n1. Add Student")
    print("2. Mark Attendance")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Display Report")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        system.add_student(sid, name)

    elif choice == "2":
        sid = input("Enter Student ID: ")
        status = input("Enter Present or Absent: ").strip().title()

        if status in ["Present", "Absent"]:
            system.mark_attendance(sid, status)
        else:
            print("Invalid attendance status")

    elif choice == "3":
        sid = input("Enter Student ID: ")
        student = system.search_student(sid)

        if student:
            print("ID:", student.sid)
            print("Name:", student.name)
            print("Attendance:", student.status)
        else:
            print("Student not found")

    elif choice == "4":
        sid = input("Enter Student ID: ")
        system.delete_student(sid)

    elif choice == "5":
        system.display_report()

    elif choice == "6":
        print("Thank you")
        break

    else:
        print("Invalid choice")
