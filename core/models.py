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

    @classmethod
    def from_int(cls, value):
        mapping = {
            1: 'CHEAPEST',
            2: 'MODERATE',
            3: 'CHEAP',
            4: 'EXPENSIVE',
            5: 'MOST_EXPENSIVE',
        }

        return cls.objects.get(name=mapping[value])

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)


class Cuisine(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    delivery_fee = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    slug = models.SlugField(max_length=255)
    avatar = models.URLField()

    price_range = models.ForeignKey(PriceRange)
    cuisine = models.ForeignKey(Cuisine)

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)


class Preference(models.Model):
    only_free_delivery = models.BooleanField()
    min_rating = models.DecimalField(max_digits=2, decimal_places=1)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    price_range = models.ForeignKey(PriceRange)
    selected_cuisines = models.ManyToManyField(Cuisine, related_name='selected_by')
    rejected_cuisines = models.ManyToManyField(Cuisine, related_name='rejected_by')


class Group(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)
