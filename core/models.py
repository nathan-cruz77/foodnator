from django.db import models
from django.contrib.auth.models import User


class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser")
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class PriceRange(models.Model):
    name = models.CharField(max_length=64)


class Cuisine(models.Model):
    name = models.CharField(max_length=255)


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    delivery_fee = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    price_range = models.ForeignKey(PriceRange)
    cuisine = models.ForeignKey(Cuisine)


class Preference(models.Model):
    type = models.CharField(max_length=64)

    user = models.ForeignKey(User)
    cuisine = models.ForeignKey(Cuisine)


class Group(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
