from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})



class Bunny(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)
# Changing this instance method does not impact the database, therefore no migrations necessary
    def __str__(self):
        return f'{self.name} ({self.id})'
    def get_absolute_url(self):
        return reverse('detail', kwargs={'bunny_id': self.id})
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


class Photo(models.Model):
    url = models.CharField(max_length=200)
    bunny = models.ForeignKey(Bunny, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for bunny_id: {self.bunny_id} @{self.url}"



class Feeding(models.Model):
    date = models.DateField('Feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0])
    # Create a bunny_id FK
    bunny = models.ForeignKey(Bunny, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'
    # change the default sort
    class Meta:
        ordering = ['-date']
