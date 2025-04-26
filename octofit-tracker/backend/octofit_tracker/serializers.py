from rest_framework import serializers

# Define serializers for the collections
class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)

# Add serializers for all collections
class TeamSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.CharField())

class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField()
    activity_type = serializers.CharField(max_length=50)
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField()
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
