score = int(input("Score: "))

if 90 <= score and score <= 100:
    print("Grade: A")
elif 80 <= score <= 90:
    print("Grade: B")
elif 70 <= score <= 90:
    print("Grade: C")
elif 60 <= score <= 90:
    print("Grade: D")
else:
    print("Grade: F")