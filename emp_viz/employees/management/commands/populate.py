from django.core.management.base import BaseCommand
from employees.models import Employee, Attendance, Performance
from faker import Faker
import random
from datetime import timedelta

fake = Faker()

class Command(BaseCommand):
    help = 'Populate database with synthetic employee data'

    def handle(self, *args, **kwargs):
        for _ in range(5):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                department=random.choice(['IT', 'HR', 'Finance']),
                joining_date=fake.date_between(start_date='-2y', end_date='today')
            )

            for _ in range(5):
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_this_year(),
                    status=random.choice(['Present', 'Absent'])
                )

                Performance.objects.create(
                    employee=emp,
                    rating=round(random.uniform(1, 5), 1),
                    review_date=fake.date_this_year(),
                    comment=fake.sentence()
                )
