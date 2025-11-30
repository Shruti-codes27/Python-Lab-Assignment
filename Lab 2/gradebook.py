# Name: Shruti
# Date: 30 Nov 2025
# Title: GradeBook Analyzer


def manual_input():
    d = {}
    num = int(input("How many students to enter: "))
    for i in range(num):
        print(f"--- Enter details for Student {i+1} ---")
        name = input("Enter the name: ")
        marks = int(input("Enter marks: "))
        d[name] = marks
    return d


def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)


def calculate_median(marks_dict):
    marks = sorted(marks_dict.values())
    mid = len(marks) // 2
    n = len(marks)
    if n % 2 == 0:
        return (marks[mid] + marks[mid - 1]) / 2
    else:
        return marks[mid]


def find_max(marks_dict):
    return max(marks_dict.values())


def find_min(marks_dict):
    return min(marks_dict.values())


def grade_section(marks_dict):
    grade = {}
    for name, marks in marks_dict.items():
        if marks >= 90:
            grade[name] = 'A'
        elif marks >= 80:
            grade[name] = "B"
        elif marks >= 70:
            grade[name] = "C"
        elif marks >= 60:
            grade[name] = "D"
        else:
            grade[name] = "F"
    return grade


def grade_distribution(grade_dict):
    distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grade_dict.values():
        distribution[grade] += 1
    return distribution


# ---------- TASK 5: PASS/FAIL FILTER ----------
def pass_fail_filter(marks_dict):
    passed_students = [name for name, marks in marks_dict.items() if marks >= 40]
    failed_students = [name for name, marks in marks_dict.items() if marks < 40]
    return passed_students, failed_students


# ---------- MAIN PROGRAM ----------
d = manual_input()
print("===================")
print("📘 STUDENT MARKS DATA")
print("=====================")
for name, marks in d.items():
    print(f"{name:<15} : {marks}")

avg = calculate_average(d)
med = calculate_median(d)
max_marks = find_max(d)
min_marks = find_min(d)

grades = grade_section(d)
gd = grade_distribution(grades)

print("====================")
print(" STATISTICS")
print("======================")
print(f"Average Marks       : {avg:.2f}")
print(f"Median Marks        : {med}")
print(f"Highest Marks       : {max_marks}")
print(f"Lowest Marks        : {min_marks}")

print("====================")
print(" GRADES")
print("======================")
for name, grade in grades.items():
    print(f"{name:<15} : Grade {grade}")

print("====================")
print(" GRADE DISTRIBUTION")
print("======================")
for grade, count in gd.items():
    print(f"Grade {grade} : {count} student(s)")

# ---------- NEW PASS/FAIL SECTION ----------
passed, failed = pass_fail_filter(d)
print("========================")
print(" PASS/FAIL ANALYSIS")
print("=========================")
print(f"Passed Students ({len(passed)}): {', '.join(passed) if passed else 'None'}")
print(f"Failed Students ({len(failed)}): {', '.join(failed) if failed else 'None'})")

print("Program Execution Completed Successfully!")