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

students2 = [
    {"name":  "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name":  "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name":  "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terry"},
    {"name":  "Draco", "house": "Slytherin", "patronus": None},
]

for student in students2:
    print(student["name"], student["house"], student["patronus"], sep=", ")