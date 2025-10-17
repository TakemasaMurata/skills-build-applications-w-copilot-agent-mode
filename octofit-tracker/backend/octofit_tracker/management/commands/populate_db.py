from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create Users
        users = [
            User(email='tony@stark.com', name='Tony Stark', team='marvel', is_superhero=True),
            User(email='steve@rogers.com', name='Steve Rogers', team='marvel', is_superhero=True),
            User(email='bruce@wayne.com', name='Bruce Wayne', team='dc', is_superhero=True),
            User(email='clark@kent.com', name='Clark Kent', team='dc', is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create Workouts
        workouts = [
            Workout(name='Pushups', description='Do pushups', difficulty='easy'),
            Workout(name='Running', description='Run 5km', difficulty='medium'),
            Workout(name='Deadlift', description='Heavy deadlifts', difficulty='hard'),
        ]
        for workout in workouts:
            workout.save()

        # Create Activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='pushup', duration=15, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='deadlift', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='run', duration=25, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
