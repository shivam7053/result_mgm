import csv
import random
import uuid

# Define parameters
colleges = [f"College_{i}" for i in range(1, 11)]  # 10 colleges
streams = [f"Stream_{i}" for i in range(1, 9)]  # 8 streams
semesters = [f"Semester_{i}" for i in range(1, 9)]  # 8 semesters
subjects = [f"Subject_{i}" for i in range(1, 7)]  # 6 subjects per semester
num_students_per_batch = 100

# Function to generate random names
def generate_student_name():
    first_names = ["John", "Jane", "Mike", "Emma", "Liam", "Sophia", "Noah", "Olivia", "Ava", "Mason"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Open CSV file to write
with open("result_management_dataset.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(["University Roll No", "College", "Stream", "Student Name", "Batch", "Semester", "Subject", "Score"])
    
    # Generate data
    roll_number = 1
    for college in colleges:
        for stream in streams:
            for student_num in range(1, num_students_per_batch + 1):
                student_name = generate_student_name()
                batch = random.randint(2018, 2024)  # Assuming batch years between 2018-2024
                
                # For each student, generate scores for all semesters and subjects
                for semester in semesters:
                    for subject in subjects:
                        score = random.randint(40, 100)  # Random score between 40 and 100
                        # Create unique university roll number
                        university_roll_no = f"{roll_number:04d}-{uuid.uuid4().hex[:6]}"
                        writer.writerow([university_roll_no, college, stream, student_name, batch, semester, subject, score])
                    
                roll_number += 1

print("Dataset generated successfully!")
