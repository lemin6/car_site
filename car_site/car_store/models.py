from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.category_name

class Marka(models.Model):
    name_marka = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name_marka

class Model(models.Model):
    name_model = models.CharField(max_length=16, unique=True)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_model

class Car(models.Model):
    name_car = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    year = models.IntegerField()
    type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

# class Car(models.Model):
#     name_car = models.CharField(max_length=32)
#     price = models.PositiveIntegerField(default=0)
#     marka = models.ForeignKey(Model, on_delete=models.CASCADE)
#     model = models.ForeignKey(Model, on_delete=models.CASCADE)
#     category = models.ForeignKey(Model, on_delete=models.CASCADE)
#     description = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     year = models.SmallIntegerField()
#     image = models.ImageField(upload_to='img/')

    def __str__(self):
        return f'{self.markal} - {self.name_car}'