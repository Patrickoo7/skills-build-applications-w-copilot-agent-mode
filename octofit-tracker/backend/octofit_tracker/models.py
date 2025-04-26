# Define models for MongoDB collections
from mongoengine import Document, StringField, ListField, IntField

class User(Document):
    email = StringField(required=True, unique=True)
    name = StringField(max_length=100)

class Team(Document):
    name = StringField(required=True, unique=True)
    members = ListField(StringField())

class Activity(Document):
    user_id = StringField(required=True)
    activity_type = StringField(max_length=50)
    duration = IntField()

class Leaderboard(Document):
    user_id = StringField(required=True)
    score = IntField()

class Workout(Document):
    name = StringField(max_length=100)
    description = StringField()
