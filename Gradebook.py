#Dictionary containing all relevant information regarding Lloyd.
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

#Dictionary containing all relevant information regarding Alice.
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

#Dictionary containing all relevant information regarding Tyler.
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

#Function which takes the list of all numbers and returns the average.
def average(numbers):
    total = sum(numbers)
    total = float(total)
    total = total / len(numbers)
    return total

#Function which calculates the weighted average of individual students.
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return (0.1 * homework) + (0.3 * quizzes) + (0.6 *     tests)
   
#Function which determines the appropriate letter grade a score receives.   
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

#Function which calculates the class average.
def get_class_average(students):
    results = []
    for student in students:
        new = get_average(student)
        results.append(new)
    return average(results)

#Prints the class average numeric score and letter grade.
students = [lloyd, alice, tyler]
print get_class_average(students)
print get_letter_grade(get_class_average(students))