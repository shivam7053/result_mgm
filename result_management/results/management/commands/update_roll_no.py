from django.core.management.base import BaseCommand
from results.models import StudentResult

class Command(BaseCommand):
    help = 'Truncate university roll numbers to the first 4 characters'

    def handle(self, *args, **kwargs):
        for result in StudentResult.objects.all():
            new_roll_number = result.university_roll_no[:4]
            result.university_roll_no = new_roll_number
            result.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated university roll numbers!'))
