# Task I: infer likely rules from examples:
# Math GPA >= 3.50; Biology GPA >= 2.75
students = {
    'Jon': (3.25, 'Math'), 'Kim': (2.25, 'Biology'),
    'Lee': (2.30, 'Math'), 'Sara': (4.00, 'Math'),
    'Miko': (1.90, 'Math'), 'Lin': (2.10, 'Biology'),
    'Toby': (2.89, 'Biology'), 'Ben': (2.75, 'Math'),
    'Mark': (2.34, 'Math'), 'Xia': (3.53, 'Biology')
}
total = 0
for gpa, major in students.values():
    total += gpa
average = total / len(students)
print(f'Average GPA: {average:.2f}')
print('Above-average students:')
for name, (gpa, major) in students.items():
    if gpa > average:
        print(name, gpa, major)
print('Predicted scholarship recipients:')
for name, (gpa, major) in students.items():
    if (major == 'Math' and gpa >= 3.5) or (major == 'Biology' and gpa >= 2.75):
        print(name, gpa, major)
