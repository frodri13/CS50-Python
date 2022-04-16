students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

for i in range(len(students)):
    print(i, students[i])

print(len(students))

students1 = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students1:
    print(student, students1[student], sep=", ")