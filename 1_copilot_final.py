# Tasks C and D: add students and correct Jon's name
students = ['Jon', 'Kim', 'Lee']
students.append('Sara')
students.append('Miko')
# change Jon to John (index 0, not index 1)
students[0] = 'John'

def greet_students():
    for student in students:
        print(f'Hi {student}')
    print(f'Total number of students: {len(students)}')

greet_students()
