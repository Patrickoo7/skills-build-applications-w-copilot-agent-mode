from django.test import TestCase

# Add tests for all collections
class UserModelTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email='testuser@example.com', name='Test User')
        self.assertEqual(user.email, 'testuser@example.com')

class TeamModelTestCase(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTestCase(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(user_id='123', activity_type='Running', duration=30)
        self.assertEqual(activity.activity_type, 'Running')

class LeaderboardModelTestCase(TestCase):
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(user_id='123', score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTestCase(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Description')
        self.assertEqual(workout.name, 'Test Workout')
