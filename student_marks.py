def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "Fail"


students = ["Alice", "Bob", "Charlie", "David", "Eve"]
marks = [92, 78, 55, 67, 85]

print("Student Report")
print("-" * 30)

for i in range(len(students)):
    grade = calculate_grade(marks[i])
    print(f"{students[i]:10} {marks[i]:3}  Grade: {grade}")