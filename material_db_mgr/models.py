from django.db import models

# Create your models here.

class Unit(models.Model):
    unit = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.unit

class Material(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class MaterialLineItem(models.Model):
    date = models.DateField()
    location = models.TextField()
    remarks = models.TextField()
    quantity = models.PositiveBigIntegerField()
    material_name = models.ForeignKey(Material, on_delete=models.PROTECT)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.date}_{self.material_name}_{self.location}"[:20]

