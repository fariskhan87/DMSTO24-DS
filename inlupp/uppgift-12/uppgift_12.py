def create_student_register(students):
    return dict(students)
def main():
    students = [("Alice", 20), ("Bob", 25), ("Charlie", 22)]
    student_register = create_student_register(students)
    print(student_register) 


if __name__ == "__main__":
    main()

