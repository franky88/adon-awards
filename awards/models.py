from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
import uuid
# Create your models here.
User = settings.AUTH_USER_MODEL


class AwardTitle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title.title()


def background_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance, filename)


class CertBG(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    background = models.ImageField(
        upload_to=background_directory_path, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name).title()


class Awardee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    award_code = models.CharField(max_length=8, unique=True, blank=True)
    award_title = models.ForeignKey(AwardTitle, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateField(
        help_text="Date of the awarding ceremony", verbose_name="date of awarding")
    Gender = models.TextChoices('Gender', 'Male Female')
    gender = models.CharField(
        default="Male", choices=Gender.choices, max_length=10)
    background = models.ForeignKey(
        CertBG, on_delete=models.CASCADE, blank=True, null=True, verbose_name="background theme")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.name.title()


@receiver(post_save, sender=Awardee)
def post_save_create_code(sender, created, instance, *args, **kwargs):
    if created:
        instance.award_code = str(uuid.uuid4()).replace("-", "").upper()[:8]
        instance.save()
