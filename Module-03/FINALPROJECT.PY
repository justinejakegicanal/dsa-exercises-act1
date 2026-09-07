# FINAL CHALLENGE: STUDENT GRADE ANALYZER
def display_students(students, grades):
    for i in range(len(students)):
        print(students[i], "-", grades[i])

def calculate_average(grades):
    return sum(grades) / len(grades)

def get_passing_students(students, grades):
    return [students[i] for i in range(len(students)) if grades[i] >= 75]

def get_failing_students(students, grades):
    return [students[i] for i in range(len(students)) if grades[i] < 75]

# Main program
students = []
grades = []

# Add student records (1-5 failing, 6-10 high grades)
raw_data = [
    ("Conrad", 68), ("Jake", 70), ("Renzo", 65), ("Vhon", 72), ("Daryll", 60),
    ("Luis", 88), ("Wilson", 85), ("Kryzle", 94), ("Rexine", 99), ("Julia", 92)
]

for name, score in raw_data:
    students.append(name)
    grades.append(score)

# List Comprehension 3 (grades above 90)
above_90 = [students[i] for i in range(len(students)) if grades[i] > 90]

# List copy, ==, is, and id() check
grades_copy = grades.copy()

# Display results
print("Student Grade Analyzer")
print("=======================")

print("\n1. All students (10 students):")
display_students(students, grades)

print("\n2. All grades:", grades)

# Indexing gamit ang index ng max at min
max_idx = grades.index(max(grades))
min_idx = grades.index(min(grades))

print(f"\n3. Highest grade: {grades[max_idx]} ({students[max_idx]})")
print(f"4. Lowest grade: {grades[min_idx]} ({students[min_idx]})")
print("5. Average grade:", calculate_average(grades))

print("\n6. Passing students:", get_passing_students(students, grades))
print("7. Failing students:", get_failing_students(students, grades))
print("8. Students with grades above 90:", above_90)

# 'in' operator check and Memory Identity verification
print("\nIs 'Jake' in students?", "Jake" in students)
print("grades == grades_copy:", grades == grades_copy)
print("grades is grades_copy:", grades is grades_copy)
print("Original ID:", id(grades), "| Copy ID:", id(grades_copy))

