from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
  user = models.OneToOneField(User)
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  views = models.IntegerField()

  def __unicode__(self):
    return self.name

class Post(models.Model):
  blog = models.ForeignKey(Blog)
  title = models.CharField(max_length=50)
  content = models.TextField()

  def __unicode__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey(Post)
  user = models.ForeignKey(User, unique=False, related_name='+')
  content = models.CharField(max_length=200)

  def __unicode__(self):
    return self.content

# class UserProfile(models.Model):
#   user = models.OneToOneField(User, related_name="profile_owner")
#   followers = models.ForeignKey(User, related_name="followers")
#   following = models.ForeignKey(User, related_name="following")

#   @staticmethod
#   def follow(follower, followee):
#     up1 = UserProfile.objects.filter(follower.id)
#     up1.following_set.add(followee)
#     up2 = UserProfile.objects.filter(followee.id)
#     up2.followers_set.add(follower)

#   def __unicode__(self):
#     return "following: " + self.following + " followers: " + self.followers