from django.db import models

# Model for the student result data
class StudentResult(models.Model):
    university_roll_no = models.CharField(max_length=50, unique=True)
    college = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)
    student_name = models.CharField(max_length=100)
    batch = models.IntegerField()
    semester = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.university_roll_no} - {self.student_name}"

    @property
    def average_score(self):
        # Get average score of a student for the current semester
        student_scores = StudentResult.objects.filter(university_roll_no=self.university_roll_no, semester=self.semester)
        total_score = sum([result.score for result in student_scores])
        return total_score / len(student_scores)
    
    @property
    def cgpa(self):
        # Assuming CGPA is calculated out of 10 based on average score
        average = self.average_score
        return round((average / 100) * 10, 2)
