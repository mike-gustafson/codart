from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create Dart model
class Dart(models.Model):
    user = models.ForeignKey(User, related_name="darts", on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=128)
    code_block = models.TextField(max_length=1024)
    date_created = models.DateTimeField(auto_now_add=True)
    code_language = models.CharField(max_length=100)
    likes = models.ManyToManyField(User, related_name='dart_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='dart_dislikes', blank=True)

    # track number of likes
    def total_likes(self):
        return self.likes.count()
    
    # track number of dislikes
    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return(
            f"User: {self.user}, Title: {self.title}, Description: {self.description}, Code Block: {self.code_block}"
        )

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.jpg', upload_to='images')
    follow = models.ManyToManyField("self",
        related_name='followed_by',
        symmetrical=False,
        blank=True)
    date_modified = models.DateTimeField(User, auto_now=True)
    dart_likes = models.ManyToManyField(Dart, related_name='dart_likes', blank=True)
    dart_dislikes = models.ManyToManyField(Dart, related_name='dart_dislikes', blank=True)


    def __str__(self):
        first_name = self.user.first_name
        last_name = self.user.last_name
        username = self.user.username
        return f"{first_name} {last_name}: @{username}"

# create profile for each user on signup
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

        # user needs to follow themselves when account is created
        user_profile.follow.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile, sender=User)