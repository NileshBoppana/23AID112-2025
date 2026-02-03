def process_student_grades(students):
    passing_count = 0
    failing_names_set = set()

    for student in students:
        name = student['name']
        grades = student['grades']
        attendance = student['attendance']

        # Handle empty grades list
        if len(grades) == 0:
            print("Error: Grades list is empty for", name)
            failing_names_set.add(name)
            continue

        average = sum(grades) / len(grades)

        # Pass / Fail condition
        if average >= 70 and attendance >= 80:
            passing_count += 1
        else:
            failing_names_set.add(name)

    return (passing_count, failing_names_set)
