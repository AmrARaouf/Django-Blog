from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
  user = models.OneToOneField(User)
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  views = models.IntegerField()
  date = models.DateTimeField('date published')

  def __unicode__(self):
    return self.name

class Post(models.Model):
  blog = models.ForeignKey(Blog)
  title = models.CharField(max_length=50)
  content = models.TextField()
  date = models.DateTimeField('date published')

  def __unicode__(self):
    return self.title

class Comment(models.Model):
  post = models.OneToOneField(Post)
  user = models.OneToOneField(User)
  content = models.CharField(max_length=200)

  def __unicode__(self):
    return self.content

class UserProfile(models.Model):
  user = models.OneToOneField(User, related_name="profile_owner+")
  followers = models.ForeignKey(User, related_name="followers+")
  following = models.ForeignKey(User, related_name="following+")

  @staticmethod
  def follow(follower, followee):
    follower.following_set.add(followee)
    followee.followers_set.add(follower)

  def __unicode__(self):
    return "following: " + self.following + " followers: " + self.followers