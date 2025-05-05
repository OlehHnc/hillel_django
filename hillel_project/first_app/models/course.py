from django.db import models


class Course(models.Model):
    name = models.TextField()
    description = models.TextField()
    learning_plan = models.TextField(null=False, default="Теми ще не додано", verbose_name="Короткий опис тем")

