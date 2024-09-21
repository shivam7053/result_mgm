import csv
from django.core.management.base import BaseCommand
from results.models import StudentResult

class Command(BaseCommand):
    help = "Load result data from CSV"

    def handle(self, *args, **kwargs):
        with open('/workspaces/result_mgm/result_management_dataset.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                StudentResult.objects.create(
                    university_roll_no=row['University Roll No'],
                    college=row['College'],
                    stream=row['Stream'],
                    student_name=row['Student Name'],
                    batch=row['Batch'],
                    semester=row['Semester'],
                    subject=row['Subject'],
                    score=row['Score']
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
