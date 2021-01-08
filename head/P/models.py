from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Filament(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=10)
    brand = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    date_added = models.DateTimeField()
    qty = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField()
    weight = models.FloatField()
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="image/", verbose_name="main", null=True)
    describe = models.TextField(max_length=1000, null=True, blank=True)


class FilamentImage(models.Model):
    filament = models.ForeignKey(Filament, default=None, on_delete=models.CASCADE, null=True)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return f"{self.filament.brand} {self.filament.type} {self.filament.color} {self.filament.brand}"


@receiver(post_delete, sender=Filament)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
