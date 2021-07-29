from django.db import models
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField
from django.conf import settings


class OpenWeatherCity(models.Model):
    name = models.CharField(
        verbose_name=_("City Name"),
        max_length=150, null=False, blank=False
    )
    country = models.CharField(
        verbose_name=_("Country"), max_length=10,
        null=False, blank=False
    )
    open_weather_id = models.IntegerField(
        _("Open Weather ID"), null=False, blank=False
    )

    class Meta:
        verbose_name = _("Open Weather City")
        verbose_name_plural = _("Open Weather Cities")

    def __str__(self):
        return f"{self.open_weather_id} - {self.name}, {self.country}"

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    location = models.CharField(max_length=50, blank=True)
    photo = CloudinaryField('image')
    bio = models.TextField(max_length=200, default= 'Hello friends', blank=True)

    def save_profile(self):
        self.save()

    def delete_profile():
        self.delete()

    def __str__(self):
        return self.user.username

    @classmethod
    def update_profile():
        self.update()