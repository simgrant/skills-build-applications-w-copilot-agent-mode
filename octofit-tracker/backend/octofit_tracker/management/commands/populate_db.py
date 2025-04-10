from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', password='thundergodpassword'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', password='metalgeekpassword'),
            User(email='zerocool@mhigh.edu', name='Elliot Alderson', password='zerocoolpassword'),
            User(email='crashoverride@hmhigh.edu', name='Dade Murphy', password='crashoverridepassword'),
            User(email='sleeptoken@mhigh.edu', name='Sleep Token', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(name='Blue Team', members=[users[0], users[1]])
        team2 = Team(name='Gold Team', members=[users[2], users[3], users[4]])
        team1.save()
        team2.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60, date=date(2025, 4, 9)),
            Activity(user=users[1], type='Crossfit', duration=120, date=date(2025, 4, 8)),
            Activity(user=users[2], type='Running', duration=90, date=date(2025, 4, 7)),
            Activity(user=users[3], type='Strength', duration=30, date=date(2025, 4, 6)),
            Activity(user=users[4], type='Swimming', duration=75, date=date(2025, 4, 5)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team1, points=200),
            Leaderboard(team=team2, points=300),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))