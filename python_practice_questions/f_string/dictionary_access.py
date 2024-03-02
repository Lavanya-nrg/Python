# Define a dictionary of student grades
student_grades = {"Lavanya": 30, "Simran": 80, "Vicky": 95}

# Attempting to access the grade for 'lavanya', but there is no 'lavanya' key in the dictionary
# This will result in a KeyError
# Fixing this to access the grade for 'Lavanya' instead
message = f"Lavanya scored {student_grades['Lavanya']} in the exam."
