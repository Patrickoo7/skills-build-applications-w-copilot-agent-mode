from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from mongoengine import connect
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        connect(db="octofit_db", host="localhost", port=27017)

        # Drop existing collections
        User.objects.delete()
        Team.objects.delete()
        Activity.objects.delete()
        Leaderboard.objects.delete()
        Workout.objects.delete()

        # Create users
        users = [
            User(id=ObjectId(), email='thundergod@mhigh.edu', name='Thor'),
            User(id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark'),
            User(id=ObjectId(), email='zerocool@mhigh.edu', name='Steve Rogers'),
            User(id=ObjectId(), email='crashoverride@mhigh.edu', name='Natasha Romanoff'),
            User(id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce Banner'),
        ]
        for user in users:
            user.save()

        # Create teams
        teams = [
            Team(id=ObjectId(), name='Blue Team', members=[users[0].id, users[1].id]),
            Team(id=ObjectId(), name='Gold Team', members=[users[2].id, users[3].id, users[4].id]),
        ]
        for team in teams:
            team.save()

        # Create activities
        activities = [
            Activity(id=ObjectId(), user_id=users[0].id, activity_type='Cycling', duration=60),
            Activity(id=ObjectId(), user_id=users[1].id, activity_type='Crossfit', duration=120),
            Activity(id=ObjectId(), user_id=users[2].id, activity_type='Running', duration=90),
            Activity(id=ObjectId(), user_id=users[3].id, activity_type='Strength', duration=30),
            Activity(id=ObjectId(), user_id=users[4].id, activity_type='Swimming', duration=75),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(id=ObjectId(), user_id=users[0].id, score=100),
            Leaderboard(id=ObjectId(), user_id=users[1].id, score=90),
            Leaderboard(id=ObjectId(), user_id=users[2].id, score=95),
            Leaderboard(id=ObjectId(), user_id=users[3].id, score=85),
            Leaderboard(id=ObjectId(), user_id=users[4].id, score=80),
        ]
        for entry in leaderboard_entries:
            entry.save()

        # Create workouts
        workouts = [
            Workout(id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
