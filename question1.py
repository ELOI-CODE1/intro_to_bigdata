def input_student_info():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grades = []
    num_courses = int(input("Enter number of courses (2 or 3): "))
    
    for i in range(num_courses):
        grade = float(input(f"Enter grade for course {i+1}: "))
        grades.append(grade)
        
    return name, age, grades

def calculate_average(grades):
    return sum(grades) / len(grades)

def display_info(name, age, grades, average):
    print("\n--- Student Information ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grades: {grades}")
    print(f"Average Grade: {average:.2f}")

# Main
name, age, grades = input_student_info()
average = calculate_average(grades)
display_info(name, age, grades, average)
