from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        app_label = 'tracker'

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.JSONField()

    class Meta:
        app_label = 'tracker'

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()

    class Meta:
        app_label = 'tracker'

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

    class Meta:
        app_label = 'tracker'

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        app_label = 'tracker'