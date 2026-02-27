class Student:
    def __init__(self, name, roll_no, email, mobile_no, address):
        self.name = name
        self.roll_no = roll_no
        self.email = email
        self.mobile_no = mobile_no
        self.address = address

    def display_details(self):
        print("Student Details")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Email:", self.email)
        print("Mobile No:", self.mobile_no)
        print("Address:", self.address)


# ---- Main Program ----
if __name__ == "__main__":
    student = Student(
        name="shiva",
        roll_no=66,
        email="shiva@example.com",
        mobile_no="9776590243",
        address="pune, India"
    )

    student.display_details()
    

