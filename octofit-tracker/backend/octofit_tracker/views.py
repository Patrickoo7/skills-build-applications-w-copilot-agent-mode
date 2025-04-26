from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout

class UserListCreateView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Similar views for Team, Activity, Leaderboard, and Workout

class api_root(APIView):
    def get(self, request):
        return Response({
            'users': reverse('user-list-create', request=request),
            'teams': reverse('team-list-create', request=request),
            'activity': reverse('activity-list-create', request=request),
            'leaderboard': reverse('leaderboard-list-create', request=request),
            'workouts': reverse('workout-list-create', request=request),
        })
