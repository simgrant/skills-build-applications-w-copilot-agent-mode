from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Test data
        users = [
            {"username": "john_doe", "email": "john@example.com"},
            {"username": "jane_smith", "email": "jane@example.com"},
        ]
        teams = [
            {"name": "Team Alpha", "description": "The first team."},
            {"name": "Team Beta", "description": "The second team."},
        ]
        activities = [
            {"name": "Running", "calories_burned_per_minute": 10},
            {"name": "Cycling", "calories_burned_per_minute": 8},
        ]
        workouts = [
            {"user": "john_doe", "activity": "Running", "duration_minutes": 30},
            {"user": "jane_smith", "activity": "Cycling", "duration_minutes": 45},
        ]
        leaderboard = [
            {"user": "john_doe", "points": 300},
            {"user": "jane_smith", "points": 360},
        ]

        # Populate users
        user_objects = {}
        for user in users:
            obj = User.objects.create(**user)
            user_objects[user["username"]] = obj

        # Populate teams
        for team in teams:
            Team.objects.create(**team)

        # Populate activities
        activity_objects = {}
        for activity in activities:
            obj = Activity.objects.create(**activity)
            activity_objects[activity["name"]] = obj

        # Populate workouts
        for workout in workouts:
            Workout.objects.create(
                user=user_objects[workout["user"]],
                activity=activity_objects[workout["activity"]],
                duration_minutes=workout["duration_minutes"],
            )

        # Populate leaderboard
        for entry in leaderboard:
            Leaderboard.objects.create(
                user=user_objects[entry["user"]],
                points=entry["points"],
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))